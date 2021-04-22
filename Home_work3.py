count_var = ""
res_var = 0
us_var = input("Введите число от 0 до 10")
n = 3
while n > 0:
    count_var = us_var + count_var
    res_var = res_var + int(count_var)
    n -= 1
print(res_var)
