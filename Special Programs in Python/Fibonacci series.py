n = int(input("Enter the number of terms upto which you want your fibonacci series : "))
result = 0
y = 0


def fib(a=0, b=1):
    global result, y
    y = result
    result = a+b
    print(result, end="\t")


if n > 0:
    print(y, end="\t")
    if n > 1:
        fib()
        for i in range(2, n):
            fib(y, result)
else:
    print("Invalid number of terms given. Please provide valid number of terms")
