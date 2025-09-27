from random import *
import string

symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
           , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
           , '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
           , '!', '@', '#', '$', '%', '^', '&', '*', ]


choose = input("Choose language (ru/en): ").lower()

if choose == "en":
    def generate_password_en(length):
        password = ''
        for i in range(length):
            password += symbols[randint(0, len(symbols) - 1)]
        return password

    while True:
        length_en = int(input("Enter password length: "))
        if length_en < 6:
            print("The minimum password length is 6 characters")
        elif length_en > 30:
            print("The maximum password length is 30 characters")
        else:
            print("Your password:", generate_password_en(length_en))
            break
    input("Press Enter for exit")

elif choose == "ru":
    def generate_password_ru(length):
        password = ''
        for i in range(length):
            password += symbols[randint(0, len(symbols) - 1)]
        return password

    while True:
        length_ru = int(input("Введите длину пароля: "))
        if length_ru < 6:
            print("Минимальная длина пароля 6 символов")
        elif length_ru > 30:
            print("Максимальная длина пароля 30 символов")
        else:
            print("Ваш пароль:", generate_password_ru(length_ru))
            break
    input("Нажмите Enter для выхода")

else:
    print("Invalid language / Неверный язык")
    input("Press Enter for exit")
