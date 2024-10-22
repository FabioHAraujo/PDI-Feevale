import numpy as np
from PIL import Image

def contrast_adjust(img, contrast):
    # Converta a imagem para um array NumPy
    img_array = np.array(img)

    # Aplique o ajuste de contraste
    # A multiplicação do contraste é aplicada a cada canal de cor
    new_img_array = img_array * contrast

    # Limite os valores para que fiquem dentro do intervalo [0, 255]
    new_img_array = np.clip(new_img_array, 0, 255)

    # Converta o array de volta para uma imagem PIL
    result_img = Image.fromarray(new_img_array.astype('uint8'))
    
    return result_img

# Exemplo de uso
if __name__ == "__main__":
    img = Image.open("antes.jpg")  # Carregar sua imagem
    contrast_value = 1.5  # Ajustar o valor de contraste aqui
    adjusted_img = contrast_adjust(img, contrast_value)
    adjusted_img.save("ajustado.jpg")  # Salvar a imagem ajustada
