import sys
try:
    if len(sys.argv)==2:
        y=[]
        with open(sys.argv[1]) as file:
            if sys.argv[1].endswith(".py"):
                for line in file:
                    if line.isspace() or line.strip().startswith("#"):
                        continue
                    else:
                        x=line.strip()
                        y.append(x)


                print(len(y))
            else:
                sys.exit(1)

    elif len(sys.argv)<2:
        print("too few arguments")
        sys.exit(1)



    else :
        print("too much arguments")
        sys.exit(1)



except FileNotFoundError:
    print("not exsists")
    sys.exit(1)


