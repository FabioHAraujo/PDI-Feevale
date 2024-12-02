import cv2
import numpy as np
from PIL import Image

def median_filter(img, kernel_size=3):
    """
    Aplica o filtro mediano em uma imagem.
    :param img: Imagem PIL (RGB ou escala de cinza).
    :param kernel_size: Tamanho do kernel para o filtro mediano (deve ser ímpar).
    :return: Imagem PIL resultante após a aplicação do filtro mediano.
    """
    # Converter a imagem PIL para NumPy
    img_array = np.array(img)

    # Aplicar filtro mediano
    print(f"Aplicando filtro mediano com kernel_size={kernel_size}...")
    if img_array.ndim == 3:  # Imagem colorida (RGB)
        # OpenCV requer filtragem por canal para imagens coloridas
        channels = cv2.split(img_array)
        filtered_channels = [cv2.medianBlur(channel, kernel_size) for channel in channels]
        filtered_img = cv2.merge(filtered_channels)
    else:  # Imagem em escala de cinza
        filtered_img = cv2.medianBlur(img_array, kernel_size)

    # Converter o resultado de volta para imagem PIL
    result_img = Image.fromarray(filtered_img)

    return result_img

# Exemplo de uso
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python main.py <caminho da imagem>")
        sys.exit(1)

    img_path = sys.argv[1]
    img = Image.open(img_path)  # Carregar sua imagem
    filtered_img = median_filter(img, kernel_size=3)  # Aplicar o filtro de mediana
    filtered_img.save("mediana.jpg")  # Salvar a imagem filtrada
