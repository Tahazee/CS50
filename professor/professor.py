import random

def get_level():
     lvl=["1","2","3"]
     while True:
         inp=input("level: ")
         if inp in lvl:
             return int(inp)




def generate_integer(level):

    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(100, 999), random.randint(100, 999)

def main():
     scr=0
     level=get_level()
     for _ in range(10):
        x,y=generate_integer(level)
        sum=x+y
        z=input(f"{x} + {y} = ")
        if z.isdigit() and sum==int(z):
            scr+=1
        else:
            for i in range(2):
                print("EEE")
                z=input(f"{x} + {y} = ")
                if z.isdigit() and sum==int(z):
                    scr+=1
                    break
            else:
                    print("EEE")
                    print(f"{x} + {y}= {sum}")
     print("Score: ",scr)
if __name__ == "__main__":
    main()




