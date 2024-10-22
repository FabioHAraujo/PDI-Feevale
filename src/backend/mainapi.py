from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
from PIL import Image
import os
import mirror
import rotate
import scale
import translate
import tempfile
import subprocess
import json
import grayscale
import bright
import contrast
import dilate
import erode
import threshold
import median
import gaussian
import sobel
import prewitt
import laplacian

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos os domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def enviar_para_pocketbase(imagem, nome_original, formato_original):
    try:
        if formato_original.lower() in ['jpeg', 'jpg']:
            imagem = imagem.convert("RGB")
        elif formato_original.lower() == 'png' and imagem.mode == 'RGBA':
            imagem = imagem.convert("RGB")

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f".{formato_original.lower()}")
        caminho_temp = temp_file.name
        temp_file.close()

        imagem.save(caminho_temp, format=formato_original)

        result = subprocess.run(['node', 'enviar_imagem.js', caminho_temp, nome_original], capture_output=True, text=True)
        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Falha ao enviar a imagem para o PocketBase: {result.stderr}")

        os.remove(caminho_temp)

        # Debug da saída do subprocesso
        print(f"Resultado do subprocesso: {result.stdout}")

        # Extraindo a URL do resultado do subprocesso
        try:
            result_json = json.loads(result.stdout)
            imagem_url = result_json.get("url")
            if not imagem_url:
                raise HTTPException(status_code=500, detail="URL da imagem não retornada pelo PocketBase.")
            return imagem_url
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Erro ao decodificar a resposta JSON do PocketBase.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/processar_imagem/")
async def processar_imagem(
    image: UploadFile = File(...),
    operation: str = Form(...),
    params: str = Form(...),
):
    try:
        img = Image.open(image.file)
        formato_original = img.format
        
        print(f"Operation: {operation}")
        print(f"Params: {params}")
        
        try:
            params_list = [float(p) for p in params.split(",")]
        except ValueError:
            return JSONResponse(status_code=400, content={"message": "Parâmetros inválidos. Certifique-se de que são números."})

        if operation == 'translacao':
            if len(params_list) != 2:
                return JSONResponse(status_code=400, content={"message": "Translação requer dois parâmetros (dx e dy)."})
            dx, dy = params_list
            img = translate.translate_image(img, dx, dy)

        elif operation == 'escala':
            if len(params_list) != 1:
                return JSONResponse(status_code=400, content={"message": "Escala requer um parâmetro (fator de escala)."})
            scale_factor = params_list[0]
            img = scale.scale_image(img, scale_factor)

        elif operation == 'rotacao':
            if len(params_list) != 1:
                return JSONResponse(status_code=400, content={"message": "Rotação requer um parâmetro (ângulo de rotação)."})
            angle = params_list[0]
            img = rotate.rotate_image(img, angle)

        elif operation == 'espelhamento':
            if len(params_list) != 1:
                return JSONResponse(status_code=400, content={"message": "Espelhamento requer um parâmetro (1 para vertical, 2 para horizontal)."})
            axis_param = params_list[0]
            axis = 'v' if axis_param == 1 else 'h' if axis_param == 2 else None
            if axis is None:
                return JSONResponse(status_code=400, content={"message": "Parâmetro inválido. Use 1 para vertical ou 2 para horizontal."})
            img = mirror.mirror_image(img, axis)
            
        elif operation == 'grayscale':
            img = grayscale.grayscale(img)
            
        elif operation == 'brilho':
            if len(params_list) != 1:
                return JSONResponse(status_code=400, content={"message": "Brilho requer um parâmetro (intensidade do brilho de 0 a 100)."})
            brilho = params_list[0]/100
            img = bright.bright_adjust(img, brilho)
            
        elif operation == 'contraste':
            if len(params_list) != 1:
                return JSONResponse(status_code=400, content={"message": "Contraste requer um parâmetro (intensidade do contraste de 0 a 20000)."})
            if params_list[0] > 20000:
                return JSONResponse(status_code=400, content={"message": "Parâmetro inválido: valor máximo é 20000."})
            contraste = params_list[0]/100
            img = contrast.contrast_adjust(img, contraste)

        elif operation == 'dilatacao':
            if len(params_list) != 1:
                return JSONResponse(status_code=400, content={"message": "Dilatação requer um parâmetro (tamanho do kernel)."})
            kernel_size = int(params_list[0])
            img = dilate.dilate_image(img, kernel_size)

        elif operation == 'erosao':
            if len(params_list) != 1:
                return JSONResponse(status_code=400, content={"message": "Erosão requer um parâmetro (tamanho do kernel)."})
            kernel_size = int(params_list[0])
            img = erode.erode_image(img, kernel_size)
        
        elif operation == 'limiarizacao':
            if len(params_list) != 1:
                return JSONResponse(status_code=400, content={"message": "Limiarização requer um parâmetro (valor do limiar)."})
            threshold_value = int(params_list[0])
            img = threshold.threshold_image(img, threshold_value)

        elif operation == 'media':
            if len(params_list) != 1:
                return JSONResponse(status_code=400, content={"message": "Média requer um parâmetro (tamanho do kernel)."})
            kernel_size = int(params_list[0])
            img = median.median_filter(img, kernel_size)

        elif operation == 'gaussiano':
            img = gaussian.gaussian_blur(img)

        elif operation == 'sobel':
            img = sobel.sobel_filter(img)

        elif operation == 'prewitt':
            img = prewitt.prewitt_filter(img)

        elif operation == 'laplaciano':
            img = laplacian.laplacian_filter(img)

        else:
            return JSONResponse(status_code=400, content={"message": "Operação inválida."})

        imagem_url = enviar_para_pocketbase(img, image.filename, formato_original)
        return JSONResponse(status_code=200, content={"message": "Imagem processada e enviada com sucesso!", "url": imagem_url})

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Erro ao processar a imagem: {str(e)}"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=39000)
