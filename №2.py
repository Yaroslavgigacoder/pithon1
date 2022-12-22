N = int(input())
fact = 1 
list = []
for i in range(2 , N+2):
    list.append(fact)
    fact *=i
print(list)