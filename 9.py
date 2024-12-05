#9
def fibonacci_sum(n):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += b
        a, b = b, a + b
    print("Сумма:", total)


fibonacci_sum(5)
