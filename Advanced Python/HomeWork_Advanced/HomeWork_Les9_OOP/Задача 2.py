class BankAccount:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def deposit(self):
        amount = float(input("Введите свои блять вонючие купюры на пополнение: "))
        if amount > 0:
            self.balance += amount
            print(f"Вы можете пополнить свой хуевый бедный баланас на данную сумму: {amount}"
                  f"\nВаш баланс СУХАРИКОВ С КРАБОМ СЕЙЧАС: {self.balance}")
        elif amount <= 0:
            print(f"Просто иди НАХУЙ отсюда,бомжара ебанный,посмотри сколько денег у тебя в руках! ВОТ {amount}")

    def withdraw(self):
        amount = float(input("Введите сумму на которую хотите кинуть банк! ПИДОРАС:  "))
        if amount > 200:
            self.balance -= amount
            print(f"О да!ебло тупое ты можешь снять свои деревянные!НО КОМИССИЯ 90 ПРОЦЕНТОВ НАХУЙ и пачка сухариков"
                  f"\nОстаток баланса: {self.balance}")
        else:
            print("ПОШЕЛ НАХУЙ!!! НА ТВОЕМ БАЛАНСЕ НИХУЯ НЕТУ кроме мелочи!")

    def __str__(self):
        print(f"Ваш вонючий аккаунт: {self.account}, ваш бомжатский баланс: {self.balance}! Пошел нахуй!")


bank_syharikov = BankAccount("Олег Калавьюти", 1000)
bank_syharikov.deposit()
bank_syharikov.withdraw()
bank_syharikov.__str__()