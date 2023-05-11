# Copyright 2020 by Andrey Ignatov. All Rights Reserved.
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from PIL import Image
import imageio.v2 as imageio
import sys
import os

from model import PyNET
import utils

from load_dataset import extract_bayer_channels
IMAGE_HEIGHT, IMAGE_WIDTH = 1472, 1984

LEVEL, restore_iter, dataset_dir, use_gpu, orig_model = utils.process_test_model_args(sys.argv)
DSLR_SCALE = float(1) / (2 ** (LEVEL - 1))

# Disable gpu if specified
config = tf.ConfigProto(device_count={'GPU': 0}) if use_gpu == "false" else None

with tf.Session(config=config) as sess:

    # Placeholders for test data
    x_ = tf.placeholder(tf.float32, [1, IMAGE_HEIGHT, IMAGE_WIDTH, 4])

    # generate enhanced image
    output_l0, output_l1, output_l2, output_l3, output_l4, output_l5 =\
        PyNET(x_, instance_norm=True, instance_norm_level_1=False)

    if LEVEL == 5:
        enhanced = output_l5
    if LEVEL == 4:
        enhanced = output_l4
    if LEVEL == 3:
        enhanced = output_l3
    if LEVEL == 2:
        enhanced = output_l2
    if LEVEL == 1:
        enhanced = output_l1
    if LEVEL == 0:
        enhanced = output_l0

    # Loading pre-trained model

    saver = tf.train.Saver()

    if orig_model == "true":
        saver.restore(sess, "models/original/pynet_level_0.ckpt")
    else:
        saver.restore(sess, "models/pynet_level_" + str(LEVEL) + "_iteration_" + str(restore_iter) + ".ckpt")

    # Processing full-resolution RAW images

    test_dir = dataset_dir + "/test/huawei_full_resolution/"
    test_photos = [f for f in os.listdir(test_dir) if os.path.isfile(test_dir + f) and (test_dir + f).split('.')[-1] == "png"]
    #print(test_photos)
    #test_photos = []

    for photo in test_photos:

            print("Processing image " + photo)

            I = np.asarray(imageio.imread((test_dir + photo)))
            I = extract_bayer_channels(I)

            I = I[0:IMAGE_HEIGHT, 0:IMAGE_WIDTH, :]
            I = np.reshape(I, [1, I.shape[0], I.shape[1], 4])

            # Run inference

            enhanced_tensor = sess.run(enhanced, feed_dict={x_: I})
            enhanced_image = np.reshape(enhanced_tensor, [int(I.shape[1] * DSLR_SCALE), int(I.shape[2] * DSLR_SCALE), 3])

            # To-Do: Image is considered in its pixel but it is not  good way to normalize it. We have to know max and min value.
            enhanced_image = (255*(enhanced_image - np.min(enhanced_image))/np.ptp(enhanced_image)).astype('uint8')  
            
            # Save the results as .png images
            photo_name = photo.rsplit(".", 1)[0]
            imageio.imwrite("results/full-resolution/" + photo_name + "_level_" + str(LEVEL) + "_iteration_" + str(restore_iter) + ".png", enhanced_image)
