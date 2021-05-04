x = int(input('Enter any three number : '))
y = int(input())
z = int(input())
if x > y and x > z:
    print(str(x)+' is the greatest number among the three numbers')
elif y > x and y > z:
    print(str(y)+' is the greatest number among the three numbers')
elif z > x and z > y:
    print(str(z)+' is the greatest number among the three numbers')
elif x == y or x == z or y == z:
    print('Values are equal')
else:
    print('Invalid Input')
