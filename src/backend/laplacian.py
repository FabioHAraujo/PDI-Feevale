import numpy as np
from PIL import Image

def laplacian_filter(img):
    # Converte a imagem para um array NumPy
    img_array = np.array(img)

    # Obtenha as dimensões da imagem
    height, width, channels = img_array.shape

    # Crie uma imagem resultante preenchida com zeros (imagem negra)
    result_array = np.zeros_like(img_array)

    # Máscara de Laplaciano
    laplacian_mask = np.array([[0, -1, 0],
                                [-1, 4, -1],
                                [0, -1, 0]])

    # Função para calcular o valor do pixel usando a máscara de Laplaciano
    def compute_pixel(image, x, y):
        gradient_value = 0
        for lx in range(3):
            for ly in range(3):
                # Obter o valor do pixel e aplicar a máscara
                pixel_value = image[y + ly - 1, x + lx - 1]
                gradient_value += pixel_value * laplacian_mask[lx, ly]
        
        # Limitar o valor máximo a 255
        return min(max(int(gradient_value), 0), 255)

    # Aplicar a convolução usando o filtro Laplaciano
    for channel in range(channels):
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                new_value = compute_pixel(img_array[:, :, channel], x, y)
                result_array[y, x, channel] = new_value

    # Converter o array resultante de volta para uma imagem PIL
    result_img = Image.fromarray(result_array.astype('uint8'))
    return result_img

# Exemplo de uso
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python main.py <caminho da imagem>")
        sys.exit(1)

    img_path = sys.argv[1]
    img = Image.open(img_path)  # Carregar sua imagem
    laplacian_img = laplacian_filter(img)
    laplacian_img.save("laplacian.jpg")  # Salvar a imagem resultante
