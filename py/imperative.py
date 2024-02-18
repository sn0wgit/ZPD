import json

with open('./input.json', 'r') as file:
    list = json.load(file)

for item_raw in list:
    #print("STARTED", item_raw)
    #print("First Stage")
    # First Stage - InputPrework
    item = str(item_raw)
    notInt, notFloat = False, False
    for char in item:
        if char not in ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            notFloat = True
        if char == ".":
            notInt = True
    if   notFloat == False and notInt == True:  itemClass, item = "FLOAT",   float(item_raw)
    elif notFloat == False and notInt == False: itemClass, item = "INTEGER", int(item_raw)
    else:                                       itemClass, item = "STRING",  str(item_raw)
    #print(f"{item} is {itemClass}")

    # Second Stage
    integ = 0
    ## STRING
    if itemClass == "STRING":
        #print("Second Stage (STRING)", item)
        letters = ["A","Ā","B","C","Č","D","E","Ē","F","G","Ģ","H","I","Ī","J","K","Ķ","L","Ļ","M","N","Ņ","O","P","Q","R","S","Š","T","U","Ū","V","W","X","Y","Z","Ž"]
        for letter in item:
            ##print(letter.upper())
            if letter.upper() in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                integ += int(letter)
                ##print(f"+{letter}")
            elif letter.upper() in letters:
                i = 0
                while letter.upper() != letters[i]:
                    i += 1
                i += 1
                integ += i
                ##print(f"+{i}")
        ##print("Second Stage (STRING)", f"[{item}] = [{integ}]")
    ## FLOAT
    elif itemClass == "FLOAT":
        #print("Second Stage (FLOAT)", item)
        floatstring = str(item)
        integ = int(floatstring.replace(".", ""))
    ## INTEGER
    elif itemClass == "INTEGER":
        #print("Second Stage (INTEGER), PASS", item)
        integ = item
    
    # Third Stage
    #print("Third Stage", integ)
    def makePositive(input):
        ##print("makePositive")
        input = abs(input)
        return input
    def pascalTriangleRow(input):
        ##print("pascalTriangleRow")
        if   input == 0: input = 1
        elif input == 1: input = 11
        elif input == 2: input = 121
        elif input == 3: input = 1331
        elif input == 4: input = 14641
        elif input == 5: input = 15101051
        return input
    def ithFibonacciNumber(input):
        ##print("ithFibonacciNumber")
        a, b = 1, 1
        for _ in range(input):
            a, b = b, a + b
        input = a
        return input
    def nextPrimeNumber(input):
        ##print("nextPrimeNumber")
        primes = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        for prime in primes:
            if input < prime:
                input = prime
        return input
    def sumDigits(input):
        ##print("sumDigits")
        sum = 0
        while input > 0:
            digit = input % 10
            sum += digit
            input = input / 10
        input = int(sum)
        return input
    decrementBase = 100000
    while decrementBase > 0:
        if   integ < 0:               integ = makePositive(integ)
        elif integ in range(0, 5):    integ = pascalTriangleRow(integ)
        elif integ in range(6, 25):   integ = ithFibonacciNumber(integ)
        elif integ in range(26, 101): integ = nextPrimeNumber(integ)
        else:                         integ = sumDigits(integ)
        decrementBase -= 1
        ##print(int, type(int))
    item_processed = int(integ)
    #print("COMPLETE", item_processed)