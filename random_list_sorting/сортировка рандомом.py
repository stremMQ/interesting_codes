from random import shuffle
import time

start_time = time.time()
number = list((input("Введите число для сортировки: ")))
sort_number = ''
cnt = 0
while sort_number == '':
    num = -1000000
    for i in range(len(number)):
            if int(number[i]) >= num:
                num = int(number[i])
                sort_number += number[i]
            else:
                sort_number = ''
                shuffle(number)
                break
print(f"Отсортированое число: {sort_number}")
end_time = time.time()
print(f"время выполнения кода: {end_time - start_time}")
