x=input("camelcase:")

snakecase=""
for i in x:
    if i.isupper():
         snakecase+="_"+i.lower()
         i+=i
    else:
         snakecase+=i
print(snakecase)





