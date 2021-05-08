# None datatype
a = None
print(a)

# Numeric datatype (int,float,complex,bool)
b = 4
print(type(b))
c = 2.5
print(type(c))
d = 4 + 5j
print(type(d))
bool = b > c
print(type(bool))
e = int(c)
print(e)
f = complex(e, b)
print(f)
print(int(True))

# List datatype
lst = [1, 2, 3, 4, 5]
print(lst)

# Set datatype
s = {4, 8, 2, 1, 6, 3}
print(s)

# Tuple datatype
tup = (10, 20, 50, 40, 30)
print(tup)

# String datatype
str = 'Sunny'
print(str)

# Range datatype
k = list(range(10))
print(k)
l = list(range(11, 21, 2))
print(l)

# Dictionary datatype
d = {1: 'sunny', 'raj': 'python', 2.4: 'java'}
print(d)
print(d.keys())
print(d.values())
print(d[2.4])
