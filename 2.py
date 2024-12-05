#2
def print_numbers_in_order(a, b):
    if a <= b:
        for i in range(a, b + 1):
            print(i, end=' ')
    else:
        for i in range(a, b - 1, -1):
            print(i, end=' ')


print_numbers_in_order(7, 3)
print('\n')
print_numbers_in_order(3, 7)
