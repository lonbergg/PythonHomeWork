>>> s1 = "Привіт" + " світ"
>>> s2 = " світ"
>>> s1 + s2
'Привіт світ світ'

>>> "Hello, " "world"
Hello, world
>>> s3 = "+"
>>> s3 * 10
++++++++++


my_string = "Hello, World!"

# Отримання підрядка з індексом від 0 до 4 (включно)
substring = my_string[0:5]  # "Hello"

# Отримання підрядка з індексом від 7 до кінця
substring = my_string[7:]  # "World!"

# Отримання підрядка від початку до 4 (включно)
substring = my_string[:5]  # "Hello"

# Отримання підрядка з кроком 2 (кожен другий символ)
substring = my_string[0:11:2]  # "Hlo ol"


>>> s1 = "1a"
>>> s2 = "aa"
>>> s3 = "Aa"
>>> s4 = "ba"

>>> "1a" > "aa"  # порівняння цифри з буквою
False

>>> "aa" > "Aa"  # порівняння регістрів
True

>>> "aa" > "ba"  # порівняння букв за алфавітним порядком
False

>>> "aa" < "az"  # перші букви однакові, порівнюються наступні дві
True


>>> s1 = "Intel"
>>> s2 = "intel"
>>> s1 == s2
False
>>> s1.lower() == s2.lower()
True


text = "Hello, World!"

lowercase_text = text.lower() # "hello, world!"
uppercase_text = text.upper() # "HELLO, WORLD!"


text = "Hello, World!  "
stripped_text = text.strip() # "Hello, World!"

text = "##Hello, World!##"
stripped_text = text.strip("#") # "Hello, World!"