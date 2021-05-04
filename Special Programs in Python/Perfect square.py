import math as m
i = list(range(1, 501))
print('All the perfect square number between 1 and 500 are : ')
for x in i:
    # y = str(m.sqrt(x))
    # if(y[2:] == '0' or y[3:] == '0'):
    if m.sqrt(x) % 1 == 0:
        print(x, end=" ")
