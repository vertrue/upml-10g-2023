from function import count_zeros

def main():
    n = int(input())
    a = []  
    for i in range(n):
        a.append(int(input()))

    zeros = count_zeros(a) 
    print(zeros)
