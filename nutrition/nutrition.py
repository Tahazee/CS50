inp=input("enter:").lower()

fruits={ "Apple":"130","Banana":"110","Strawberries":"","Avocado":"50","Cantaloupe":"50",
        "Grapefruit":"60",
        "Grapes":"90",
        "Honeydew Melonz":"50","Kiwifruit":"90","lemon":"15",
        "lime":"20","orange":"80","Peach":"60","Pear":"100","Nectarine":"60","pineapple":"50",
        "plums":"70",
        "Sweet Cherries":"100","Tangerine":"50","Watermelon":"80"
}
for fruit in fruits:
    if fruit.lower()==inp:
        print(fruits[fruit])

