from PIL import Image, ImageOps
import numpy as np


def processJump(threshold=12.5):
    img = Image.open('img.png')
    w, h = img.size

    left = w - (w*0.85)
    top = h/1.7
    right = w-(w*0.65)
    bottom = (3.7*h)/4.2

    focus_area = (left, top, right, bottom)
    img1 = img.crop(focus_area)
    img1 = ImageOps.grayscale(img1)
    img1 = img1.convert('1')
    w1, h1 = img1.size

    img2 = np.asarray(img1)
    img3 = Image.fromarray(img2[0:int(h1*0.92)][0:w1])
    w2, h2 = img3.size

    finalImage = np.asarray(img3)
    trueCount = np.count_nonzero(finalImage)
    totalCount = w2 * h2

    output = trueCount/totalCount * 100

    jump = False if output < threshold else True
    if jump:
        print(output)
    return jump

#processJump()