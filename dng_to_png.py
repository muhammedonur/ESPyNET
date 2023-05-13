# Copyright 2019-2020 by Andrey Ignatov. All Rights Reserved.

# python dng_to_png.py path_to_my_dng_file.dng

import numpy as np
import imageio.v2 as imageio
import rawpy
import sys
import os


def fix_bayer_channels(raw):
    # Training Spatial Order: Do not forget, image is up and down when processing in image libraries, this is the reason pattern look like different from dng file metadata.
    # ch_R  = raw[0::2, 0::2]
    # ch_Gb = raw[0::2, 1::2]
    # ch_Gr = raw[1::2, 0::2]
    # ch_B  = raw[1::2, 1::2]
    # R  Gb
    # Gr B
    # [Blue,Green]
    # [Green,Red]


    # Samsung RAW Image Spatial Order
    ch_Gr = np.array(raw[0::2, 0::2]) + 64
    ch_R = np.array(raw[0::2, 1::2]) + 45
    ch_B = np.array(raw[1::2, 0::2]) + 64
    ch_Gb = np.array(raw[1::2, 1::2]) + 64
    # We have to modify raw image according to model training spatial. According to internet resources;
    # it can be one of them:
    # Gb B
    # R  Gr
    # [Green,Red]
    # [Blue,Green]

    raw[0::2, 0::2] = ch_R
    raw[0::2, 1::2] = ch_Gr
    raw[1::2, 0::2] = ch_Gb
    raw[1::2, 1::2] = ch_B

    return raw


if __name__ == "__main__":

    raw_file = sys.argv[1]
    output_file = sys.argv[2]
    print("Converting file " + raw_file)

    if not os.path.isfile(raw_file):
        print("The file doesn't exist!")
        sys.exit()

    raw = rawpy.imread(raw_file)
    raw_image = raw.raw_image
    del raw


    # Use the following code to rotate the image (if needed)
    # raw_image = np.rot90(raw_image, k=2)

    raw_image = raw_image.astype(np.float32)
    #
    raw_image = fix_bayer_channels(raw_image)

    png_image = raw_image.astype(np.uint16)

    new_name = output_file + '/' + raw_file.replace(".dng", ".png")
    imageio.imwrite(new_name, png_image)
