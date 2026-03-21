import string

def count_spaces_digits_punctuation(text: str) -> tuple:
    """
    Подсчитывает количество пробелов, цифр и знаков пунктуации в строке.
    Возвращает кортеж (spaces, digits, punctuation).
    """
    spaces = text.count(' ')
    
    digits = sum(1 for ch in text if ch.isdigit())
    
    punctuation = sum(1 for ch in text if ch in string.punctuation)
    
    return spaces, digits, punctuation

def main_task3():
    print("=== Задание 3: подсчёт пробелов, цифр и знаков пунктуации ===")
    
    while True:
        text = input("Введите строку для анализа: ")
        
        spaces, digits, punctuation = count_spaces_digits_punctuation(text)
        
        print(f"\nРезультаты анализа:")
        print(f"Пробелов: {spaces}")
        print(f"Цифр: {digits}")
        print(f"Знаков пунктуации: {punctuation}")
        print(f"Всего символов: {len(text)}")
        
        again = input("\nПроанализировать другую строку? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main_task3()