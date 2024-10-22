import numpy as np
from PIL import Image

# Kernel gaussiano
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]])

def gaussian_blur(img):
    # Converte a imagem para um array NumPy
    img_array = np.array(img)
    
    # Obtém as dimensões da imagem
    height, width, channels = img_array.shape
    
    # Cria uma imagem resultante preenchida com zeros (imagem negra)
    result_array = np.zeros_like(img_array)

    # Tamanho do kernel
    ksize = kernel.shape[0]
    kernel_sum = kernel.sum()

    # Função para aplicar a convolução
    for channel in range(channels):
        for x in range(width):
            for y in range(height):
                process_kernel(img_array, result_array, channel, x, y, kernel, kernel_sum)

    # Converter o array resultante de volta para uma imagem PIL
    result_img = Image.fromarray(result_array.astype('uint8'))
    return result_img

def process_kernel(img_array, result_array, channel, x, y, kernel, kernel_sum):
    sum_value = 0
    ksize = kernel.shape[0]
    
    for i in range(ksize):
        for j in range(ksize):
            # Calcula a posição do pixel no array original, limitando para evitar índice fora da faixa
            x_pos = min(max(x + (i - 1), 0), img_array.shape[1] - 1)
            y_pos = min(max(y + (j - 1), 0), img_array.shape[0] - 1)
            sum_value += img_array[y_pos, x_pos, channel] * kernel[i, j]
    
    # Normaliza o valor pela soma dos valores do kernel
    sum_value /= kernel_sum

    # Limita o valor para o intervalo permitido
    result_array[y, x, channel] = min(max(0, int(np.round(sum_value))), 255)

# Exemplo de uso
if __name__ == "__main__":
    img = Image.open("sua_imagem.jpg")  # Substitua pelo caminho da sua imagem
    blurred_img = gaussian_blur(img)
    blurred_img.save("imagem_gaussiana.jpg")  # Salva a imagem suavizada
