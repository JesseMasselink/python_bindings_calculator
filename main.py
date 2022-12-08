

print("Please enter two numbers")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = float(num1)
num2 = float(num2)

print("First number is",num1)
print("Second number is",num2)

print("What operation would you like to perform?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")

operations = {
  "1": (num1 + num2, "addition"),
  "2": (num1 - num2, "subtraction"),
  "3": (num1 * num2, "multiplication"),
  "4": (num1 / num2, "division"),
  "5": (num1 ** num2, "exponentiation")
}

choice = input("Enter your choice: ")

result, operation_name = operations.get(choice, (None, None))

if result is None:
  print("Error: Invalid choice")
else:
  # Before we print the result of division, we'll check for division by zero
  if choice == "4" and num2 == 0:
      print("Error: Cannot divide by zero")
  else:
      print("The result of the", operation_name, "operation is:", result)
