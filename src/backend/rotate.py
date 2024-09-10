from PIL import Image
import numpy as np
import math

def rotate_image(img, angle):
    img = img.convert("RGBA")
    img_array = np.array(img)
    height, width = img_array.shape[:2]

    # Calcula o centro da imagem original
    cx, cy = width // 2, height // 2

    # Converte o ângulo para radianos
    rad = math.radians(angle)

    # Calcula o novo tamanho necessário para a imagem rotacionada
    cos_rad = abs(math.cos(rad))
    sin_rad = abs(math.sin(rad))
    new_width = int(width * cos_rad + height * sin_rad)
    new_height = int(height * cos_rad + width * sin_rad)

    # Cria uma nova imagem rotacionada com fundo transparente
    rotated_img_array = np.zeros((new_height, new_width, 4), dtype=np.uint8)
    new_cx, new_cy = new_width // 2, new_height // 2

    # Faz a rotação manualmente usando interpolação inversa
    for y in range(new_height):
        for x in range(new_width):
            # Calcula a nova posição invertida
            src_x = int((x - new_cx) * math.cos(-rad) - (y - new_cy) * math.sin(-rad) + cx)
            src_y = int((x - new_cx) * math.sin(-rad) + (y - new_cy) * math.cos(-rad) + cy)

            # Garantir que a posição calculada está dentro dos limites da imagem original
            if 0 <= src_x < width and 0 <= src_y < height:
                rotated_img_array[y, x] = img_array[src_y, src_x]
            else:
                # Defina o valor do pixel para transparente se fora dos limites
                rotated_img_array[y, x] = [0, 0, 0, 0]

    # Converte o array de volta para uma imagem
    rotated_img = Image.fromarray(rotated_img_array, 'RGBA')
    return rotated_img
