# coding=utf-8
import cv2
import numpy as np

f = cv2.imread('test.png')
f = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
binary_f = cv2.adaptiveThreshold(f, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 35, -5)

rows, cols = binary_f.shape

scale = 40

# recognize rows
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cols // scale, 1))
dilated_col = cv2.dilate(binary_f, kernel, iterations=1)
# recognize columns
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows // scale))
dilated_row = cv2.dilate(binary_f, kernel, iterations=1)

empty_f = cv2.bitwise_and(dilated_col, dilated_row)
cv2.imshow("empty", empty_f)
cv2.waitKey(0)

merge = cv2.add(dilated_col, dilated_row)
cv2.imshow("point", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()

merge2 = cv2.subtract(empty_f, merge)

ys, xs = np.where(empty_f == 0)

y_point_arr = []
x_point_arr = []

i = 0
sort_x_point = np.sort(xs)
for i in range(len(sort_x_point) - 1):
    if sort_x_point[i + 1] - sort_x_point[i] > 10:
        x_point_arr.append(sort_x_point[i])
    i = i + 1
x_point_arr.append(sort_x_point[i])
print(x_point_arr)

i = 0
sort_y_point = np.sort(ys)
for i in range(len(sort_y_point) - 1):
    if sort_y_point[i + 1] - sort_y_point[i] > 10:
        y_point_arr.append(sort_y_point[i])
    i = i + 1
y_point_arr.append(sort_y_point[i])
print(y_point_arr)

