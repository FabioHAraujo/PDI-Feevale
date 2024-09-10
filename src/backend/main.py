import argparse
import subprocess
import tempfile
import os
import time
from PIL import Image
import mirror
import rotate
import scale
import translate

def enviar_para_pocketbase(imagem, nome_original, formato_original):
    try:
        # Se o formato original for JPEG, converte a imagem para RGB (sem transparência)
        if formato_original.lower() in ['jpeg', 'jpg']:
            imagem = imagem.convert("RGB")

        elif formato_original.lower() == 'png' and imagem.mode == 'RGBA':
            imagem = imagem.convert("RGB")

        # Cria um arquivo temporário com um nome único
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f".{formato_original.lower()}")
        caminho_temp = temp_file.name
        temp_file.close()  # Fecha o arquivo temporário para liberar o arquivo para outros processos

        # Salva a imagem no arquivo temporário
        imagem.save(caminho_temp, format=formato_original)

        # Chama o script Node.js passando o caminho do arquivo temporário
        result = subprocess.run(['node', 'enviar_imagem.js', caminho_temp, nome_original], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Falha ao enviar a imagem para o PocketBase: {result.stderr}")
            return

        print("Imagem enviada para PocketBase com sucesso!")

        # Aguarda um curto período para garantir que o Node.js terminou
        time.sleep(1)

        # Remove o arquivo temporário após o envio
        try:
            os.remove(caminho_temp)
        except Exception as e:
            print(f"Erro ao remover o arquivo temporário: {e}")

    except subprocess.CalledProcessError as e:
        print(f"Falha ao enviar a imagem para o PocketBase: {e}")
    except Exception as e:
        print(f"Erro: {e}")

def main():
    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description="Aplicar operações em uma imagem e enviá-la para PocketBase.")
    parser.add_argument('image_path', type=str, help="Caminho para o arquivo da imagem.")
    parser.add_argument('operation', type=str, choices=['translacao', 'escala', 'rotacao', 'espelhamento'], help="Operação a ser realizada na imagem.")
    parser.add_argument('params', type=str, nargs='*', help="Parâmetros adicionais para a operação escolhida.")

    args = parser.parse_args()

    try:
        # Abre a imagem e obtém seu formato original
        img = Image.open(args.image_path)
        formato_original = img.format  # Captura o formato original (ex: PNG, JPEG)
    except FileNotFoundError:
        print("Arquivo de imagem não encontrado. Verifique o nome e tente novamente.")
        return

    # Conversão dos parâmetros para o tipo correto
    try:
        params = [float(p) for p in args.params]
    except ValueError:
        print("Parâmetros inválidos. Certifique-se de que são números.")
        return
    
    # Realiza a operação na imagem
    if args.operation == 'translacao':
        if len(params) != 2:
            print("Erro: Translação requer dois parâmetros (dx e dy).")
            return
        dx, dy = params
        img = translate.translate_image(img, dx, dy)

    elif args.operation == 'escala':
        if len(params) != 1:
            print("Erro: Escala requer um parâmetro (fator de escala).")    
            return
        scale_factor = params[0]
        img = scale.scale_image(img, scale_factor)

    elif args.operation == 'rotacao':
        if len(params) != 1:
            print("Erro: Rotação requer um parâmetro (ângulo de rotação).")
            return
        angle = params[0]
        img = rotate.rotate_image(img, angle)

    elif args.operation == 'espelhamento':
        if len(args.params) != 1:
            print("Erro: Espelhamento requer um parâmetro (1 para vertical, 2 para horizontal).")
            return
        
        axis_param = params[0]
        axis = 'v' if axis_param == 1 else 'h' if axis_param == 2 else None
        if axis is None:
            print("Erro: Parâmetro inválido. Use 1 para vertical ou 2 para horizontal.")
            return

        img = mirror.mirror_image(img, axis)

    # Envia a imagem processada com o formato original para o PocketBase
    enviar_para_pocketbase(img, args.image_path, formato_original)

if __name__ == "__main__":
    main()
