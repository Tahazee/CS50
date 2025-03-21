import math

def main():
      f=input("fraction:")
      x=convert(f)
      y=gauge(x)
      print(y)

def convert(f):
    try:

           x,y=f.split("/")
           X,Y=int(x),int(y)
           if X<=Y and Y!=0:
                           per=math.ceil((X/Y)*100)
                           return per
           elif Y==0:
                  raise ZeroDivisionError
           else:
                  raise ValueError

    except(ValueError,ZeroDivisionError):
            raise

def gauge(per):
          if per<=1:
             return("E")
          elif 101>per>=99 :
              return("F")
          else:
               return(f"{per}%")

if __name__ == "__main__":
    main()






# import math


# def main():
#       f=input("fraction:")
#       r=convert(f)
#       print(r)

# def convert(f):
#     try:
#       x,y=f.split("/")
#       X,Y=int(x),int(y)
#       if X>Y or Y==0:
#              raise ValueError("error")
#       per=math.ceil((X/Y)*100)
#       return gauge(per)
#     except ValueError:
#           raise ValueError('error')
#     except ZeroDivisionError:
#           raise ZeroDivisionError('error')

# def gauge(per):
#       if per<=1:
#              return("E")
#       elif 101>per>=99 :
#               return("F")
#       else:
#              return(f"{per}%")


# if __name__ == "__main__":
#     main()








