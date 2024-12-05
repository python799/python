#3
def print_odd_numbers(a, b):
    for i in range(a, b - 1, -1):
        if i % 2 != 0:
            print(i, end=' ')


print_odd_numbers(10, 1)
