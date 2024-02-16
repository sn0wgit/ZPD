class InputPrework{
    constructor(input){
        this.input = String(input);
        this.inputClass = "?";
        console.log("### item {item} 1 - INITIALIZED");
        this.setDataClass();
    }

    notInt(this){
        let notInt = False;
        for (let i = 0; i < len(this.input); i++) {
            let char = this.charAt(i);;
            if (char == ".") {
                notInt = True;
            }
        }
        return notInt;
    }

    notFloat(this){
        let notFloat = False;
        for (let i = 0; i < this.input.length; i++){
            let char = this.input.charAt(i);
            if ("-" == input.charAt(i) ||
                "0" == input.charAt(i) ||
                "1" == input.charAt(i) ||
                "2" == input.charAt(i) ||
                "3" == input.charAt(i) ||
                "4" == input.charAt(i) ||
                "5" == input.charAt(i) ||
                "6" == input.charAt(i) ||
                "7" == input.charAt(i) ||
                "8" == input.charAt(i) ||
                "9" == input.charAt(i) ||
                "." == input.charAt(i)){}else{
                notFloat = True;
            }
        }
        return notFloat;
    }

    setDataClass(this){
        if (this.notFloat() == False && this.notInt() == True){
            print("### item {item} 1 - FLOAT", this.notfloat(), this.notint())
            this.inputClass = "FLOAT"
            this.input = parseFloat(this.input)
        }
        else if (this.notFloat() == False && this.notInt() == False){
            print("### item {item} 1 - INTEGER", this.notfloat(), this.notint())
            this.inputClass = "INTEGER"
            this.input = parseInt(this.input)
        }
        else{
            print("### item {item} 1 - STRING", this.notfloat(), this.notint())
            this.inputClass = "STRING"
        }
    }

    get_class(this){
        return this.inputClass;
    }
    get_input(this){
        return this.input;
    }
}

class PointPerCharacterConvertingSystem{
    constructor(input){
        this.input = input;
        this.letters = ["A","Ā","B","C","Č","D","E","Ē","F","G","Ģ","H","I","Ī","J","K","Ķ","L","Ļ","M","N","Ņ","O","P","Q","R","S","Š","T","U","Ū","V","W","X","Y","Z","Ž"];
        this.output = this.stringProcessor();
    }
    stringProcessor(this){
        let points = 0;
        for (let i = 0; i < this.input.length; i++){
            let letter = this.input.charAt(i)
            if ("0" == letter ||
                "1" == letter ||
                "2" == letter ||
                "3" == letter ||
                "4" == letter ||
                "5" == letter ||
                "6" == letter ||
                "7" == letter ||
                "8" == letter ||
                "9" == letter){
                points += parseInt(letter)
                //print(f"+{letter}")
            }
            else if (letter.upper() in this.letters){
                i = 0
                while (letter.upper() != this.letters[i]){
                    i++
                }
                i++
                points = points + i
                //print(f"+{i}")
            }
        }
        return points;
    }
    get_output(this){
        return this.output;
    }
}
class FloatToInt{
    constructor(this, input){
        this.output = parseInt(String(input).replace(".", ""))
    }
    get_output(this){
        return this.output
    }
}
class ComplexIntegerProcessingScript{
    constructor(input){
        this.input = input
        decrementBase = 100000
        while (decrementBase > 0):
            if      (this.input < 0)               {this.makePositive()}
            else if (this.input in range(0, 5))    {this.pascalTriangleRow()}
            else if (this.input in range(6, 25))   {this.ithFibonacciNumber()}
            else if (this.input in range(26, 101)) {this.nextPrimeNumber()}
            else                                   {this.sumDigits()}
            decrementBase--
            //print(this.input, type(this.input))
        this.output = this.input
    }
    
    makePositive(this){
        //print("makePositive")
        this.input = abs(this.input)
    }
    pascalTriangleRow(this){
        //print("pascalTriangleRow")
        if      (this.input == 0) {this.input = 1}
        else if (this.input == 1) {this.input = 11}
        else if (this.input == 2) {this.input = 121}
        else if (this.input == 3) {this.input = 1331}
        else if (this.input == 4) {this.input = 14641}
        else if (this.input == 5) {this.input = 15101051}
    }
    ithFibonacciNumber(this){
        //print("ithFibonacciNumber")
        a = 1
        b = 1
        for _ in range(this.input):
            a, b = b, a + b
        this.input = a
    }
    nextPrimeNumber(this){
        //print("nextPrimeNumber")
        primes = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        for (let i = 0; i < this.input.length; i++){
            prime = this.length[i]
            if (this.input < prime){
                this.input = prime
            }
        }
    }
    sumDigits(this){
        //print("sumDigits")
        sum = 0
        while (this.input > 0){
            digit = this.input % 10
            sum = sum + digit
            this.input = this.input / 10
        }
        this.input = parseInt(sum)
    }
    get_output(this){
        return parseInt(this.output)
    }
}
class Processing:
    constructor(this, input):
        this.list = input
        for item in input:
            print(f"# item {item} START")
            this.dataitem = item
            print(f"## item {item} 1 START")
            this.firstStage = InputPrework(this.dataitem)
            print(f"## item {item} 1 COMPLETE")
            print(this.firstStage.get_class(), this.firstStage.get_input())
            if this.firstStage.get_class() == "STRING":
                print(f"## item {item} 2 START")
                this.secondStage = PointPerCharacterConvertingSystem(this.firstStage.get_input())
                print(this.secondStage.get_output())
                print(f"## item {item} 2 COMPLETE")
                print(f"## item {item} 3 START")
                this.thirdStage = ComplexIntegerProcessingScript(this.secondStage.get_output())
            else if this.firstStage.get_class() == "FLOAT":
                print(f"## item {item} 2 START")
                this.secondStage = FloatToInt(this.firstStage.get_input())
                print(f"## item {item} 2 COMPLETE")
                print(f"## item {item} 3 START")
                this.thirdStage = ComplexIntegerProcessingScript(this.secondStage.get_output())
            else:
                print(f"## item {item} 2 PASS")
                print(this.firstStage.get_input())
                print(f"## item {item} 3 START")
                this.thirdStage = ComplexIntegerProcessingScript(this.firstStage.get_input())
            print(f"## item {item} 3 COMPLETE", this.thirdStage.get_output())

with open('./input.json', 'r') as f:
    file = json.load(f)

iteration = Processing(file)