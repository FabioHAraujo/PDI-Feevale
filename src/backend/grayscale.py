from PIL import Image

def grayscale(img):
    # Cria uma nova imagem em escala de cinza com as mesmas dimensões da imagem original
    result_image = Image.new("L", img.size)  # "L" para imagens em escala de cinza

    # Itera sobre cada pixel da imagem original
    width, height = img.size
    for x in range(width):
        for y in range(height):
            # Obtém os valores RGB do pixel
            r, g, b = img.getpixel((x, y))

            # Calcula o valor médio dos canais RGB
            gray_value = (r + g + b) // 3  # Média dos valores RGB

            # Define o valor do pixel na imagem resultante
            result_image.putpixel((x, y), gray_value)

    return result_image

# Exemplo de uso
if __name__ == "__main__":
    img = Image.open("sua_imagem.jpg")  # Substitua pelo caminho da sua imagem
    gray_img = grayscale(img)
    gray_img.save("imagem_gray.jpg")  # Salva a imagem em escala de cinza
