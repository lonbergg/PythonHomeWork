import re
text = "1928346"
if re.match(r"^\d+$", text):
    print("Валидное число")
else:
    print("хуйня")