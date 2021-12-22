def possibility(list_, destination):
    location = list_[0]     # стартовое положение
    while location < destination: # Цикл движения. Пока не пройдены все значения
        location += list_[location - 1]
    if location == destination: # Проверка на совпадение текущего положения и требуемого
        return ("YES")
    else:
        return ("NO")

if __name__ == '__main__':
    n, t = map(int, input().split()) # вводим данные через пробел, разбиваем функцией split и функцией map присваиваем им тип данных int
    portals = map(int, input().split(" "))
    print(possibility(list(portals), t))
