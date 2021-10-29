from PIL import ImageGrab
from time import sleep

image = ImageGrab.grab()

print (image.getpixel((298,209)))
input("> ")
