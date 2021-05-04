import math
print('All perfect square numbers between 1 and 500 are : ')
for i in range(1, 501):
    i = i**2
    if(i > 500):
        break
    print(i, end=" ")
