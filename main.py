from random import randrange


def random_password():
    # Определяем случайную длину пароля от 7 до 10 символов
    password_length = randrange(7, 11)
    password = ""

    for i in range(password_length):
        char_code = randrange(33, 127)
        char = chr(char_code)
        password += char

    return password


def main():
    generated_password = random_password()
    print(generated_password)


if __name__ == '__main__':
    main()
