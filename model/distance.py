# import the necessary packages

import numpy as np

import cv2


# 找到目标函数

def distance_to_camera(width):
    # convert the image to grayscale, blur it, and detect edges

    # 可以用多值取平均值减少误差

    IMAGE_PATHS = ["Picture1.jpg", "Picture2.jpg", "Picture3.jpg"]

    # 读入第一张图，通过已知距离计算相机焦距

    image = cv2.imread(IMAGE_PATHS[0])

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    edged = cv2.Canny(gray, 35, 125)

    # find the contours in the edged image and keep the largest one;

    # we'll assume that this is our piece of paper in the image

    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # 求最大面积 

    c = max(cnts, key=cv2.contourArea)

    # compute the bounding box of the of the paper region and return it

    # cv2.minAreaRect() c代表点集，返回rect[0]是最小外接矩形中心点坐标，

    # rect[1][0]是width，rect[1][1]是height，rect[2]是角度



    #纸到摄像头的距离

    KNOWN_DISTANCE = 26 * 0.39

    # A4纸的长和宽(单位:inches)

    KNOWN_WIDTH = 20.9 * 0.39

    KNOWN_HEIGHT = 14.1 * 0.39

    #获得的焦距单位是像素

    focalLength = (cv2.minAreaRect(c)[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

    #人固定的宽度40
    return (40 * focalLength) / width


