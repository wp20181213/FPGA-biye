import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import pandas as pd
from tqdm import tqdm

# 绘制直方图函数
def grayHist(img):
    h, w = img.shape[:2]
    pixelSequence = img.reshape([h * w, ])
    numberBins = 256
    histogram, bins, patch = plt.hist(pixelSequence, numberBins,
                                      facecolor='black', histtype='bar')
    plt.xlabel("gray label")
    plt.ylabel("number of pixels")
    plt.axis([0, 255, 0, np.max(histogram)])
    plt.show()

image = cv2.imread("test.bmp", cv2.IMREAD_GRAYSCALE)

grayHist(image)