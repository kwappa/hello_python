for i in range(1, 1000):
    sosuu = 1
    for j in range(2, i):
        if i % j == 0:
            sosuu = 0
    if sosuu == 1:
        print (i, '(素数)')
    else:
        print(i)
