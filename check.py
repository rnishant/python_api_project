C = int(input())
S = int(input())

if S>C:
    Profit = S - C
    print(1)
    print(Profit)
else:
    Loss = C - S
    print(-1)
    print(Loss)