import json

with open('./input.json', 'r') as file:
    LIST:list[str|int|float] = json.load(file)

for item_raw in LIST:
    #print("STARTED", item_raw)
    #print("First Stage")
    """# First Stage - InputPrework"""
    item:str|int|float = str(item_raw)
    notInt:bool; notFloat:bool = False, False
    for char in item:
        if char not in ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            notFloat = True
        if char == ".":
            notInt = True
    if   notFloat == False and notInt == True : itemClass:str; item = "FLOAT",   float(item_raw)
    elif notFloat == False and notInt == False: itemClass:str; item = "INTEGER", int(item_raw)
    else                                      : itemClass:str; item = "STRING",  str(item_raw)
    #print(f"{item} is {itemClass}")

    """# Second Stage"""
    integ:int = 0
    if itemClass == "STRING":
        """## STRING"""
        #print("Second Stage (STRING)", item)
        LETTERS = ["A","Ā","B","C","Č","D","E","Ē","F","G","Ģ","H","I","Ī","J","K","Ķ","L","Ļ","M","N","Ņ","O","P","Q","R","S","Š","T","U","Ū","V","W","X","Y","Z","Ž"]
        for letter in item:
            ##print(letter.upper())
            if letter.upper() in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                integ += int(letter)
                ##print(f"+{letter}")
            elif letter.upper() in LETTERS:
                i = 0
                while letter.upper() != LETTERS[i]:
                    i += 1
                i += 1
                integ += i
                ##print(f"+{i}")
        ##print("Second Stage (STRING)", f"[{item}] = [{integ}]")
    elif itemClass == "FLOAT":
        """## FLOAT"""
        #print("Second Stage (FLOAT)", item)
        floatstring = str(item)
        integ = int(floatstring.replace(".", ""))
    elif itemClass == "INTEGER":
        """## INTEGER"""
        #print("Second Stage (INTEGER), PASS", item)
        integ = item
    
    """# Third Stage"""
    #print("Third Stage", integ)
    def makePositive(input) -> int:
        """Atgriež veselo skaitli"""
        ##print("makePositive")
        return abs(input)
    def pascalTriangleRow(input) -> int:
        """Atgriež Paskāla trīsstūra n-1 rindu"""
        ##print("pascalTriangleRow")
        if   input == 0: return 1
        elif input == 1: return 11
        elif input == 2: return 121
        elif input == 3: return 1331
        elif input == 4: return 14641
        elif input == 5: return 15101051
    def ithFibonacciNumber(input) -> int:
        """Atgriež n-to Fibonači skaitli"""
        ##print("ithFibonacciNumber")
        a, b = 1, 1
        for _ in range(input):
            a, b = b, a + b
        return a
    def nextPrimeNumber(input) -> int:
        """Atgriež mazāko no pirms _n_ skaitļa"""
        ##print("nextPrimeNumber")
        PRIMES = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        for prime in PRIMES:
            if input < prime:
                input = prime
        return input
    def sumDigits(input) -> int:
        """Atgriež skaitļa ciparu summu"""
        ##print("sumDigits")
        sum:int = 0
        while input > 0:
            digit = input % 10
            sum += digit
            input = input / 10
        return int(sum)
    decrementBase:int = 100000
    while decrementBase > 0:
        if   integ <  0             : integ = makePositive(integ)
        elif integ in range(0, 5)   : integ = pascalTriangleRow(integ)
        elif integ in range(6, 25)  : integ = ithFibonacciNumber(integ)
        elif integ in range(26, 101): integ = nextPrimeNumber(integ)
        else                        : integ = sumDigits(integ)
        decrementBase -= 1
        ##print(int, type(int))
    item_processed:int = int(integ)
    #print("COMPLETE", item_processed)