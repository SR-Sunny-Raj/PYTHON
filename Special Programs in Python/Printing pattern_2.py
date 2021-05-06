def pattern(n, bool):
    if(bool):
        for i in range(0, n):
            for j in range(0, i+1):
                print("*", end=" ")
            print()
    else:
        for i in range(n+1, 0, -1):
            for j in range(1, i):
                print("*", end=" ")
            print()


n = int(input("Enter a number -: "))
while(True):
    b = int(input("Enter 0 or 1 :- "))
    if(b == 0 or b == 1):
        bool = bool(b)
        pattern(n, bool)
        break
    else:
        print("Please enter either 0 or 1 only")
        continue
