string_var1 = input("Как Вас зовут?")
string_var2 = None
int_var1 = int(input("Сколько Вам лет?"))
int_var2 = int(input("Сколько лет вашему брату?"))
float_var = float(input("Какая у Вас температура?"))
bool_var = None
if int_var1 == int_var2:
    string_var2 = "брат близнец"
elif int_var1 > int_var2:
    bool_var = True
else:
    bool_var = False
if bool_var == True:
    string_var2 = "младший брат"
else:
    string_var2 = "старший брат"
print(f"{string_var1}, Вам {int_var1} лет, у Вас есть {string_var2}.")
if float_var >= 37:
    print(f"{float_var} Вероятно Вы заболели.")