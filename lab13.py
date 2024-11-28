def fsm(graph, A, B, input_string):
    """
    Симуляция конечного автомата на основе списка смежности.
    
    :param graph: Список смежности в виде словаря {текущее состояние: {входной символ: (следующее состояние, выходной символ)}}.
    :param A: Множество входного алфавита.
    :param B: Множество выходного алфавита.
    :param input_string: Входная строка.
    :return: Выходная строка, сформированная автоматом.
    """
    # Начальное состояние автомата
    state = "start"
    output = []  # Хранилище для выходной строки
    
    for symbol in input_string:
        if symbol not in A:
            raise ValueError(f"Символ '{symbol}' не принадлежит входному алфавиту A.")
        
        # Проверяем наличие перехода для текущего состояния и входного символа
        if state not in graph or symbol not in graph[state]:
            raise ValueError(f"Нет перехода из состояния '{state}' с символом '{symbol}'.")
        
        # Получаем следующее состояние и выходной символ
        next_state, output_symbol = graph[state][symbol]
        
        if output_symbol not in B:
            raise ValueError(f"Выходной символ '{output_symbol}' не принадлежит алфавиту B.")
        
        # Добавляем выходной символ в результат
        output.append(output_symbol)
        # Переход в следующее состояние
        state = next_state
    
    return ''.join(output)


# Пример использования:
if __name__ == "__main__":
    # Список смежности для автомата
    graph = {
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
    result = fsm(graph, A, B, input_string)
    print("Выходная строка:", result)
