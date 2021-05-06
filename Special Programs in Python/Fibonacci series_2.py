def fibo(a, b, n):
    if n <= 1:
        return
    print(b, end=" ")
    a, b = b, a+b
    fibo(a, b, n-1)


n = int(input("Enter the number of terms you want in fibonacci series -: "))
a = 0
b = 1
print(a, end=" ")
fibo(a, b, n)
