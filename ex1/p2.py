def string_lenght(string):
    return (len(set(string)))  # set - удаляет повторяющиеся символы, len - возвращает количество символов


if __name__ == '__main__':
    input_string = input()  # Вводим строку с клавиатуры
    print(string_lenght(input_string)) # Выводим значение функции
