import numpy as np
from PIL import Image
from dilate import dilate_image
from erode import erode_image

def opening_image(img, kernel_size):
    """
    Aplica a operação de abertura em uma imagem (erosão seguida de dilatação).
    """
    # Primeiro aplica a erosão
    eroded_img = erode_image(img, kernel_size)

    # Depois aplica a dilatação no resultado da erosão
    opened_img = dilate_image(eroded_img, kernel_size)

    return opened_img

# Exemplo de uso
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Uso: python opening.py <caminho da imagem> <tamanho do kernel>")
        sys.exit(1)

    img_path = sys.argv[1]
    kernel_size = int(sys.argv[2])

    img = Image.open(img_path)  # Carregar sua imagem
    opened_img = opening_image(img, kernel_size)
    opened_img.save("abertura.jpg")  # Salvar a imagem após a abertura
