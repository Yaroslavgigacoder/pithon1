N = int(input())
summa = 0
for i in range(1, N+1):
    summa += ((1 + 1/i)**i)
print(round(sum, 3))

