import numpy as np
from PIL import Image
from dilate import dilate_image
from erode import erode_image

def closing_image(img, kernel_size):
    """
    Aplica a operação de fechamento em uma imagem (dilatação seguida de erosão).
    """
    # Primeiro aplica a dilatação
    dilated_img = dilate_image(img, kernel_size)

    # Depois aplica a erosão no resultado da dilatação
    closed_img = erode_image(dilated_img, kernel_size)

    return closed_img

# Exemplo de uso
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Uso: python closing.py <caminho da imagem> <tamanho do kernel>")
        sys.exit(1)

    img_path = sys.argv[1]
    kernel_size = int(sys.argv[2])

    img = Image.open(img_path)  # Carregar sua imagem
    closed_img = closing_image(img, kernel_size)
    closed_img.save("fechamento.jpg")  # Salvar a imagem após o fechamento
