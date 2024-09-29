from collections import Counter

# Функция для построения кодов Шеннона-Фано
def build_shannon_fano_codes(symbols, prefix=""):
    # Если в списке один символ, присваиваем ему код
    if len(symbols) == 1:
        symbol, _ = symbols[0]
        return {symbol: prefix}

    # Разделяем символы на две группы с примерно одинаковой суммарной вероятностью
    total_prob = sum(prob for _, prob in symbols)
    cumulative_prob = 0
    split_index = 0

    for i, (_, prob) in enumerate(symbols):
        cumulative_prob += prob
        if cumulative_prob >= total_prob / 2:
            split_index = i
            break

    # Рекурсивно строим коды для обеих групп
    left_codes = build_shannon_fano_codes(symbols[:split_index + 1], prefix + "0")
    right_codes = build_shannon_fano_codes(symbols[split_index + 1:], prefix + "1")

    # Объединяем коды из левой и правой групп
    left_codes.update(right_codes)
    return left_codes

# Функция для сжатия текста методом Шеннона-Фано
def shannon_fano_compress(text):
    # Шаг 1: Рассчитать частоты символов
    frequencies = Counter(text)
    total_count = sum(frequencies.values())
    
    # Преобразуем частоты в вероятности
    probabilities = [(char, freq / total_count) for char, freq in frequencies.items()]
    
    # Упорядочим символы по убыванию вероятности
    probabilities.sort(key=lambda x: x[1], reverse=True)

    # Шаг 2: Построить коды Шеннона-Фано
    shannon_fano_codes = build_shannon_fano_codes(probabilities)

    # Шаг 3: Закодировать текст
    compressed_text = ''.join(shannon_fano_codes[char] for char in text)

    return compressed_text, shannon_fano_codes

# Функция для декодирования сжатого текста методом Шеннона-Фано
def shannon_fano_decompress(compressed_text, shannon_fano_codes):
    # Инвертируем словарь кодов
    reverse_codes = {code: char for char, code in shannon_fano_codes.items()}

    decoded_text = ""
    current_code = ""

    for bit in compressed_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text

# Пример использования
if __name__ == "__main__":
    text = "hello shannon fano coding"
    print("Исходный текст:", text)

    # Сжимаем текст
    compressed_text, codes = shannon_fano_compress(text)
    print("Сжатый текст:", compressed_text)
    print("Коды Шеннона-Фано:", codes)

    # Восстанавливаем текст из сжатого состояния
    decompressed_text = shannon_fano_decompress(compressed_text, codes)
    print("Восстановленный текст:", decompressed_text)
