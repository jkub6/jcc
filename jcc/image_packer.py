"""
Transform images into custom glyph format.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""


import os
import PIL
from PIL import Image
import numpy


def pack(folder_path, outfile_path, label_ascii=False):
    """Pack folder of images into glyph format."""
    output = ""

    # image size
    M = 64
    N = 64

    filenames = os.listdir(folder_path)
    for filename in filenames:
        if os.path.isfile(os.path.join(folder_path, filename)):
            if (filename.endswith(".jpg") or filename.endswith(".png") or
               filename.endswith(".bmp")):
                img = PIL.Image.open(os.path.join(folder_path, filename))
                img_pixel_array = numpy.asarray(img)

                tiles = []
                count = 0
                for x in range(0, img_pixel_array.shape[1], N):
                    for y in range(0, img_pixel_array.shape[0], M):
                        tiles.append(img_pixel_array[x:x+M, y:y+N])
                        count += 1

                for i, pixel_array in enumerate(tiles):
                    if label_ascii:
                        if i == 0:
                            char = "NULL"
                        else:
                            char = chr(i)
                        output += "//ASCII symbol: '{}'\n".format(char)
                    else:
                        output += "//" + filename + "_" + str(i) + "\n"
                    for i, row in enumerate(pixel_array):
                        line = []
                        for pixel in row:
                            if list(pixel) == [255, 255, 255]:
                                line.append("0")
                            else:
                                line.append("1")
                        output += "7'd{:02}: value = ".format(i)
                        output += "".join(line) + ";\n"
                    output += "\n\n\n"
    out_file = open(outfile_path, "w")
    out_file.write(output)
    out_file.close()
