#5
def sum_of_cubes(n):
    total = sum(i ** 3 for i in range(1, n + 1))
    print("Сумма кубов:", total)


sum_of_cubes(5)
