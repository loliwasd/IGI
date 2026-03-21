def multiply_last_digits():
    """
    Принимает целые числа с клавиатуры, перемножает их последние цифры.
    Окончание цикла — ввод числа 0.
    """
    product = 1
    has_input = False
    
    print("Введите целые числа (0 для завершения):")
    
    while True:
        try:
            num = int(input("> "))
            
            if num == 0:
                break
            
            last_digit = abs(num) % 10
            product *= last_digit
            has_input = True
            print(f"Последняя цифра: {last_digit}, текущее произведение: {product}")
            
        except ValueError:
            print("Ошибка: введите целое число!")
    
    if has_input:
        print(f"\nПроизведение последних цифр = {product}")
    else:
        print("\nНе было введено ни одного числа (кроме 0)")

def main_task2():
    print("=== Задание 2: умножение последних цифр ===")
    
    while True:
        multiply_last_digits()
        again = input("\nВыполнить ещё раз? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main_task2()