n = int(input("Введите сколько прошло минут: "))
hour = n // 60 % 24
minutes = n % 60
print(f"Часы {hour} : Минуты {minutes}")
