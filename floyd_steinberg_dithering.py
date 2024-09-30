from PIL import Image
import math

def normalize(x):
    if x>=127:
        return 255
    else:
        return 0

image = Image.open('911.webp')
image = image.convert("L")
width, height = image.size
pixels = image.load()

for y in range(0,height-1):
    for x in range(1,width-1):
        oldpixel = pixels[x, y]
        newpixel = normalize(oldpixel)
        quant_error = oldpixel - newpixel
        pixels[x,y]= newpixel
        
        pixels[x + 1,y    ] = int(pixels[x + 1,y    ] + quant_error * 7 / 16)
        pixels[x - 1,y + 1] = int(pixels[x - 1,y + 1] + quant_error * 3 / 16)
        pixels[x    ,y + 1] = int(pixels[x    ,y + 1] + quant_error * 5 / 16)
        pixels[x + 1,y + 1] = int(pixels[x + 1,y + 1] + quant_error * 1 / 16)
        
image.save('new_image.png')
