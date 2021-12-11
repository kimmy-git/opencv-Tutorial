import cv2 as cv
import sys

img = cv.imread('.\\tetris_blocks.png')

if img is None:
    print('Image load failed')
    sys.exit()

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, dst = cv.threshold(img_gray, 225, 250, cv.THRESH_BINARY_INV)

mask = dst.copy()
# mask 지정을 해줘야함
output = cv.bitwise_and(img, img, mask=mask)

cv.imshow('image', img)
cv.imshow('img_gray', img_gray)
cv.imshow('thresh', dst)
cv.imshow('bitwise', output)
cv.waitKey()