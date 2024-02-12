import re

email = 'vlad@gmail.comm'
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Email валідний.")
else:
    print("Email не валідний.")