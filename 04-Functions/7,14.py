


def f(number1,number2,operator):
    result = ""
    if operator == "+":
        result = number1 + number2
    if operator == "-":
        result = number1 - number2
    if operator == "%":
        result = number1 % number2
    if operator == "**":
        result = number1 ** number2
    if operator == "*":
        result = number1*number2
    return result 

print(f(2,3, "+")) 
print(f(2,3, "%"))
print(f(2,3, "**")) 
print(f(2,3, "*")) 
print(f(2,3, "-")) 























