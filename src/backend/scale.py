from PIL import Image
import numpy as np

def scale_image(img, scale_factor):
    # Converte a imagem para RGBA para ter consistência de 4 canais
    img = img.convert("RGBA")
    img_array = np.array(img)
    height, width = img_array.shape[:2]

    # Calcula o novo tamanho
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # Cria uma nova imagem redimensionada com RGBA
    scaled_img_array = np.zeros((new_height, new_width, 4), dtype=np.uint8)

    # Faz a escala manualmente
    for y in range(new_height):
        for x in range(new_width):
            src_x = int(x / scale_factor)
            src_y = int(y / scale_factor)

            if src_x < width and src_y < height:
                scaled_img_array[y, x] = img_array[src_y, src_x]

    # Converte o array de volta para uma imagem
    scaled_img = Image.fromarray(scaled_img_array)
    return scaled_img
