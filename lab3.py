import cv2
import numpy as np

#1
def Cam():

    size = 5
    sigma = 1.0  # отклонение
    center = size // 2
    kernel = np.zeros((size, size))

    for x in range(size):
        for y in range(size):

            centrX = center
            centrY = center

            # Гауссовская функция
            kernel[x, y] = (1 / (2 * np.pi * sigma ** 2)) * np.exp(
                -((x - centrX) ** 2 + (y - centrY) ** 2) / (2 * sigma ** 2)
            )

    print("Матрица свертки:")
    print(kernel)

Cam()

#2

# def Cam():
#
#     size = 5  #
#     sigma = 1.0  #отклонение
#     center = size // 2
#     kernel = np.zeros((size, size))
#
#     for x in range(size):
#         for y in range(size):
#
#             centrX = center
#             centrY = center
#
#             # Гауссовская функция
#             kernel[x, y] = (1 / (2 * np.pi * sigma ** 2)) * np.exp(
#                 -((x - centrX) ** 2 + (y - centrY) ** 2) / (2 * sigma ** 2)
#             )
#
#         # Нормализация матрицы, чтобы сумма всех элементов была равна 1
#     kernel_sum = np.sum(kernel)
#     if kernel_sum != 0:
#         kernel /= kernel_sum
#     print("Матрица свертки:")
#     print(kernel)
#
# Cam()

#3

# def Cam():
#
#     size = 5
#     sigma = 1.0  # отклонение
#     center = size // 2
#     kernel = np.zeros((size, size))
#
#     for x in range(size):
#         for y in range(size):
#
#             centrX = center
#             centrY = center
#
#             # Гауссовская функция
#             kernel[x, y] = (1 / (2 * np.pi * sigma ** 2)) * np.exp(
#                 -((x - centrX) ** 2 + (y - centrY) ** 2) / (2 * sigma ** 2)
#             )
#
#
#     kernel_sum = np.sum(kernel)
#     if kernel_sum != 0:
#         kernel /= kernel_sum
#     print("Матрица свертки:")
#     print(kernel)
#
#     image = cv2.imread('D:/draw/boom.png', cv2.THRESH_BINARY)
#     image2 = cv2.filter2D(image, -1, kernel)
#
#     cv2.namedWindow('Normal', cv2.WINDOW_KEEPRATIO)
#     cv2.imshow('Normal', image)
#     cv2.namedWindow('Filter', cv2.WINDOW_KEEPRATIO)
#     cv2.imshow('Filter', image2)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#
# Cam()

#4
# def GAIS(size,sigma):
#     center = size // 2
#     kernel = np.zeros((size, size))
#     for x in range(size):
#         for y in range(size):
#
#             centrX = center
#             centrY = center
#
#             # Гауссовская функция
#             kernel[x, y] = (1 / (2 * np.pi * sigma ** 2)) * np.exp(
#                 -((x - centrX) ** 2 + (y - centrY) ** 2) / (2 * sigma ** 2)
#             )
#
#     kernel /= np.sum(kernel)
#
#     return kernel
#
# def Cam():
#
#     size = 7
#     size2 = 3
#     sigma2 = 0.5
#     sigma = 1.0  # отклонение
#
#     image = cv2.imread('D:/draw/boom.png', cv2.THRESH_BINARY)
#     kernel = GAIS(size,sigma)
#     kernel2 = GAIS(size2, sigma2)
#
#     image = cv2.filter2D(image, -1, kernel)
#     image2 = cv2.filter2D(image, -1, kernel2)
#
#     cv2.namedWindow('Matrix 7x7', cv2.WINDOW_KEEPRATIO)
#     cv2.imshow('Matrix 7x7', image)
#     cv2.namedWindow('Matrix 3x3', cv2.WINDOW_KEEPRATIO)
#     cv2.imshow('Matrix 3x3', image2)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#
# Cam()


#5

# def Cam():
#
#     size = 7
#     sigma = 1.0  # отклонение
#
#     image = cv2.imread('D:/draw/boom.png', cv2.THRESH_BINARY)
#
#     image = cv2.GaussianBlur(image, (size, size), sigma)
#     cv2.namedWindow('Gausse', cv2.WINDOW_KEEPRATIO)
#     cv2.imshow('Gausse', filtered_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#
# Cam()