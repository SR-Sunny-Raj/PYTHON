x = int(input("Enter any positive number to check if it's prime or not : "))
for i in range(2, int(x/2)+1):
    if x % i == 0:
        print(x, ' is not a prime number')
        break
else:
    print(x, ' is a prime number')
