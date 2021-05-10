T = int(input())
for i in range(T):
    sum = 0
    x = int(input())
    while int(x/10) != 0:
        y = int(x % 10)
        x = int(x/10)
        sum = sum + y
    sum = sum + x
    print(sum)
