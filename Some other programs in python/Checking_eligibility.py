x = int(input("Enter your age -: "))
if x > 4 and x < 100:
    if x > 18:
        print("You are eligible to drive vehicles")
    elif x == 18:
        print("Please contact us to check your elegibility")
    else:
        print("You are not eligible to drive vehicles")
else:
    print("Please enter a valid age")

# Lecture practice on if else
# lst = [12, 21, 13, 24, 55]
# if 21 in lst:
#     print("Yass")
# if 1 not in lst:
#     print("Nahh")
