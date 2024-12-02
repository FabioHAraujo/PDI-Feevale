import cv2
import numpy as np
from PIL import Image

def sobel_filter(img):
    """
    Aplica o filtro Sobel em uma imagem.
    :param img: Imagem PIL (RGB ou escala de cinza).
    :return: Imagem PIL resultante após a aplicação do Sobel.
    """
    # Converter a imagem PIL para NumPy
    img_array = np.array(img)

    # Verificar se a imagem é RGB ou escala de cinza
    if img_array.ndim == 3 and img_array.shape[2] == 3:  # Imagem colorida (RGB)
        # Converter para escala de cinza
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Aplicar o filtro Sobel
    print("Aplicando filtro Sobel...")
    sobel_x = cv2.Sobel(img_array, cv2.CV_64F, 1, 0, ksize=3)  # Gradiente X
    sobel_y = cv2.Sobel(img_array, cv2.CV_64F, 0, 1, ksize=3)  # Gradiente Y
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)  # Magnitude do gradiente

    # Normalizar os valores para 8 bits
    sobel_result = np.uint8(np.clip(sobel_combined, 0, 255))

    # Converter o resultado de volta para imagem PIL
    result_img = Image.fromarray(sobel_result)

    return result_img

# Exemplo de uso
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python main.py <caminho da imagem>")
        sys.exit(1)

    img_path = sys.argv[1]
    img = Image.open(img_path)  # Carregar sua imagem
    sobel_img = sobel_filter(img)
    sobel_img.save("sobel.jpg")  # Salvar a imagem resultante
