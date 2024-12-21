ad=50
am=0
print("Amount due:",ad)
while ad>0 :
    ui=int(input("insert coin:"))
    if ui==25 or ui==10 or ui==5:
        am+=ui
        ad=ad-ui
    if ad>0:
        print("Amount Due:",ad)
if ad<=0:
    print("Change Owed:",am-50)







