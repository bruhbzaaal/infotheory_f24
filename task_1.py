import numpy as np

# Функция для кодирования сообщения
def encode(message, n):
    """
    Функция кодирования сообщения путем повторения символов.
    
    message: массив исходного сообщения (например, [1, 0, 1])
    n: количество повторений для каждого символа
    """
    encoded_message = np.repeat(message, n)
    return encoded_message

# Функция для проверки и исправления ошибок в закодированном сообщении
def decode(encoded_message, n):
    """
    Функция декодирования сообщения с исправлением ошибок.
    
    encoded_message: массив закодированного сообщения
    n: количество повторений каждого символа
    """
    # Разбиваем закодированное сообщение на блоки по n символов
    blocks = np.reshape(encoded_message, (-1, n))
    
    # Для каждого блока определяем символ на основе большинства
    corrected_message = np.array([np.bincount(block).argmax() for block in blocks])
    
    return corrected_message

# Пример использования
if __name__ == "__main__":
    # Исходное сообщение
    message = np.array([1, 0, 1])
    
    # Кодирование с повторением 3 раза (код [3, 1])
    n = 3
    encoded = encode(message, n)
    print(f"Закодированное сообщение: {encoded}")
    
    # Внесем ошибку в закодированное сообщение
    encoded_with_error = encoded.copy()
    encoded_with_error[2] = 0  # Вносим ошибку
    print(f"Сообщение с ошибкой: {encoded_with_error}")
    
    # Декодируем и исправляем ошибки
    decoded = decode(encoded_with_error, n)
    print(f"Декодированное и исправленное сообщение: {decoded}")
