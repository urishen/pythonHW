time_s_in = int(input("Введите время в секундах: "))
time_h = int(time_s_in // 3600)
time_m = int((time_s_in % 3600) // 60)
time_s = int(time_s_in % 3600) % 60
print(f"{time_h: 2}:{time_m: 2}:{time_s: 2}")

