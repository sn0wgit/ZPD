import json

class InputPrework:
    description = "Šī klase ir atbildīga par ievaddatu pirmapstrādi - saraksta _(list)_ lasīšanu un datu definēšanu."
    def __init__(self, input):
        self.input, self.inputClass = str(input), "?"
        #print("### item {item} 1 - INITIALIZED")
        self.setDataClass()

    def notint(self):
        notInt = False
        for char in self.input:
            if char == ".":
                notInt = True
        return notInt

    def notfloat(self):
        notFloat = False
        for char in self.input:
            if char not in ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                notFloat = True
        return notFloat

    def setDataClass(self):
        if   self.notfloat() == False and self.notint() == True:
            #print("### item {item} 1 - FLOAT", self.notfloat(), self.notint())
            self.inputClass, self.input = "FLOAT", float(self.input)
        
        elif self.notfloat() == False and self.notint() == False:
            #print("### item {item} 1 - INTEGER", self.notfloat(), self.notint())
            self.inputClass, self.input = "INTEGER", int(self.input)

        else:
            #print("### item {item} 1 - STRING", self.notfloat(), self.notint())
            self.inputClass = "STRING"

    def get_class(self):
        return self.inputClass

    def get_input(self):
        return self.input

class PointPerCharacterConvertingSystem:
    description = "Šī klase ir atbildīga par virknes _(string)_ pārveidošanu."

    def __init__(self, input):
        self.input = input
        self.letters = ["A","Ā","B","C","Č","D","E","Ē","F","G","Ģ","H","I","Ī","J","K","Ķ","L","Ļ","M","N","Ņ","O","P","Q","R","S","Š","T","U","Ū","V","W","X","Y","Z","Ž"]
        self.output = self.stringProcessor()
        
    def stringProcessor(self):
        points = 0
        for letter in self.input:
            if letter.upper() in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                points += int(letter)
                #print(f"+{letter}")
            elif letter.upper() in self.letters:
                i = 0
                while letter.upper() != self.letters[i]:
                    i += 1
                i += 1
                points += i
                #print(f"+{i}")
        return points

    def get_output(self):
        return self.output

class FloatToInt:
    description = "Šī klase pārveido daļu _(float)_ par skaitli _(integer)_"
    def __init__(self, input):
        self.output = int(str(input).replace(".", ""))

    def get_output(self):
        return self.output
    
class ComplexIntegerProcessingScript:
    description = "Šī klase apstrādā skaitļus _(integer)_ ar visdažādākām matemātiskām metodēm 100 reizes"
    def __init__(self, input):
        self.input = input
        decrementBase = 100000
        while decrementBase > 0:
            if   self.input < 0:               self.makePositive()
            elif self.input in range(0, 5):    self.pascalTriangleRow()
            elif self.input in range(6, 25):   self.ithFibonacciNumber()
            elif self.input in range(26, 101): self.nextPrimeNumber()
            else:                              self.sumDigits()
            decrementBase -= 1
            #print(self.input, type(self.input))
        self.output = self.input
    
    def makePositive(self):
        #print("makePositive")
        self.input = abs(self.input)

    def pascalTriangleRow(self):
        #print("pascalTriangleRow")
        if   self.input == 0: self.input = 1
        elif self.input == 1: self.input = 11
        elif self.input == 2: self.input = 121
        elif self.input == 3: self.input = 1331
        elif self.input == 4: self.input = 14641
        elif self.input == 5: self.input = 15101051
    
    def ithFibonacciNumber(self):
        #print("ithFibonacciNumber")
        a, b = 1, 1
        for _ in range(self.input):
            a, b = b, a + b
        self.input = a

    def nextPrimeNumber(self):
        #print("nextPrimeNumber")
        primes = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        for prime in primes:
            if self.input < prime:
                self.input = prime

    def sumDigits(self):
        #print("sumDigits")
        sum = 0
        while self.input > 0:
            digit = self.input % 10
            sum += digit
            self.input = self.input / 10
        self.input = int(sum)
    
    def get_output(self):
        return int(self.output)

class Processing:
    description = "Šī klase ir atbildīga par visu datu apstrādi."
    def __init__(self, input):
        self.list = input
        for item in input:
            #print(f"# item {item} START")
            self.dataitem = item
            #print(f"## item {item} 1 START")
            self.firstStage = InputPrework(self.dataitem)
            #print(f"## item {item} 1 COMPLETE")
            #print(self.firstStage.get_class(), self.firstStage.get_input())
            if self.firstStage.get_class() == "STRING":
                #print(f"## item {item} 2 START")
                self.secondStage = PointPerCharacterConvertingSystem(self.firstStage.get_input())
                #print(self.secondStage.get_output())
                #print(f"## item {item} 2 COMPLETE")
                #print(f"## item {item} 3 START")
                self.thirdStage = ComplexIntegerProcessingScript(self.secondStage.get_output())
            elif self.firstStage.get_class() == "FLOAT":
                #print(f"## item {item} 2 START")
                self.secondStage = FloatToInt(self.firstStage.get_input())
                #print(f"## item {item} 2 COMPLETE")
                #print(f"## item {item} 3 START")
                self.thirdStage = ComplexIntegerProcessingScript(self.secondStage.get_output())
            else:
                #print(f"## item {item} 2 PASS")
                #print(self.firstStage.get_input())
                #print(f"## item {item} 3 START")
                self.thirdStage = ComplexIntegerProcessingScript(self.firstStage.get_input())
            #print(f"## item {item} 3 COMPLETE", self.thirdStage.get_output())

with open('./input.json', 'r') as f:
    file = json.load(f)

iteration = Processing(file)