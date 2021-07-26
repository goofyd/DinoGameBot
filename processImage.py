from PIL import Image, ImageOps
import numpy as np


def processJump(threshold=12.5):
    img = Image.open('img.png')
    w, h = img.size

    left = w - (w*0.79)
    top = h/2
    right = w-(w*0.67)
    bottom = (3.2*h)/5

    focus_area = (left, top, right, bottom)
    img1 = img.crop(focus_area)
    img1 = ImageOps.grayscale(img1)
    img1 = img1.convert('1')
    w1, h1 = img1.size

    img2 = np.asarray(img1)
    img3 = Image.fromarray(img2[0:int(h1*0.92)][0:w1])
    w2, h2 = img3.size
    img3.save('out.png')

    finalImage = np.asarray(img3)
    trueCount = np.count_nonzero(finalImage)
    totalCount = w2 * h2

    output = trueCount/totalCount * 100
    print(None)
    jump = False if output < threshold else True
    if jump:
        print('Found Obstacle!')
    return jump