a = ["one", "two", "three"]

a = '","'.join(a) + '"'
# print(f'"{a}')
print(a)

b = ["one", "two", "three"]
b = '"' + '","'.join(b) + '"'
print(b)
