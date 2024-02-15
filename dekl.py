import json
with open('input.json', 'r') as file: list = json.load(file)

for item_raw in list: 
    item = str(item_raw)
    notInt = False
    notFloat = False
    for char in item:
        inInt = ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if char not in inInt:
            notFloat = True
        if char == ".":
            notInt = True
    if notFloat == False and notInt == True:
        itemClass = "FLOAT"
        item = float(item_raw)
    elif notFloat == False and notInt == False:
        itemClass = "INTEGER"
        item = int(item_raw)
    else: 
        itemClass = "STRING"
    print(f"{item1} is {itemClass}")