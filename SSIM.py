import numpy as np
import cv2 as cv
import math
import os

path_DeHaze = r'F:\retest\yuantu\GT'

path_GT = r'F:\retest\yuantu\GT-GCA'

HazeFileList = os.listdir(path_DeHaze)

GTFileList = os.listdir(path_GT)

psnr_total = 0
ssim_total = 0

def psnr(img1, img2):
    mse = np.mean((img1 / 255. - img2 / 255.) ** 2)

    if mse < 1.0e-10:
        return 100

    PIXEL_MAX = 1

    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))






def ssim(img1, img2):
    C1 = (0.01 * 255)**2
    C2 = (0.03 * 255)**2

    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    kernel = cv.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.transpose())

    mu1 = cv.filter2D(img1, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv.filter2D(img2, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv.filter2D(img1**2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv.filter2D(img2**2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv.filter2D(img1 * img2, -1, window)[5:-5, 5:-5] - mu1_mu2

    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                            (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()


def calc_ssim(img1, img2):
    '''calculate SSIM
    the same outputs as MATLAB's
    img1, img2: [0, 255]
    '''
    if not img1.shape == img2.shape:
        raise ValueError('Input images must have the same dimensions.')
    if img1.ndim == 2:
        return ssim(img1, img2)
    elif img1.ndim == 3:
        if img1.shape[2] == 3:
            ssims = []
            for i in range(3):
                ssims.append(ssim(img1, img2))
            return np.array(ssims).mean()
        elif img1.shape[2] == 1:
            return ssim(np.squeeze(img1), np.squeeze(img2))
    else:
        raise ValueError('Wrong input image dimensions.')






for i in range(3):
    num = i // 21

    GT_path = os.path.join(path_GT, GTFileList[i])

    print(GT_path)

    haze_path = os.path.join(path_DeHaze, HazeFileList[i])

    print(haze_path)

    haze_image = cv.imread(haze_path)

    GT_image = cv.imread(GT_path)

    y = psnr(GT_image,haze_image)
    ssim_y = calc_ssim(haze_image,GT_image)
    print(ssim_y)
    print(y)
    psnr_total += y
    ssim_total += ssim_y

print("4张图片的PSNR为： ",psnr_total)
print("4张图片的平均PSNR为： ",psnr_total/3)
print("4张图片的SSIM为： ",ssim_total)
print("4张图片的平均SSIM为： ",ssim_total/3)