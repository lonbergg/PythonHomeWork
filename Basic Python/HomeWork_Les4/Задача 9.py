total_sum = 0

while True:
    user_input = input("Введите любое число, если захочешь конца то введи число с минусом) ")

    try:
        number = int(user_input)
        if number < 0:
            break
        total_sum += number
    except ValueError:
        print("Введи блять целое число еблуша!")

print(f"Общая сумма чисел: {total_sum}")

