#6
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("Факториал:", result)


factorial(5)
factorial(4)
factorial(3)
factorial(2)
