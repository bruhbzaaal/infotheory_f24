import numpy as np

# Функция для кодирования с использованием кода Хэмминга
def hamming_encode(message):
    """
    Функция для кодирования сообщения с использованием кода Хэмминга.
    
    message: массив исходного сообщения (например, [1, 0, 1, 1])
    """
    m = len(message)
    # Определяем количество проверочных битов
    r = 0
    while (2**r - 1) < (m + r):
        r += 1

    # Инициализируем кодовое слово с местами для проверочных битов
    n = m + r
    encoded = np.zeros(n, dtype=int)

    # Вставляем исходное сообщение в позиции, которые не являются степенями двойки
    j = 0
    for i in range(1, n + 1):
        if not (i & (i - 1)) == 0:  # Позиции, не являющиеся степенями двойки
            encoded[i - 1] = message[j]
            j += 1

    # Рассчитываем проверочные биты
    for i in range(r):
        pos = 2**i
        parity = 0
        for j in range(1, n + 1):
            if j & pos != 0:
                parity ^= encoded[j - 1]
        encoded[pos - 1] = parity

    return encoded

# Функция для проверки и исправления ошибок в коде Хэмминга
def hamming_decode(encoded):
    """
    Функция для декодирования сообщения с использованием кода Хэмминга и исправления ошибок.
    
    encoded: массив закодированного сообщения (например, [1, 0, 0, 1, 1, 0, 1])
    """
    n = len(encoded)
    r = 0
    while 2**r - 1 < n:
        r += 1

    # Проверка на ошибки
    error_pos = 0
    for i in range(r):
        pos = 2**i
        parity = 0
        for j in range(1, n + 1):
            if j & pos != 0:
                parity ^= encoded[j - 1]
        if parity != 0:
            error_pos += pos

    # Если была ошибка, исправляем её
    if error_pos != 0:
        print(f"Ошибка обнаружена в позиции {error_pos}")
        encoded[error_pos - 1] ^= 1  # Инвертируем бит

    # Извлекаем исходное сообщение, исключая проверочные биты
    decoded = []
    for i in range(1, n + 1):
        if not (i & (i - 1)) == 0:  # Позиции, не являющиеся степенями двойки
            decoded.append(encoded[i - 1])

    return np.array(decoded), error_pos

# Пример использования
if __name__ == "__main__":
    # Исходное сообщение
    message = np.array([1, 0, 1, 1])

    # Кодирование с использованием кода Хэмминга
    encoded = hamming_encode(message)
    print(f"Закодированное сообщение: {encoded}")

    # Внесем ошибку в закодированное сообщение
    encoded_with_error = encoded.copy()
    encoded_with_error[4] ^= 1  # Инвертируем бит для имитации ошибки
    print(f"Сообщение с ошибкой: {encoded_with_error}")

    # Декодирование и исправление ошибок
    decoded, error_pos = hamming_decode(encoded_with_error)
    print(f"Декодированное сообщение: {decoded}")
    if error_pos:
        print(f"Ошибка была исправлена в позиции {error_pos}")
