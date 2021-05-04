d = {1: 'sunny', 2: 'Raj', 4: 'Python'}
print(d)
print(d[1])
print(d[2])
print(d.get(3, 'Not Found'))
print(d[4])
keys = [7, 8, 9, 10, 11]
values = ['a', 'b', 'c', 'd', 'e']
dic = dict(zip(keys, values))
print(dic)
dic[12] = 'f'
print(dic)
dicti = {'JS': 'atom', 'python': ['vs code', 'pycharm'],
         'java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
print(dicti)
print(dicti.keys())
print(dicti['JS'])
print(dicti['python'])
print(dicti['python'][1])
print(dicti['java'])
print(dicti['java']['JEE'])
