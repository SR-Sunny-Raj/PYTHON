while(True):
    a = int(input("\nEnter 1st number :- "))
    b = int(input("Enter 2nd number -: "))
    o = input("Enter the operator -: ")
    if o in ['+', '-', '*', '/']:
        if (a == 45 and b == 3 and o == "*") or (a == 3 and b == 45 and o == "*"):
            print("{} * {} = 555".format(a, b))
        elif (a == 56 and b == 9 and o == "+") or (a == 9 and b == 56 and o == "+"):
            print("{} + {} = 77".format(a, b))
        elif a == 56 and b == 6 and o == "/":
            print("{} / {} = 4".format(a, b))
        else:
            if o == "+":
                print("{} + {} = {}".format(a, b, a+b))
            elif o == "-":
                print("{} - {} = {}".format(a, b, a-b))
            elif o == "*":
                print("{} * {} = {}".format(a, b, a*b))
            else:
                print("{} / {} = {}".format(a, b, a/b))
    else:
        print("\nPlease enter a valid operator next time.")
    ch = input("\nDo you want to calculate again(y/n) ? -: ")
    if ch == 'y' or ch == 'Y':
        continue
    else:
        print("See you later")
        break
