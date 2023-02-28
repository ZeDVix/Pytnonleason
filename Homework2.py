# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
# for i in range(0,5):
#     print(i + 1, 0)


# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
# count = 0
# for i in range(10):
#     number = int(input("Введите ваши числа:"))
#     if number == 5:
#         count += 1
# print(count)

#3. Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

#4. Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
# sum = 1
# for i in range(1,10):
#     sum *= i
#     print(sum)

# 5. Вывести цифры числа на каждой строчке.
#
# integer_number = 2129
# print(integer_number%10,integer_number//10)
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

# 6. Найти сумму цифру числа.
# n = int(input("Введите ваше число: "))
# summa_4isel = 0
# while n > 0:
#     summa_4isel += n % 10
#     n = n // 10
# print(summa_4isel)


# 7. Найти произведение цифр числа.
# num = int(input("Введите число: "))
# mult = 1
# while (num != 0):
#     mult = mult * (num % 10)
#     num = num // 10
# print("Произведение =  ", mult)

# 8. Дать ответ на вопрос: есть ли среди цифр числа 5?
# integer_number = int(input("Vvedite 4islo: "))
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

# 9. Найти максимальную цифру в числе
# a = int(input("Vvedite 4islo: "))
# m = a%10
# a = a//10
# while a > 0:
#     if a%10 > m:
#         m = a%10
#     a = a//10
# print(m)


# 10. Найти количество цифр 5 в числе
int_num = 5454
d = 0
while int_num>0:
    if int_num%10 == 5:
        d += 1
    int_num = int_num//10
print('количество цифр 5 :', d)
