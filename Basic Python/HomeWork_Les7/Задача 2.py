import re
text = "hello"
if re.match("^.", text):
    print("Текст валид")
else:
    print("хуйня")