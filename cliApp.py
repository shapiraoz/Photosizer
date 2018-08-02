import os
import core.defs as defs
from argparse import ArgumentParser
import core.ImageAction as imgActions


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg  # return an open file handle


parser = ArgumentParser(description="pictures manipulations")
parser.add_argument("-f", dest="filename", required=False,
                    help="picture file", metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))

parser.add_argument("-o", dest="outdir", required=False)
parser.add_argument("-p", dest="precent", required=False)
parser.add_argument("-d", dest="resizeDir", required=False)


def main():
    args = parser.parse_args()
    out_dir = args.outdir if args.outdir else defs.OUTPUT_DIR
    percent = args.precent if args.precent else defs.PERCENT

    ims = imgActions.ImgAction(out_dir)

    if args.filename:
        ims.resizePic(args.filename, percent)

    if args.resizeDir:
        ims.resizeFolder(args.resizeDir)






if __name__== "__main__":
    main()



