input_start = input('введите данные:')
result = ""
for char in input_start:
    if char not in result:
        result+= char
print(result)