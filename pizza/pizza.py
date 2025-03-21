import csv
import sys
import tabulate
try:
    if len(sys.argv)==2:
        if sys.argv[1].endswith(".csv"):
            lst=[]
            with open(sys.argv[1],"r") as file:
                reader=csv.reader(file)
                for i in reader:
                    lst.append(i)
            w=tabulate.tabulate(lst[1:],headers=lst[0],tablefmt="grid")
            print(w)
        else:
            print("Not csv file")
            sys.exit(1)
    elif len(sys.argv)>2:
        print("too much arguments")
        sys.exit(1)
    else:
        print("too few arguments")
        sys.exit(1)
except FileNotFoundError:
    print("file not exists")
    sys.exit(1)
