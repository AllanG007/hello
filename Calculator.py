# Building a Calculator
#x,y +-*/**
#import pdb

def nl():
    print('\n')

nl()

x = float(input("give me a number: "))
o = input("Give me an operator: ")
y = float(input("Give me another number: "))
    #pdb.set_trace()  # This is where the program will pause


Procedure ValidateInput(x, y)
 If (x, y) does not contain a number
      Return "Please Input a Number"
 If (x, y) contains a special character
      Return "Please Input a Number"
end Procedure

Procedure ValidateOperator(o)
 If o does not contain the correct Operator
      Return "Please Input a valid Operator"
 If o contains a number
      Return "Please Input a valid Operator"
end Procedure

if 0 == "+":
    print(x + y)
elif o == "-":
    print(x - y)
elif o == "/":
    print(x / y)
elif o == "*":
    print(x * y)
elif o == "**":
    print(x ** y)
else:
    print("Unknown Operator.")