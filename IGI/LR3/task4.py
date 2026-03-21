import string

def clean_word(word: str) -> str:
    """Удаляет знаки пунктуации в конце слова."""
    return word.strip(string.punctuation)

def count_words_starting_or_ending_with_vowel(words: list) -> int:
    """Подсчитывает слова, начинающиеся или заканчивающиеся на гласную."""
    vowels = set('aeiouyAEIOUY')
    count = 0
    for word in words:
        cleaned = clean_word(word)
        if cleaned and (cleaned[0] in vowels or cleaned[-1] in vowels):
            count += 1
    return count

def count_char_frequencies(text: str) -> dict:
    """Подсчитывает частоту каждого символа."""
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

def get_words_after_comma(text: str) -> list:
    """Возвращает слова, идущие после запятых (очищенные от знаков)."""
    result = []
    parts = text.split(',')
    for i, part in enumerate(parts):
        if i > 0:
            words = part.strip().split()
            if words:
                cleaned = clean_word(words[0])
                if cleaned:
                    result.append(cleaned)
    return sorted(result)

def main_task4():
    print("=== Задание 4: анализ строки ===")
    
    SAMPLE_TEXT = (
        "So she was considering in her own mind, as well as she could, for the "
        "hot day made her feel very sleepy and stupid, whether the pleasure of "
        "making a daisy-chain would be worth the trouble of getting up and "
        "picking the daisies, when suddenly a White Rabbit with pink eyes ran "
        "close by her."
    )
    
    print("Исходный текст:\n")
    print(SAMPLE_TEXT)
    print("\n" + "="*50)
    
    # Разбиваем на слова
    words = SAMPLE_TEXT.split()
    
    # а) число слов, начинающихся или заканчивающихся на гласную
    count_vowel = count_words_starting_or_ending_with_vowel(words)
    print(f"\nа) Количество слов, начинающихся или заканчивающихся на гласную: {count_vowel}")
    
    # б) сколько раз повторяется каждый символ
    freq = count_char_frequencies(SAMPLE_TEXT)
    print("\nб) Частота повторения символов (только символы, не только буквы):")
    for ch in sorted(freq.keys()):
        if ch == '\n':
            continue
        print(f"   '{ch}': {freq[ch]}")
    
    # в) слова, идущие после запятой, в алфавитном порядке
    words_after_comma = get_words_after_comma(SAMPLE_TEXT)
    print("\nв) Слова, идущие после запятой (в алфавитном порядке):")
    for w in words_after_comma:
        print(f"   {w}")

if __name__ == "__main__":
    import string
    main_task4()