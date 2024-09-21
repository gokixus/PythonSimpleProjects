def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

number = int(input("Number: "))
print(f"Factorial of number: {factorial(number)}")