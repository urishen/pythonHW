user_var = int(input("Введите число из последовательности случайных цифр"))
max_sign = 0
while user_var > 9:
    tail_var = user_var % 10
    max_sign = max_sign if (max_sign > tail_var) else tail_var
    user_var = user_var // 10
print(max_sign)
