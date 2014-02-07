from PIL import Image as I
import numpy as np


def asciify(img,width=80,invert=False,vert_scale=False):
    tmp = img.convert('L')
    X,Y = tmp.size
    factor = float(width)/X
    if vert_scale:
        vert_scale = 0.75
    else:
        vert_scale = 1.0
    tmp = tmp.resize((int(X*factor),int(Y*factor*vert_scale)))
    data = np.array(tmp)
    buf = ""
    for x in xrange(len(data)):
        for y in xrange(len(data[x])):
            buf += ascii_hash(data[x][y],invert)
        buf += "\n"
    return buf

def ascii_hash(n,invert=False):
    char_map = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    if invert:
        char_map = char_map[::-1]
    index = int((float(n)/255.)*(len(char_map)-1))
    return char_map[index]



if __name__ == '__main__':
    import sys
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-w","--width",dest="width",default=80)
    parser.add_option("-i","--invert",action="store_true",dest="invert",default=False)
    parser.add_option("-s","--no-vertical-scale",action="store_false",dest="vert_scale",default=True)
    opts,args = parser.parse_args()
    if len(args) <= 0:
        print "No image provided"
        sys.exit(1)
    img = I.open(args[0])
    print asciify(img,opts.width,opts.invert,opts.vert_scale)

