# розмір масиву
n = int(input())

# створення масиву
a = []
for i in range(n):
    a.append(int(input()))

# чи є хоча б один нуль
flag = False
for i in range(n):
    if a[i] == 0:
        flag = True

# виведення
if flag:
    print("є")
else:
    print("нема")
