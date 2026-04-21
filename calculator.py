while True:
  num1 = int(input("Type the first number: "))
  op = input("Type the operation: ")
  num2 = int(input("Type the second number: "))

  if op == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
  elif op == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
  elif op == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
  else:
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

  a = "Yes"
  b = "No"

  again = input("Do you want to do another operation? ")
  if again == "no":
    break
