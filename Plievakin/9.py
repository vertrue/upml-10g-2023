n=int(input())
a = [0] * n
for i in range(n):
    a[i]=int(input())
summa=0
for i in range(n):
    if a[i]<=10:
        summa+=a[i]
print(summa)
