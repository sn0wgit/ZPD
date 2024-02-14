import json

class InputPrework:
    description = "Šī klase ir atbildīga par ievaddatu pirmapstrādi.\
                   Tas iekļauj sevī saraksta _(list)_ lasīšanu un datu definēšanu."
    def __init__(self, input):
        self.input = input
        self.inputClass = ""

    def NotInt(self):
        notInt = False
        for char in self.input:
            if char is ".":
                notInt = True
        return notInt

    def NotFloat(self):
        notFloat = False
        for char in self.input:
            if char not in ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                notFloat = True
        return notFloat

    def SetDataClass(self):
        if NotFloat() == True    and NotInt == True :
            self.inputClass = "STRING"
        
        elif NotFloat() == True  and NotInt == False:
            self.inputClass = "FLOAT"
            self.input = float(self.input)
        
        elif NotFloat() == False and NotInt == False:
            self.inputClass = "INTEGER"
            self.input = int(self.input)


    def __repr__(self):
        return self.input

    def ReturnClass(self):
        return self.inputClass

class PointPerCharacterConvertingSystem:
    description = "Šī klase ir atbildīga par virknes _(string)_ pārveidošanu."
    def __init__(self, input):
        self.input = input

class FloatToInt:
    description = "Šī klase pārveido daļu _(float)_ par skaitli _(integer)_"
    def __init__(self, input):
        self.input = int(str(input).replace(".", ""))

    def __repr__(self):
        return self.input
    
class ComplexIntegerProcessingScript:
    description = "Šī klase apstrādā skaitļus _(integer)_ ar visdažādākām matemātiskām metodēm 100 reizes"
    decrementBase = 100
    def __init__(self, input):
        self.input = input

    def __repr__(self):
        return self.input

class Processing:
    description = "Šī klase ir atbildīga par visu datu apstrādi."
    def __init__(self, input):
        self.list = input
        for unit in input:
            self.dataUnit = input[unit]
            self.firstStage = InputPrework(self.dataUnit)
            if firstStage.ReturnClass() == "STRING":
                self.secondStage = PointPerCharacterConvertingSystem(firstStage)
                self.thirdStage = ComplexIntegerProcessingScript(secondStage)
            elif firstStage.ReturnClass() == "FLOAT":
                self.secondStage = FloatToInt(firstStage)
                self.thirdStage = ComplexIntegerProcessingScript(secondStage)
            else:
                self.thirdStage = ComplexIntegerProcessingScript(firstStage)