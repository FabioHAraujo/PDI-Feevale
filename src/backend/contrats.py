from PIL import ImageEnhance

def contrast_adjust(img, contrast):
  ajuste = ImageEnhance.Contrast(img)
  img = ajuste.enhance(contrast)
  return img