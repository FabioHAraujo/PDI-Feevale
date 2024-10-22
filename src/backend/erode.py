import numpy as np
from PIL import Image

def erode_image(img, kernel_size):
    # Converte a imagem para um array NumPy
    img_array = np.array(img)

    # Obtenha as dimensões da imagem
    height, width, channels = img_array.shape

    # Crie uma imagem resultante preenchida com zeros (imagem negra)
    result_array = np.zeros_like(img_array)

    # Calcule o raio do kernel
    radius = kernel_size // 2

    # Função para obter o menor valor entre os vizinhos
    def compute_center(neighbours):
        return np.min(neighbours)

    # Convolução para erosão
    for channel in range(channels):
        for x in range(radius, width - radius):
            for y in range(radius, height - radius):
                neighbours = []
                # Coletar os vizinhos de acordo com o tamanho do kernel
                for lx in range(-radius, radius + 1):
                    for ly in range(-radius, radius + 1):
                        # Obter valores dos vizinhos
                        neighbours.append(img_array[y + ly, x + lx, channel])
                
                # Calcular o novo valor
                new_value = compute_center(neighbours)
                result_array[y, x, channel] = new_value

    # Converter o array resultante de volta para uma imagem PIL
    result_img = Image.fromarray(result_array.astype('uint8'))
    return result_img

# Exemplo de uso
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Uso: python main.py <caminho da imagem> <tamanho do kernel>")
        sys.exit(1)

    img_path = sys.argv[1]
    kernel_size = int(sys.argv[2])

    img = Image.open(img_path)  # Carregar sua imagem
    eroded_img = erode_image(img, kernel_size)
    eroded_img.save("erodido.jpg")  # Salvar a imagem erodida
