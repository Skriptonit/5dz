m = 1
sum = 0
n = int(input())

for i in range(1, n + 1):
    m *= i
    sum += m

print(sum)
