def main():
   x=input("enter time:")
   y=convert(x)
   if 7.0<=y<=8.0:
        print("breakfast time")
   if 12.0<=y<=13.0:
        print("lunch time")
   if 18.0<=y<=19.0:
        print("dinner time")


def convert(time):
    h,m=time.split(":")
    return float(h)+float(m)/60

if __name__ == "__main__":
    main()






