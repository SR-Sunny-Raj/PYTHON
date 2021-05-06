f = open("E:\\My Codes\\Python Codes\\April 2021\\30-04-2021\\file1.txt", "r")
# content = f.read()
# print(content)

# for line in f:
#     print(line)

# content = f.readline()
# print(content)

content = f.readlines()
print(content)

f.close()
