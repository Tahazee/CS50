import random

while True:
    n=input("level: ")
    if n.isdigit() and int(n)>0:
        x=int(n)
        break


num=random.randint(1,x)
while True:
    while True:
           g=input("Guess: ")
           if g.isdigit() and int(g)>0:
                    y=int(g)
                    break

    if int(g)>num:
            print("Too large!")
    elif int(g)<num:
            print("Too small!")
    else:
              print("Just right!")
              break







# if num==int(g):

#     print("Just right!")

# else:
#      while True:
#           if int(g)>num:
#             print("Too large!")
#             g=input("Guess: ")
#           elif int(g)<num:
#             print("Too small!")
#             g=input("Guess: ")
#           else:
#               print("Just right!")
#               break




















