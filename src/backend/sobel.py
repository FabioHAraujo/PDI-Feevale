import numpy as np
from PIL import Image

def sobel_filter(img):
    # Converte a imagem para um array NumPy
    img_array = np.array(img)

    # Verificar se a imagem tem canais ou é em escala de cinza
    if img_array.ndim == 2:  # Imagem em escala de cinza
        height, width = img_array.shape
        channels = 1
    else:  # Imagem com múltiplos canais (RGB)
        height, width, channels = img_array.shape

    # Criar uma imagem resultante preenchida com zeros
    result_array = np.zeros_like(img_array)

    # Máscaras de Sobel
    x_mask = np.array([[1, 0, -1],
                       [2, 0, -2],
                       [1, 0, -1]])
    
    y_mask = np.array([[1, 2, 1],
                       [0, 0, 0],
                       [-1, -2, -1]])

    # Função para calcular o valor do pixel usando as máscaras de Sobel
    def compute_pixel(image, x, y):
        gradient_x = 0
        gradient_y = 0
        for lx in range(3):
            for ly in range(3):
                # Obter o valor do pixel e aplicar a máscara
                pixel_value = image[y + ly - 1, x + lx - 1]
                gradient_x += pixel_value * x_mask[lx, ly]
                gradient_y += pixel_value * y_mask[lx, ly]
        
        # Calcular a magnitude do gradiente
        value = int(np.sqrt(gradient_x ** 2 + gradient_y ** 2))
        return min(value, 255)  # Limitar o valor máximo a 255

    # Aplicar a convolução usando o filtro Sobel
    if channels == 1:  # Imagem em escala de cinza
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                new_value = compute_pixel(img_array, x, y)
                result_array[y, x] = new_value
    else:  # Imagem com múltiplos canais
        for channel in range(channels):
            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    new_value = compute_pixel(img_array[:, :, channel], x, y)
                    result_array[y, x, channel] = new_value

    # Converter o array resultante de volta para uma imagem PIL
    if channels == 1:  # Se for escala de cinza, remover o canal extra
        result_img = Image.fromarray(result_array.astype('uint8'))
    else:  # Caso contrário, manter a estrutura de múltiplos canais
        result_img = Image.fromarray(result_array.astype('uint8'), mode="RGB")
    
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
