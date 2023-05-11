def fname(a,n):
    """docstring for fname"""

    summa = 0
    for i in range(n):
        if a[i] < 5:
            summa += a[i]
    
    print(summa)
