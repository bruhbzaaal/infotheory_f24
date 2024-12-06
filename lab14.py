def turing_machine(input_string):
    """
    Функция симулирует работу Машины Тьюринга.
    Определяет, чётное или нечётное количество единиц в входной строке.

    :param input_string: строка, содержащая символы '0' и '1'
    :return: строка "Чётное" или "Нечётное"
    """
    # Лента с добавлением конца строки
    tape = list(input_string) + ["_"]  # "_" — символ пустой ячейки
    head = 0  # Положение головки
    state = "q0"  # Начальное состояние

  while (state != "halt_even") and (state != "halt_odd"):
        if state == "q0":
            if tape[head] == "1":
                tape[head] = "X"  # Помечаем единицу
                state = "q1"
                head += 1  # Сдвигаем головку вправо
            elif tape[head] == "0":
                head += 1
            elif tape[head] == "_":  # Конец строки
                state = "halt_even"
        
        elif state == "q1":
            if tape[head] == "1":
                tape[head] = "X"  # Помечаем единицу
                state = "q0"
                head += 1
            elif tape[head] == "0":
                head += 1
            elif tape[head] == "_":  # Конец строки
                state = "halt_odd"

    return "Чётное" if state == "halt_even" else "Нечётное"


# Пример использования:
input_string = "1101"
result = turing_machine(input_string)
print(f"Количество единиц в строке '{input_string}' — {result}.")
