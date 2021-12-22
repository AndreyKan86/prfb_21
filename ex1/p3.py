def is_palindrome(string):

    return (string == string[::-1])  # Разворачиваем строку с помощью функции среза, сравниваем с исходной строкой и возвращаем логическое значение


if __name__ == '__main__':
    input_string = input()  # Вводим строку с клавиатуры
    # Выводим текст в зависимости от возврата функции
    if is_palindrome(input_string) == True:
        print('Это палиндром')
    else:
        print('Это не палиндром')
