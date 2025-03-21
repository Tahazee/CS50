try:
    items={}
    count=1
    while True:
          inp=input().lower()
          if inp not in items:

                    items[inp]=1
          else:
                items[inp]+=1
except ValueError:
    pass
except EOFError:
    pass
for item in sorted(items):
        print(items.get(item),item.upper(), sep=" ")





