
from PIL import Image, ImageOps 

def grayscale(img):
    grayapplied = ImageOps.grayscale(img)
    return grayapplied
