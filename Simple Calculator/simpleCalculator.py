#Make the operation select not case-sensitive

while True:
    operation = input("What type of math operation would you like to do? \nAddition, Subtraction, Multiplication, Division\n\n")
    if operation == "Addition":
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        print(number1 + number2)
        break
    elif operation == "Subtraction":
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        print(number1 - number2)
        break
    elif operation == "Multiplication":
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        print(number1 * number2)
        break
    elif operation == "Division":
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        print(number1 / number2)
        break
    else: print("Sorry, it doesn't seem that was an option")
