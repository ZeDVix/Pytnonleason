from random import randint

x = randint(1,100)
print("Привет, я загадал число от 1 до 100, попробуй угадать его ")
user_num = 0
attempt = 0

while True:
    user_num = int(input("Введи число которое я загадал"))
    attempt += 1
    if user_num == x:
        print("А ты харош, угадал мое число с " + str(attempt) + " попыток")
        break
    elif user_num > x:
        print("Мое число меньше, попробуй снова)")
    elif user_num < x:
        print("Ммм, не, мое число больше, попробуй снова")
