n = int(input("Enter the number whose factorial you want : "))


def fac(n):
    if n >= 0:
        y = 1
    else:
        y = -1
    x = 1
    for i in range(y, n+y, y):
        x = x*i
    return x


x = fac(n)
print("Factorial of {} is : ".format(n), x)
