N = int(input())
sum = 0
for i in range(1, N+1):
    sum += ((1 + 1/i)**i)
print(round(sum, 3))

