n = 8 
for i in range(n // 2, n, 2):
    print(' ' * ((n - i) // 2), end='')
    print('+' * i, end='')
    print(' ' * (n - i), end='')
    print('+' * i)
k = 0
for i in range(n * 2, 0, -2):
    margin = (n * 2 - i) // 2
    print(' ' * k + '+' * i)
    k = k + 1
