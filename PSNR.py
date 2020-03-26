import tensorflow as tf
import os

path_DeHaze = r'F:\dehazeresult\sequence\AOD-result'

path_GT = r'F:\dehazeresult\result'

HazeFileList = os.listdir(path_DeHaze)

GTFileList = os.listdir(path_GT)

def psnr(img1,img2):
    return tf.image.psnr(img1,img2,max_val=255)

def ssim(img1,img2):
    return tf.image.ssim(img1,img2,max_val=255)

psnr_total = 0
ssim_total = 0

# for i in range(5271):
#
#     num = i // 21
#
#     GT_path = os.path.join(r'F:\dehazeresult\result',GTFileList[num])
#
#     print(GT_path)
#
#     haze_path = os.path.join(path_DeHaze,HazeFileList[i])
#
#     print(haze_path)
#
#     haze_image = tf.image.decode_image(tf.read_file(haze_path))
#
#     GT_image = tf.image.decode_image(tf.read_file(GT_path))
#
#     with tf.Session() as sess:
#         sess.run(tf.global_variables_initializer())
#         y = sess.run(psnr(GT_image,haze_image))
#         ssim_y = sess.run(ssim(GT_image,haze_image))
#         print(ssim_y)
#         print(y)
#         psnr_total += y
#         ssim_total += ssim_y

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(5271):
        num = i // 21

        GT_path = os.path.join(r'F:\dehazeresult\result', GTFileList[num])

        print(GT_path)

        haze_path = os.path.join(path_DeHaze, HazeFileList[i])

        print(haze_path)

        haze_image = tf.image.decode_image(tf.read_file(haze_path))

        GT_image = tf.image.decode_image(tf.read_file(GT_path))

        y = sess.run(psnr(GT_image, haze_image))
        ssim_y = sess.run(ssim(GT_image, haze_image))
        print(ssim_y)
        print(y)
        psnr_total += y
        ssim_total += ssim_y

print("5271张图片的PSNR为： ",psnr_total)
print("5271张图片的SSIM为： ",ssim_total)