from os.path import splitext
import sys
from PIL import Image,ImageOps
f1= splitext(sys.argv[1])
f2=splitext(sys.argv[2])


def check():
      ext=[".jpg",".png",".jpeg"]
      if f1[1] in ext or f2[1] in ext:
            if f1[1].lower()==f2[1].lower():
                  return True
            else:
                   sys.exit("not possible")
      else:
            sys.exit("invalid")


try:
    if len(sys.argv)==3:
                     check()
                     bg=Image.open(sys.argv[1])
                     shirt=Image.open("shirt.png")
                     size=shirt.size
                     newimg=ImageOps.fit(bg,size)
                     newimg.paste(shirt,shirt)
                     newimg.save(sys.argv[2])



    elif len(sys.argv)>3:
           sys.exit("too much arguments")
    else:
            sys.exit("too few arguments")


except FileNotFoundError:
      sys.exit("not readable")
