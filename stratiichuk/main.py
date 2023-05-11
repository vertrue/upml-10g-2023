from f import v10

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

if v10(n, a):
    print("є")
else:
    print("нема")
