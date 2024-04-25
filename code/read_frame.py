# coding=utf-8
import cv2
import numpy as np


def read_frame(image):
    f = cv2.imread(image)
    # gray processing
    f = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    # binary
    binary_f = cv2.adaptiveThreshold(~f, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -5)

    rows, cols = binary_f.shape

    scale = 20
    # recognize rows
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cols // scale, 1))
    eroded = cv2.erode(binary_f, kernel, iterations=1)
    row_line = cv2.dilate(eroded, kernel, iterations=1)
    # cv2.imshow("row", row_line)
    # cv2.waitKey(0)

    # recognize columns
    scale = 10
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows // scale))
    eroded = cv2.erode(binary_f, kernel, iterations=1)
    col_line = cv2.dilate(eroded, kernel, iterations=1)
    # cv2.imshow("column", col_line)
    # cv2.waitKey(0)

    # find cross points
    cross_point = cv2.bitwise_and(row_line, col_line)
    # cv2.imshow("point", cross_point)
    # cv2.waitKey(0)

    # table structure
    empty_f = cv2.add(row_line, col_line)

    # delete lines and show content
    content = cv2.subtract(binary_f, empty_f)
    # cv2.imshow("content", content)
    # cv2.waitKey(0)

    # determine position of cross points
    ys, xs = np.where(cross_point > 0)
    y_point_arr = []
    x_point_arr = []

    i = 0
    sort_x_point = np.sort(xs)
    for i in range(len(sort_x_point) - 1):
        if sort_x_point[i + 1] - sort_x_point[i] > 10:
            x_point_arr.append(sort_x_point[i])
            i = i + 1
    x_point_arr.append(sort_x_point[i])

    i = 0
    sort_y_point = np.sort(ys)
    for i in range(len(sort_y_point) - 1):
        if sort_y_point[i + 1] - sort_y_point[i] > 10:
            y_point_arr.append(sort_y_point[i])
            i = i + 1
    y_point_arr.append(sort_y_point[i])

    # Create answer matrix
    ans = np.zeros((len(y_point_arr)-2, len(x_point_arr)-2))
    for i in range(1, len(x_point_arr)-1):
        for j in range(1, len(y_point_arr)-1):
            x1 = x_point_arr[i]
            x2 = x_point_arr[i+1]
            y1 = y_point_arr[j]
            y2 = y_point_arr[j+1]
            box = content[y1:y2, x1:x2]
            if np.max(box) > 0:
                ans[j-1][i-1] = 1
    return ans


if __name__ == "__main__":
    filename = 'test.png'
    ans_matrix = read_frame(filename)
    print(ans_matrix)




