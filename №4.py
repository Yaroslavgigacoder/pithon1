import random
list = []
N = int(input())
for i in range(1, N+1):
    list.append(random.randint(-N, N))
random.shuffle(list)
print(list)