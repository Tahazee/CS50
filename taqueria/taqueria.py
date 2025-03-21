


items={ "Baja Taco": 4.25, "Burrito": 7.50, "Bowl": 8.50,
        "Nachos": 11.00, "Quesadilla": 8.50,"Super Burrito": 8.50, "Super Quesadilla": 9.50,
        "Taco": 3.00, "Tortilla Salad": 8.00}


total=0
try :
    while True:

        ui=input("item:").lower().strip()
        for item in items:
            if ui==item.lower().strip():
                cost=items[item]
                total+=cost
                print(f"${total:.2f}")



except ValueError:
    pass
except EOFError:
    pass




