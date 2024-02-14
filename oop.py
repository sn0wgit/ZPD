import json

class InputPrework:
    description = "Šī klase ir atbildīga par ievaddatu pirmapstrādi.\
                   Tas iekļauj sevī saraksta _(list)_ lasīšanu un datu definēšanu."
    def __init__(self, input):
        self.input = input
        self.inputClass = str(type(input))

    def NotIntOrFloat(text, symbols):
        state = False
        for char in text:
            if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                state = True
        return state

    def __repr__(self):
        return self.input

    def ReturnClass(self):
        return self.inputClass

class PointPerCharacterConvertingSystem:
    description = "Šī klase ir atbildīga par virknes _(string)_ pārveidošanu."
    def __init__(self, input):
        self.input = input

class FloatToInt:
    description = ""
    def __init__(self, input):
        self.input = input
    
class ComplexIntegerProcessingScript:
    description = ""
    def __init__(self, input):
        self.input = input

class Processing:
    description = "Šī klase ir atbildīga par visu datu apstrādi."
    def __init__(self, input):
        self.list = input
        for unit in input:
            self.dataUnit = input[unit]
            PirmaisPosms = InputPrework(self.dataUnit)
            

