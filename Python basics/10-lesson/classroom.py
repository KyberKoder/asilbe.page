def fibonachchi(n):
    # n = 1
    # n = 2
    # n = 3
    # n = 4
    # n = 5
    sonlar = []
    a, b = 0, 1    
    for i in range(n):
        sonlar.append(a)
        a, b = b, a + b
    return sonlar
print(fibonachchi(n=5))
