import sys

try:
    x=float(input("Give x: "))
    y = float(input("Give y: "))
except ValueError:
    print("Error: invalid input. Not a number")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)
    
print(f"{x} / {y} = {result}")    
