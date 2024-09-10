from PIL import Image
import numpy as np

def translate_image(img, dx, dy):
    img_array = np.array(img)  # Converte a imagem para um array numpy
    h, w, c = img_array.shape  # Obtém as dimensões da imagem (altura, largura, canais)

    # Cria uma imagem de saída com o mesmo tamanho e tipo de dados
    translated_img_array = np.zeros_like(img_array)

    # Calcula a translação e copia os pixels
    for y in range(h):
        for x in range(w):
            new_x = int(x + dx)  # Garante que new_x seja um inteiro
            new_y = int(y - dy)  # Garante que new_y seja um inteiro

            # Garante que os novos índices estejam dentro dos limites
            if 0 <= new_x < w and 0 <= new_y < h:
                translated_img_array[new_y, new_x] = img_array[y, x]

    # Converte o array de volta para uma imagem
    translated_img = Image.fromarray(translated_img_array)
    return translated_img
