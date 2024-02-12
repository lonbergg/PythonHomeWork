secret_num = 7
while True:
        n1 = input("Вгадайте секретне число від 1 до 10 ")

        if n1 == '0':
            print("Наступного разу пощастить!")
            break

        try:
            n1 = int(n1)
            if 1 <= n1 <= 10:
                if n1 == secret_num:
                    print("Ты гачи пес! Це перемога!!!!!")
                    break
                else:
                    print("Спробуйте ще раз.")
            else:
                print("Будь ласка пеодор введі число від 1 до 10.")
        except ValueError:
            print("Будь ласка, введіть коректне ціле число.")
