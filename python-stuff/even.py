value = int(input("Enter number: "))
sum = 0
for i in range(1, value + 1):
    if i % 2 == 0:
        sum += i

print(sum)