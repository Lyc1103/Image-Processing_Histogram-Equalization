# Reference : https://iter01.com/519791.html
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_name = input(
    "Please enter the Image file name that you want to improve contracts : ")

# Original color image
img_color = cv2.imread(img_name)
cv2.imwrite('ColorImage_' + img_name + '.jpg', img_color)
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr_color = cv2.calcHist([img_color], [i], None, [256], [0, 256])
    plt.plot(histr_color, color=col)
    plt.xlim([0, 256])
plt.title('Color image without Histogram-Equalization')
plt.show()

# Original gray image
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imwrite('GrayImage_' + img_name + '.jpg', img_gray)
histr_gray = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.xlim([0, 256])
plt.hist(img_gray.ravel(), 256, [0, 256])
plt.title('Gray image without Histogram-Equalization')
plt.show()

# Histogram Equalization of gray image
equ_gray = cv2.equalizeHist(img_gray)
cv2.imwrite('HistogramEqualizationOfGrayImage_' + img_name + '.jpg', equ_gray)
equ_histr_gray = cv2.calcHist([equ_gray], [0], None, [256], [0, 256])
plt.xlim([0, 256])
plt.hist(equ_gray.ravel(), 256, [0, 256])
plt.title('Gray image with Histogram-Equalization')
plt.show()

# Histogram Equalization of color image
(b, g, r) = cv2.split(img_color)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
equ_color = cv2.merge((bH, gH, rH))
cv2.imwrite('HistogramEqualizationOfColorImage_' +
            img_name + '.jpg', equ_color)
for i, col in enumerate(color):
    equ_histr_color = cv2.calcHist([equ_color], [i], None, [256], [0, 256])
    plt.plot(equ_histr_color, color=col)
    plt.xlim([0, 256])
plt.title('Color image with Histogram-Equalization')
plt.show()

cv2.imshow("Original Color Image", img_color)
cv2.imshow("Original Gray Image", img_gray)
cv2.imshow("Histogram Equalization Of Gray Image", equ_gray)
cv2.imshow("Histogram Equalization Of Color Image", equ_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
