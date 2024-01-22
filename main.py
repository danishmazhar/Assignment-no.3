#ASSIGNMENT NO.03;

# Question no.01
def calculate_factorial(number):
      factorial = 1
      for i in range(1, number + 1):
          factorial *= i
      return factorial

  
number = int(input("Enter a number: "))

 
result = calculate_factorial(number)
print(f"The factorial of {number} is: {result}")

print("NOW;")
# Question no.02
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = num1 * num2

print(f"The result of multiplying {num1} and {num2} is: {result}")
print("NOW;")
#Question no.03
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))


if denominator != 0:
    
    quotient = numerator / denominator

    
    print(f"The quotient of dividing {numerator} by {denominator} is: {quotient}")
else:
    print("Error: Division by zero is undefined.")

print("THANK YOU!!!!!")