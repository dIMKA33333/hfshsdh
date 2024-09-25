try:
    text = input("Введите строку:")
    result = ""
    for item in text:
        if item.isdigit() and result.count(item) == 0:
            result += item
    print(f"{result}")
except ValueError as e:
    print(f"NO {e}")
else:print("NO"
           "")


