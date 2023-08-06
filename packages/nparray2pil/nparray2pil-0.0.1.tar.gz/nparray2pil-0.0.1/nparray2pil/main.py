from PIL import Image
import numpy as np
import cv2

#opencv-python
#PIL
#numpy


def convert(myarray: np.array) -> Image:

    return Image.fromarray(cv2.cvtColor(myarray, cv2.COLOR_BGR2RGB))



