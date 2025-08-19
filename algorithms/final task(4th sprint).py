def platforms_for_robots(weight: list[int], limit: int) -> int:
    """
    https://contest.yandex.ru/contest/52720/problems/A/
    A. Служба доставки
    Функция для определения минимального количества транспортных платформ,
    необходимого для перевозки всех роботов, описанных в массиве.
     - Количество платформ неограниченно.
     - Каждая платформа выдерживает максимальный вес limit.
     - На каждой платформе можно перевезти не более двух роботов при условии,
       что их совокупный вес не превышает limit.
     - Вес отдельного робота не может превышать limit.

    Формат ввода
    В первой строке записан массив целых чисел,
    через пробел — это вес отдельных роботов.
    Во второй строке записан лимит — предельная грузоподъёмность платформы.

    Формат вывода
    Целое число, указывающее на необходимое количество платформ
    для транспортировки.

    Пример 1
    Ввод
    1 2
    3
    Вывод
    1

    Пример 2
    Ввод
    3 2 2 1
    3
    Вывод
    3
    """

    weight.sort()

    platform_count: int = 0
    left: int = 0
    right: int = len(weight) - 1

    while left <= right:
        if weight[left] + weight[right] <= limit:
            left += 1
        right -= 1
        platform_count += 1

    return platform_count


def main():
    """
    Функция для ввода и вывода данных.
    """
    weight: list[int] = list(map(int, input().split()))
    limit: int = int(input())
    print(platforms_for_robots(weight, limit))


if __name__ == '__main__':
    main()
