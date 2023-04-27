n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

summa = 0
for i in range(n):
    if a[i] < 5:
        summa += a[i]

print(summa)
