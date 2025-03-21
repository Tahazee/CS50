import csv
import sys

try:
    if len(sys.argv)==3:
      data=[]
      with open(sys.argv[1],"r") as file:
            reader=csv.DictReader(file)
            for i in reader:
                  f,l=i["name"].split(",")
                  data.append({"first":l.lstrip(),"last":f,"house":i["house"]})
      with open(sys.argv[2],"w") as file2:
            writer=csv.DictWriter(file2,fieldnames=["firstname","lastname","house"])
            writer.writerow({"firstname":"first","lastname":"last","house":"house"})
            for i in data:
                  writer.writerow({"firstname":i["first"],"lastname":i["last"],"house":i["house"]})



    elif len(sys.argv)>3:
           sys.exit("too much arguments")
    else:
            sys.exit("too few arguments")


except FileNotFoundError:
      sys.exit("not readable")



