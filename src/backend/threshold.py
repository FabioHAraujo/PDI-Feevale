import numpy as np
from PIL import Image

def grayscale(image):
    # Converte a imagem para grayscale
    img_array = np.array(image)
    # Calcula a média de cada pixel para converter para escala de cinza
    gray_array = np.mean(img_array, axis=2).astype('uint8')
    # Retorna a imagem em escala de cinza como uma nova imagem PIL
    return Image.fromarray(gray_array, mode='L')

def threshold_image(img, threshold=100):
    # Converte a imagem para escala de cinza
    grayscale_image = grayscale(img)
    
    # Converte a imagem em escala de cinza para um array NumPy
    img_array = np.array(grayscale_image)

    # Aplica o limiar
    binary_array = np.where(img_array >= threshold, 255, 0).astype('uint8')

    # Converte o array binário de volta para uma imagem PIL
    result_img = Image.fromarray(binary_array, mode='L')
    return result_img

# Exemplo de uso
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Uso: python main.py <caminho da imagem> <valor do limiar>")
        sys.exit(1)

    img_path = sys.argv[1]
    threshold_value = int(sys.argv[2])

    img = Image.open(img_path)  # Carregar a imagem
    thresholded_img = threshold_image(img, threshold_value)
    thresholded_img.save("thresholded.jpg")  # Salvar a imagem limiarizada
