m1 = input("Введите ряд: ")
chistaya_stroka = ""
znaki = "!',-.:;=?@"


for char in m1:

    if char not in znaki:

        chistaya_stroka += char

print("Строка без разделтельных знаков: ")
print(chistaya_stroka)
