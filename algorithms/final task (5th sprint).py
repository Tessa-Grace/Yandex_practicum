from string import digits

PLACE_VALUE: int = 10
digits_set: set[str] = set(digits)

def encrypted_instructions(data: str) -> str:
    """
    ID 141456219
    """
    stack: list[tuple[int, str]] = []
    current_str: str = ''
    current_num: int = 0

    for item in data:
        if item in digits_set:
            current_num = current_num * PLACE_VALUE + int(item)
        elif item == '[':
            stack.append((current_num, current_str))
            current_num = 0
            current_str = ''
        elif item == ']':
            num, prev_str = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += item
    return current_str


def main():
    """Функция для ввода данных"""
    data: str = input()
    print(encrypted_instructions(data))


if __name__ == '__main__':
    main()
