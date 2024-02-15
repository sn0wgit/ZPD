import json
with open('input.json', 'r') as file: list = json.load(file)

for item_raw in list: 
    item = str(item_raw)
    notInt = False
    notFloat = False
    for i in ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        if item.find(i) != -1:
            if item.find(".") != -1:
                try:
                    item, itemClass = float(item), "FLOAT"
                    break; break
                except: break; break
            else:
                try:
                    item, itemClass = int(item), "INTEGER"
                    break; break
                except: break; break
        else:
            try: item, itemClass = str(item), "STRING"
            except: pass
    print(f"{item} is {itemClass}")
    if itemClass == "STRING":
        integ = 0
        for letter in item:
            if letter.upper() in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                integ += int(letter)
            elif letter.upper() in ["A","Ā","B","C","Č","D","E","Ē","F","G","Ģ","H","I","Ī","J","K","Ķ","L","Ļ","M","N","Ņ","O","P","Q","R","S","Š","T","U","Ū","V","W","X","Y","Z","Ž"]:
                points = 0
                while letter.upper() != ["A","Ā","B","C","Č","D","E","Ē","F","G","Ģ","H","I","Ī","J","K","Ķ","L","Ļ","M","N","Ņ","O","P","Q","R","S","Š","T","U","Ū","V","W","X","Y","Z","Ž"][points]:
                    points += 1
                points += 1
                integ += points
            else: pass
        print(integ)
    elif itemClass == "FLOAT":
        integ = int(str(item).replace(".", ""))
        print(integ)
    else:
        integ = item
        print(integ)
    decrementBase = 100000
    while decrementBase > 0:
        if   integ < 0:
            integ = abs(integ)
        elif integ in range(0, 5):
            if   integ == 0: integ = 1
            elif integ == 1: integ = 11
            elif integ == 2: integ = 121
            elif integ == 3: integ = 1331
            elif integ == 4: integ = 14641
            elif integ == 5: integ = 15101051
        elif integ in range(6, 25):
            a, b = 1, 1
            for _ in range(integ):
                a, b = b, a + b
            integ = a
        elif integ in range(26, 101):
            for prime in [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]:
                if integ < prime: integ = prime
        else:                  
            sum = 0
            while integ > 0:
                digit = integ % 10
                sum += digit
                integ = integ / 10
            integ = int(sum)
        decrementBase -= 1
    print(integ)