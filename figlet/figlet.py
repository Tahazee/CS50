import sys
import random
from pyfiglet import Figlet
fi=Figlet()
f=fi.getFonts()
if len(sys.argv)==1:
    inp=input("Input:")
    y=fi.setFont(font=random.choice(f))
    print(fi.renderText(inp))

if len(sys.argv)==3:
    if sys.argv[1]=="-f" or sys.argv[1]=="-font":
        if sys.argv[2] in f:
                inp=input("Input:")
                fi.setFont(font=sys.argv[2])
                print(fi.renderText(inp))
        else:
             print("Invalid usage")
             sys.exit(1)
    else:
             print("Invalid usage")
             sys.exit(1)
else:
             print("Invalid usage")
             sys.exit(1)

