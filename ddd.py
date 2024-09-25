input_start = input('введите данные:')
punctuation_count = sum(1 for char in input_start if char in ',;!?')
print(punctuation_count)
