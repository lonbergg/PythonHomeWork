#t_borch = 30
#while t_borch <=100:
    #print("Перемешать")
    #t_borch += 1
    #print(t_borch)
#print("Борщ готов!")

#Задача по циклу вайл ( пример решения )

result = 0
number_or_stop = input("Введите число или стоп ")
while number_or_stop != "stop":
    result += int(number_or_stop)
    number_or_stop = input("Введите число или стоп ")

print(result)