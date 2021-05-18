# x = 17
# y = 3
# # z = y
# # y = x
# # x = z
# # print("x = ", x, "y = ", y)
# print("Subtracting y from x = ", x-y)
# print("Multiplication = ", x*y)
# print("division = ", x//y)

# x = 7
# y = 4
# print("x to power y = ",x**y)
# print("Modulo = ",x%y)

# x = 24
# y = 24
# z = 12
# if(x > y and x > z):
#     print(x, " is greater")
# elif y > x and y > z:
#     print(y, " is greater")
# else:
#     print(z, " is greater")

# i = 0
# for i in range(0,5):
#     print(i, end="\t")
# s = "Sunny"
# for i in s:
#     print(i*3)
# b = 1
# for i in range(10, 101, 10):
#     print(f"10 * {b} = ", i)
#     b += 1
# a = '246'
# s = ' Namaste World'
# print(s[1:4])
# print(s*2)
# print(a.isdigit())
# print(a.isalnum())
# print(a.isalpha())
# print(s.upper())        # new
# print(s)
# print(s.strip())  # new
# print(s.isspace())   # new
# print(s.split(" "))
# print(s[13:0:-1])
# a = float(input("Enter 1st number -: "))
# b = float(input("Enter 2nd number -: "))
# c = a+b
# print(c)
# print(fr"Sum is\t {c}")

# def eo(x):
#     if x % 2 == 0:
#         print(f"{x} is even")
#     else:
#         print(f"{x} is odd")


# x = int(input("Enter no -: "))
# eo(x)

# def fact(x):
#     b = 1
#     for i in range(x, 1, -1):
#         b = b*i
#     return b


# a = int(input("Enter your number -: "))
# if a == 0:
#     print(1)
# else:
#     print("Factorial is -: ", fact(a))

# def calc(a, b, o):
#     if o == '+':
#         print(f"Sum of {a} and {b} is -: ", a+b)
#     elif o == '-':
#         print(f"Subtraction of {a} and {b} is -: ", a-b)
#     elif o == '*':
#         print(f"Multiplication of {a} and {b} is -: ", a*b)
#     elif o == '/':
#         print(f"Division of {a} and {b} is -: ", a//b)


# o = input("Enter the operator -: ")
# a = int(input("Enter 1st number -: "))
# b = int(input("Enter 2nd number -: "))
# calc(a, b, o)
# a = input("Enter the expression -: ")
# print(eval(a))
