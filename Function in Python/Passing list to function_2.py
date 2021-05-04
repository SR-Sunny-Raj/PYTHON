lst = []
n = int(input("Enter the number of elements you want in the list : "))
print("Enter the names : ")
for i in range(n):
    lst.append(input())


def count(lst):
    x = 0
    for i in lst:
        if len(i) > 5:
            x += 1
    return x


name = count(lst)
print("There are {} names having more than 5 letters".format(name))
