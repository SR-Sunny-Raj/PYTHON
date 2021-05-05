while(True):
    x = int(input("Enter a number -: "))
    if x <= 100:
        print("Try again!")
        continue
    print("Congratulations you had entered a number greater than 100")
    break
