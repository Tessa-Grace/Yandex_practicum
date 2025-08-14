def valid_mountain_array(numbers):
    """
    https://contest.yandex.ru/contest/52599/problems/
    A. Неправильные горы
    При путешествии по планете марсоход постоянно замеряет высоту рельефа и сохраняет результаты замеров в массив.
    Одна из задач марсохода — поиск «правильных гор». «Правильной» считается та гора, у которой на пути от подножия 
    до вершины высота постоянно растёт, а на пути от вершины к подножию — постоянно уменьшается. Если у горы есть несколько вершин 
    или в каком-то месте встречается горизонтальный участок — это «неправильная гора».
    Напишите функцию valid_mountain_array, которая будет принимать на вход массив с высотами и возвращать True или False 
    в зависимости от того, «правильная» это гора или нет. Если в массиве менее трёх элементов, такой массив не может описывать «правильную» гору.

    Формат ввода
    Массив целых чисел через пробел — отметки о высоте точек рельефа.
    Формат вывода
    Булево значение: True — если гора «правильная», False — если гора «неправильная».

    Пример 1
    Ввод
    2 1 3 5 8
    Вывод
    False
    
    Пример 2
    Ввод
    3 5 5
    Вывод
    False
    """


    max_index = numbers.index(max(numbers))

    if len(numbers) < 3: 
        return False

    if max_index == 0 or max_index == len(numbers) - 1:
        return False

    for num in range(max_index):
        if numbers[num] >= numbers[num + 1]:
            return False

    for num in range(max_index, len(numbers) - 1):
        if numbers[num] <= numbers[num + 1]:
            return False
    return True

def main():
    numbers = list(map(int, input().split()))
    print(valid_mountain_array(numbers))

if __name__ == '__main__':
    main()