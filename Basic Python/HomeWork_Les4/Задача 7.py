n1 = input("Введите рядок ")
frequency_dict = {}

for char in n1:
    if ('а' <= char <= 'я') or ('А' <= char <= 'Я') or ('0' <= char <= '9'):
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

print("Частота символов в ряде: ")
for char, count in frequency_dict.items():
    print(f"{char}: {count}")
