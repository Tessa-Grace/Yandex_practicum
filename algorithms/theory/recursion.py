"""
Рекурсия

Под словом «рекурсия» в контексте программирования понимают, как правило, рекурсивное выполнение каких-то действий, 
например функцию, которая может многократно вызывать саму себя. Рекурсивное выполнение функций часто применяется при работе с иерархическими, 
вложенными данными, когда заранее неизвестна глубина вложенности.

Условия, при которых ничто не препятствует углублению рекурсии, называют рекурсивным случаем.

Условие, при котором рекурсивная функция прекращает вызывать сама себя, называют базовым случаем. 
Без базового случая рекурсия просто не сможет остановиться — и в результате программа завершится с ошибкой.

Итак, корректно работающая рекурсия должна содержать:
- рекурсивный случай, при котором начинается прямой ход рекурсии и происходит её углубление;
- базовый случай, при котором рекурсия перестаёт углубляться и запускается обратный ход рекурсии.

На практике рекурсивный и базовый случаи можно представить как условие «или/или»: если определённое условие выполняется 
— это рекурсивный случай, углубляем рекурсию; если условие не выполняется — это базовый случай, выходим из рекурсии.
Условий для выхода из рекурсии может быть несколько, а значит, и базовых случаев может быть больше одного. 
Главное — точно понять, что именно должно происходить в базовом случае.
Базовый случай определяет ситуацию, при которой рекурсию нужно остановить. 
Для базового случая результат выполнения функции следует вычислить явно, не прибегая к рекурсивным вызовам.

Чтобы изменить объём памяти, выделенный под стек вызовов, в Python используется метод setrecursionlimit() модуля sys. 
В него передаётся параметр limit — он задаёт максимально возможную глубину рекурсии.
Наибольшее возможное значение зависит от платформы, но и оно ограничено. Текущее значение этой величины можно узнать, вызвав метод getrecursionlimit().
"""
# ________________________________________________________________________________________________
# Задача - вывести 138 чисел

def stairs_builder(n):
    if n == 0:  # Базовый случай.
        print('Испанская лестница построена!')
        return
    # Построить 1 ступеньку.
    print(f'Осталось построить ступеней: {n}.')
    stairs_builder(n - 1)  # Рекурсивный случай.


stairs_builder(138)

# ________________________________________________________________________________________________
# Матрешка

# через рекурсию
class Matryoshka:

    def __init__(self, size, item=None):
        self.size = size
        self.inner_item = item


def disassemble_matryoshka(matryoshka):
    """Функция разборки матрёшки."""
    inner_item = matryoshka.inner_item
    if inner_item is None:
        print(f'Все матрёшки разобраны! Размер последней матрёшки: {matryoshka.size}')
        return
    print(f'Разобрали матрёшку размера {matryoshka.size}, разбираем дальше!')
    disassemble_matryoshka(inner_item)

if __name__ == '__main__':
    big_matryoshka = Matryoshka('L', Matryoshka('M', Matryoshka('S')))
    disassemble_matryoshka(big_matryoshka)

# итеративным способом (через цикл)
class Matryoshka:

    def __init__(self, size, item=None):
        self.size = size
        self.inner_item = item


def disassemble_matryoshka(matryoshka):
    """Функция разборки матрёшки."""
    # В этом списке храним ту матрёшку,
    # которую цикл разбирает в текущей итерации.
    # В начале выполнения программы здесь хранится самая большая матрёшка.
    items_for_disassemble = [matryoshka]

    # Пока список items_for_disassemble не пуст, выполняем цикл.
    while items_for_disassemble:
        # Извлекаем последний (он же единственный) элемент из списка.
        element_to_disassemble = items_for_disassemble.pop()
        # Получаем из текущего элемента вложенный.
        inner_item = element_to_disassemble.inner_item
        # Если вложенный элемент существует...
        if inner_item is not None:
            # ...помещаем этот вложенный элемент в спискок.
            # Список был пуст, но полезно вспомнить, 
            # что метод append() добавляет новый элемент в конец списка.
            items_for_disassemble.append(inner_item)
            print(f'Разобрали матрёшку размера {element_to_disassemble.size}, разбираем дальше!')
    # Когда цикл выполнился, печатаем сообщение 
    # об окончании работы и данные последней матрёшки:
    print(f'Все матрёшки разобраны! Размер последней матрёшки: {element_to_disassemble.size}')


if __name__ == '__main__':
    big_matryoshka = Matryoshka('L', Matryoshka('M', Matryoshka('S')))
    disassemble_matryoshka(big_matryoshka)

# ________________________________________________________________________________________________
# Функция разбора коробок (одна в другой в другой в другой...)

# итеративным способом (через цикл) 
class Box:

    def __init__(self, size, inner_items=None):
        self.size = size
        self.inner_items = inner_items

    def __repr__(self):
        # При распечатке объекта через print()
        # будет выводиться свойство size - размер коробки.
        return self.size


def disassemble_boxes(box):
    """Функция разборки коробок."""
    items_for_disassemble = [box]

    # Пока список items_for_disassemble не пуст - выполняем цикл.
    while items_for_disassemble:
        # Извлекаем последний элемент из списка.
        element_to_disassemble = items_for_disassemble.pop()
        # Получаем из текущего элемента вложенные элементы.
        inner_items = element_to_disassemble.inner_items
        # Если вложенные элементы существуют...
        if inner_items is not None:
            # ...добавляем их в список. 
            # Элементов может быть несколько, поэтому применяем extend().
            items_for_disassemble.extend(inner_items)
            print(f'Взяли коробку размера {element_to_disassemble.size}, '
                  f'внутри: {inner_items}.')
        else:
            print(f'В коробке размера {element_to_disassemble.size} '
                  'больше ничего нет.')


if __name__ == '__main__':
    # Создаём четыре маленькие коробки: четыре объекта класса Box. 
    # В них ничего нет.
    small_boxes = [Box(size='S') for _ in range(4)]
    # Создаём коробку среднего размера, пустую:
    middle_box_empty = Box(size='M')
    # Создаём ещё одну среднюю коробку, в неё кладём четыре маленькие:
    middle_box_full = Box(size='M', inner_items=small_boxes)
    # Создаём большую коробку, в неё вкладываем две средние:
    large_box = Box(size='L', inner_items=[middle_box_empty, middle_box_full])
    # Отправляем большую коробку в функцию-разбиратель:
    disassemble_boxes(large_box)


# через рекурсию
class Box:

    def __init__(self, size, inner_items=None):
        self.size = size
        self.inner_items = inner_items

    def __repr__(self):
        return self.size


def disassemble_boxes(box):
    """Функция разборки коробок."""
    print(f'Взяли коробку размера {box.size}, внутри: {box.inner_items}.')
    for item in box.inner_items:
        if item.inner_items is None:
            print(f'В коробке размера {item.size} больше ничего нет.')
            # continue - перейти к следующему шагу цикла, не выполняя код ниже.
            continue
        disassemble_boxes(item)


if __name__ == '__main__':
    small_boxes = [Box(size='S') for _ in range(4)]
    middle_box_full = Box(size='M', inner_items=small_boxes)
    middle_box_empty = Box(size='M')
    large_box = Box(size='L', inner_items=[middle_box_empty, middle_box_full])
    disassemble_boxes(large_box)
