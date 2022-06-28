
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# comment
while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        
        if choice == '1':
            resultadoSum = add.sum(number1, number2)
            print("Sum: " + resultadoSum)
        
        elif choice == '2':
            resultadoSub = subFile.sub(number1, number2)
            print("Sub: " + resultadoSub)

        elif choice == '3':
            resultadoMult = multiply.multiply(number1, number2)
            print("Multiply: " + resultadoMult)

        elif choice == '4':
            resultadoDiv = divFile.div(number1, number2)
            print("Div: " + resultadoDiv)
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
