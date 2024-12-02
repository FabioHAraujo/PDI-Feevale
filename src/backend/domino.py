import cv2
import numpy as np

def apply_pipeline(img):
    """
    Aplica o pipeline completo de pré-processamento:
    1. Filtro mediano
    2. Escala de cinza
    3. Sobel (detecção de bordas)
    :param img: Imagem PIL original.
    :return: Imagem NumPy processada (após Sobel).
    """
    # Converter para NumPy
    img_np = np.array(img)

    # Aplicar filtro mediano para reduzir ruído
    print("Aplicando filtro mediano...")
    img_np = cv2.medianBlur(img_np, ksize=3)

    # Converter para escala de cinza
    print("Convertendo para escala de cinza...")
    if img_np.ndim == 3:  # Caso seja colorida
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    # Aplicar Sobel para detecção de bordas
    print("Aplicando filtro Sobel...")
    sobel_x = cv2.Sobel(img_np, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img_np, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)

    # Normalizar para valores de 0 a 255
    sobel_result = np.uint8(np.clip(sobel_combined, 0, 255))

    return sobel_result


def detect_circles(img):
    """
    Detecta círculos em uma imagem e retorna a contagem de círculos.
    :param img: Imagem NumPy processada.
    :return: Número total de círculos detectados.
    """
    # Aplicar threshold para binarizar a imagem
    _, binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    print("Imagem binarizada.")

    # Encontrar contornos na imagem
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f"Total de contornos encontrados: {len(contours)}")

    # Contar círculos
    circles = []
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        if perimeter == 0:
            continue
        circularity = 4 * np.pi * (area / (perimeter ** 2))
        if 0.7 <= circularity <= 1.3:  # Aproximadamente circular
            circles.append(contour)

    print(f"Número de círculos detectados: {len(circles)}")
    return len(circles)


def process_domino(img):
    """
    Processa a imagem do dominó, conta os pontos em cada lado e retorna os resultados.
    :param img: Imagem PIL original.
    :return: Dicionário com contagem de pontos e imagem anotada (opcional).
    """
    try:
        if img is None:
            raise ValueError("A imagem de entrada está como None.")

        # Aplicar pipeline de pré-processamento
        processed_img = apply_pipeline(img)

        print(f"Imagem processada com shape: {processed_img.shape}")

        # Dividir a imagem em dois lados
        height, width = processed_img.shape
        if height >= width:  # Divisão horizontal
            half_height = height // 2
            lado_1 = processed_img[:half_height, :]
            lado_2 = processed_img[half_height:, :]
        else:  # Divisão vertical
            half_width = width // 2
            lado_1 = processed_img[:, :half_width]
            lado_2 = processed_img[:, half_width:]

        # Detectar círculos em cada lado
        pontos_lado_1 = detect_circles(lado_1)
        pontos_lado_2 = detect_circles(lado_2)

        # Retornar os resultados como dicionário
        return {
            "pontos_lado_1": pontos_lado_1,
            "pontos_lado_2": pontos_lado_2,
        }

    except Exception as e:
        print(f"Erro no processamento do dominó: {e}")
        raise