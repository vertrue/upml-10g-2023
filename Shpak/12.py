#     розмір масиву
n = int(input())

#     створення масиву
arr = []
for i in range(0, n):
    arr.append(int(input()))

#     чи є нуль нулів
flag = True
for i in range(0, n):
    if arr[i] == 0:
        flag = False

#     виведення
if flag :
    print("нема")
else:
    print("є")