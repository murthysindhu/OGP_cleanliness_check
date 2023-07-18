import numpy as np
from PIL import Image #, ImageOps
import cv2 as cv
# import matplotlib.pyplot as plt


def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def getGrayScale(img):
    grayIm = (rgb2gray(img)/255)
    c,b,= np.histogram((grayIm).flatten(), range=(0., 1), bins=25)
    return np.round( 100*np.sum(c[np.where(b<0.4)[0]])/np.sum(c), 3)

def getKmeanClus(img, K=3, epsilon=1.0):
    Z = np.float32(img.reshape((-1,3)))
    ## define criteria, number of clusters(K) and apply kmeans()
    ## maximum number of iteration; maximum value of epsilon
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, epsilon)
    ret,label,center=cv.kmeans(Z, K=K, bestLabels=None, criteria=criteria, attempts=10, flags=cv.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = (center[label.flatten()]).reshape((img.shape))
    return rgb2gray(res)

def getClusGrayScale(img):
    clusIm = getKmeanClus(img)
    color, count = np.unique(clusIm.flatten(), return_counts=True)
    return np.round( 100*count[0]/np.sum(count) ,3)


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', default="image.png")
parser.add_argument('-m', '--method', default="2")
parser.add_argument('-s', '--score', default="0.5")
args = parser.parse_args()

img = np.array(Image.open(args.file))
if args.method == '1':
    print("Checking image with by grayscale distribution ...")
    score = getGrayScale(img)
    if score > float(args.score):
        print("Score =", str(score), '%')
        print("Check for contaminants!!")
    else:
        print("Sample clean")
elif args.method == '2':
    print("Checking image with k-means clustering ...")
    score = getClusGrayScale(img)
    if score > float(args.score):
        print("Score =", str(score), '%')
        print("Check for contaminants!!")
    else:
        print("Sample clean")
