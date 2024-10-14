from PIL import ImageEnhance

def bright_adjust(img, bright):
    ajuste = ImageEnhance.Brightness(img)
    img = ajuste.enhance(bright)
    return img
