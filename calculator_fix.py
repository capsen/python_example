# Please fix the code below this code should be able let people enter first number, operator, second number then calculate the result base on the input.

def multiply(first, second):
    return first*second

def devide(first, second):
    return first/second

print("Welcome to python calculator")
print("="*18)
firstnumber = float(input("Please enter first number: "))
operator = input("Please enter the operator (+, -, *, /): ")
secondnumber = float(input("Please enter second number: "))
if(operator=="+"):
    result=firstnumber+secondnumber
if(operator=="-"):
    result=firstnumber-secondnumber
if(operator=="*"):
    result=multiply(firstnumber, secondnumber)
if(operator=="/"):
    result=devide(firstnumber, secondnumber)


print("result of", firstnumber,operator, secondnumber,"=", result)