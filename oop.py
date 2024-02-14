import json

class InputPrework:
    description = "Šī klase ir atbildīga par ievaddatu pirmapstrādi - saraksta _(list)_ lasīšanu un datu definēšanu."
    def __init__(self, input):
        self.input = str(input)
        self.inputClass = "?"
        print("### unit{unit} 1 - INITIALIZED")
        self.SetDataClass()

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

    def SetDataClass(self):
        if   self.notfloat() == True and self.notint() == False:
            print("### unit{unit} 1 - STRING", self.notfloat(), self.notint())
            self.inputClass = "STRING"
        
        elif self.notfloat() == False and self.notint() == True:
            print("### unit{unit} 1 - FLOAT", self.notfloat(), self.notint())
            self.inputClass = "FLOAT"
            self.input = float(self.input)
        
        elif self.notfloat() == False and self.notint() == False:
            print("### unit{unit} 1 - INTEGER", self.notfloat(), self.notint())
            self.inputClass = "INTEGER"
            self.input = int(self.input)

        else:
            print(f"Error: {self.input}")
            print(self.notfloat(), self.notint())

    def get_class(self):
        return self.inputClass

    def get_input(self):
        return self.input

class PointPerCharacterConvertingSystem:
    description = "Šī klase ir atbildīga par virknes _(string)_ pārveidošanu."

    def __init__(self, input):
        self.input = input
        self.output = 0
        self.points = {"A": 1, \
                       "Ā": 2, \
                       "B": 3, \
                       "C": 4, \
                       "Č": 5, \
                       "D": 6, \
                       "E": 7, \
                       "Ē": 8, \
                       "F": 9, \
                       "G": 10,\
                       "Ģ": 11,\
                       "H": 12,\
                       "I": 13,\
                       "Ī": 14,\
                       "J": 15,\
                       "K": 16,\
                       "Ķ": 17,\
                       "L": 18,\
                       "Ļ": 19,\
                       "M": 20,\
                       "N": 21,\
                       "Ņ": 22,\
                       "O": 23,\
                       "P": 24,\
                       "Q": 25,\
                       "R": 26,\
                       "S": 27,\
                       "Š": 28,\
                       "T": 29,\
                       "U": 30,\
                       "Ū": 31,\
                       "V": 32,\
                       "W": 33,\
                       "X": 34,\
                       "Y": 35,\
                       "Z": 36,\
                       "Ž": 37}
        self.stringProcessor()
        
    def stringProcessor(self):
        for letter in self.input:
            if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                self.output = self.output + int(letter)
            elif letter in self.points:
                self.output = self.output + self.points[letter]
        print(self.output)
        return self.output

    def __repr__(self):
        return self.output

class FloatToInt:
    description = "Šī klase pārveido daļu _(float)_ par skaitli _(integer)_"
    def __init__(self, input):
        self.output = int(str(input).replace(".", ""))

    def __repr__(self):
        return self.output
    
class ComplexIntegerProcessingScript:
    description = "Šī klase apstrādā skaitļus _(integer)_ ar visdažādākām matemātiskām metodēm 100 reizes"
    decrementBase = 100
    def __init__(self, input):
        self.input = input

class Processing:
    description = "Šī klase ir atbildīga par visu datu apstrādi."
    def __init__(self, input):
        self.list = input
        for unit in input:
            print(f"# unit{unit} START")
            self.dataUnit = unit
            print(f"## unit{unit} 1 START")
            self.firstStage = InputPrework(self.dataUnit)
            print(f"## unit{unit} 1 COMPLETE")
            print(self.firstStage.get_class(), self.firstStage.get_input())
            if self.firstStage.get_class() == "STRING":
                print(f"## unit{unit} 2 START")
                self.secondStage = PointPerCharacterConvertingSystem(self.firstStage.get_input())
                print(f"## unit{unit} 2 COMPLETE")
                print(f"## unit{unit} 3 START")
                self.thirdStage = ComplexIntegerProcessingScript(self.secondStage)
                print(f"## unit{unit} 3 COMPLETE")
            elif self.firstStage.get_class() == "FLOAT":
                print(f"## unit{unit} 2 START")
                self.secondStage = FloatToInt(self.firstStage.get_input())
                print(f"## unit{unit} 2 COMPLETE")
                print(f"## unit{unit} 3 START")
                self.thirdStage = ComplexIntegerProcessingScript(self.secondStage)
                print(f"## unit{unit} 3 COMPLETE")
            else:
                print(f"## unit{unit} 2 PASS")
                print(f"## unit{unit} 3 START")
                self.thirdStage = ComplexIntegerProcessingScript(self.firstStage.get_input())
                print(f"## unit{unit} 3 COMPLETE")

iteration = Processing(["HMM", 444, .21])