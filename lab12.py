def fsm(table, A, B, input_string):
    """
    Симуляция конечного автомата.
    
    :param table: Словарь с таблицей переходов {текущее состояние: {входной символ: (следующее состояние, выходной символ)}}.
    :param A: Множество входного алфавита.
    :param B: Множество выходного алфавита.
    :param input_string: Входная строка.
    :return: Строка, сформированная автоматом на основе input_string.
    """
    # Начальное состояние автомата
    state = "start"  # Например, состояние "start"
    output = []  # Хранилище для выходной строки
    
    for symbol in input_string:
        if symbol not in A:
            raise ValueError(f"Символ '{symbol}' не принадлежит входному алфавиту A.")
        
        # Проверяем наличие перехода для текущего состояния и входного символа
        if state not in table or symbol not in table[state]:
            raise ValueError(f"Нет перехода из состояния '{state}' с символом '{symbol}'.")
        
        # Получаем следующее состояние и выходной символ
        next_state, output_symbol = table[state][symbol]
        
        if output_symbol not in B:
            raise ValueError(f"Выходной символ '{output_symbol}' не принадлежит алфавиту B.")
        
        # Добавляем выходной символ в результат
        output.append(output_symbol)
        # Переход в следующее состояние
        state = next_state
    
    return ''.join(output)


# Пример использования:
if __name__ == "__main__":
    # Таблица переходов автомата
    table = {
        "start": {"a": ("q1", "x"), "b": ("q2", "y")},
        "q1": {"a": ("q1", "z"), "b": ("q2", "x")},
        "q2": {"a": ("q1", "y"), "b": ("q2", "z")}
    }
    # Входной и выходной алфавиты
    A = {"a", "b"}
    B = {"x", "y", "z"}
    # Входная строка
    input_string = "abba"
    # Вызываем функцию
    result = fsm(table, A, B, input_string)
    print("Выходная строка:", result)
