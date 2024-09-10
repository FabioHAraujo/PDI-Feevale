from PIL import Image
import numpy as np

def mirror_image(img, axis):
    # Converte a imagem para um array numpy
    img_array = np.array(img)

    # Espelhamento vertical
    if axis == 'v':
        mirrored_img_array = img_array[::-1, :]
    # Espelhamento horizontal
    elif axis == 'h':
        mirrored_img_array = img_array[:, ::-1]
    else:
        raise ValueError("Eixo inválido. Use 'v' para vertical ou 'h' para horizontal.")

    # Converte o array de volta para uma imagem
    mirrored_img = Image.fromarray(mirrored_img_array)
    return mirrored_img
