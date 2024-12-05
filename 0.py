#0
def fibonacci_partial_sum(n, k):
    a, b = 0, 1  
    total = 0
    for i in range(k + n):  
        if i >= k: 
            total += a
        a, b = b, a + b  
    print("Сумма:", total)


# Пример вызова
n = int(input("Введите количество чисел (n): "))
k = int(input("Введите порядковый номер начала (k): "))
fibonacci_partial_sum(n, k)
