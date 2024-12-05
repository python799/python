#7
def sum_of_factorials(n):
    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total += fact
    print("Сумма факториалов:", total)


sum_of_factorials(5)
