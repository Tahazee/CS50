try:
    ad=[]
    n=0
    while True:
           inp=input("")
           ad.append(inp)
           def comma():
            e=""
            if len(ad)>1:
                  e=", ".join(ad[:-1])
            else:
                  e="".join(ad)
            return e




except EOFError:
      pass
x="".join(ad[-1:])
if len(ad)>2:
               print(f"Adieu, adieu, to {comma()}, and {x}")
elif len(ad)==2:
        print(f"Adieu, adieu, to {comma()} and {x}")
else:
               print(f"Adieu, adieu, to {comma()} ")






