import ctypes
from PIL import Image
import sys

class Main:
    def __init__(self):
        path = sys.argv[1]
        basewidth = 1341
        img = Image.open(path)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
        print("ok")

application = Main()
print("run")