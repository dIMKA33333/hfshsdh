try:
    count = 0
    text = input('введите данные:')
    result = ""
    for item in text:
        if item not in result:
            result+=item
    print(result)
except ValueError as e:
    print(f"No {e}")
else: print("NO")
