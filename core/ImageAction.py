
import os
import PIL
import defs
from PIL import Image
from os import listdir
from os.path import isfile, join


def mkdir_recursive(path):
    sub_path = os.path.dirname(path)
    if not os.path.exists(sub_path):
        mkdir_recursive(sub_path)
    if not os.path.exists(path):
        os.mkdir(path)


class ImgAction:
    def __init__(self, out_dir=defs.OUTPUT_DIR):

        if out_dir :
            if not os.path.isdir(out_dir):
                mkdir_recursive(out_dir)
            self.out_dir = out_dir

    def resizePic(self, filePath, precet=defs.PERCENT):

        try:
            img = Image.open(filePath)
            precet = float(precet)/float(100)
            wsize = int((float(img.size[0]) * float(precet)))
            hsize = int((float(img.size[1]) * float(precet)))
            img = img.resize((wsize, hsize), PIL.Image.ANTIALIAS)
            if self.out_dir:
                fileName =os.path.basename(filePath)
                filePath = os.path.join(self.out_dir, fileName)
            img.save(filePath)
        except Exception as e:
            print "error {}".format(e)

    def resizeFolder(self, folder_path):
        if not os.path.isdir(folder_path):
            print "the folder not exist "
        onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
        for f in onlyfiles :
            print "the corrent file is {}".format(f)
