#include <iostream>
#include <fstream>
#include <string>
#include <variant>
#include "json.hpp"
using namespace std;
using json = nlohmann::json;

class Processing{
    public:
        string inputClass;
        struct CustomVariant {
            std::string strValue;
            int intValue;
            float floatValue;
        };
        CustomVariant input;
        Processing(string item) {
            /*for (int n = 0; n < sizeof(input) / sizeof(int); n++){
                cout << "Hello World!";
            }*/
            string inputClass = setDataClass(item);
            if   (notfloat(item) == false && notint(item) == true){
                //print("### item {item} 1 - FLOAT", self.notfloat(), self.notint())
                input.floatValue = stof(item);
            }
            else if (notfloat(item) == false && notint(item) == false){
                //print("### item {item} 1 - INTEGER", self.notfloat(), self.notint())
                input.intValue = stoi(item);
            }
            else{
                //print("### item {item} 1 - STRING", self.notfloat(), self.notint())
                input.strValue = item;
            }
        }
        int notint(string item){
            bool notInt = false;
            for (int i = 0; i < item.size(); i++){
                string charac = to_string(item[i]);
                if (charac == "."){
                    notInt = true;
                    cout<<"!notInt! 000 !!!";
                }
            }
            return notInt;
        }
        int notfloat(string item){
            bool notFloat = false;
            for (int i = 0; i < item.size(); i++){
                string charac = to_string(item[i]);
                if (charac == "."){
                    notFloat = true;
                    cout<<"!notFloat! 111 !!!";
                }
            }
            return notFloat;
        }
        string setDataClass(string item){
            if   (notfloat(item) == false && notint(item) == true){
                //print("### item {item} 1 - FLOAT", self.notfloat(), self.notint())
                string inputClass = "FLOAT";
            }
            else if (notfloat(item) == false && notint(item) == false){
                //print("### item {item} 1 - INTEGER", self.notfloat(), self.notint())
                string inputClass = "INTEGER";
            }
            else{
                //print("### item {item} 1 - STRING", self.notfloat(), self.notint())
                string inputClass = "STRING";
            }
            return inputClass;
        }

        string get_inputClass(){
            return inputClass;
        }

        std::string get_strValue() { 
            return input.strValue; 
        }

        int get_intValue() { 
            return input.intValue; 
        }

        float get_floatValue() { 
            return input.floatValue; 
        }
};

class FloatToInt{
    public:
        int result;
        FloatToInt(float input){
            std::string strFloat = to_string(input);

            strFloat.erase(std::remove(strFloat.begin(), strFloat.end(), '.'), strFloat.end());

            result = std::stoi(strFloat);
        }
        int get_result(){
            return result;
        }
};
int main(){
    ifstream file("../input.json");
    json j;
    file >> j;

    vector<std::string> dataArray;

    for (auto& item : j) {
        std::string data = item.get<std::string>();
        dataArray.push_back(data);
    }

    for (const auto& data : dataArray) {
        Processing iteration(data);
    }
}