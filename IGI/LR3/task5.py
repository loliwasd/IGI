import math

def input_list() -> list:
    """Ввод вещественного списка с клавиатуры."""
    while True:
        try:
            size = int(input("Введите размер списка: "))
            if size <= 0:
                print("Размер должен быть положительным.")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число.")
    
    lst = []
    print(f"Введите {size} вещественных чисел:")
    for i in range(size):
        while True:
            try:
                val = float(input(f"lst[{i}] = "))
                lst.append(val)
                break
            except ValueError:
                print("Ошибка: введите число.")
    return lst

def print_list(lst: list, name: str = "Список"):
    """Вывод списка на экран."""
    print(f"\n{name}:")
    for i, val in enumerate(lst):
        print(f"  [{i}] = {val}")

def find_max_element_index(lst: list) -> int:
    """Находит индекс максимального элемента списка."""
    max_idx = 0
    max_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            max_idx = i
    return max_idx

def find_first_nonzero_index(lst: list) -> int:
    """Находит индекс первого ненулевого элемента."""
    for i, val in enumerate(lst):
        if val != 0:
            return i
    return -1

def find_second_nonzero_index(lst: list, start_after: int) -> int:
    """Находит индекс второго ненулевого элемента после указанной позиции."""
    count = 0
    for i, val in enumerate(lst):
        if val != 0:
            count += 1
            if count == 2:
                return i
    return -1

def product_between_nonzero(lst: list) -> float:
    """
    Вычисляет произведение элементов между первым и вторым ненулевыми элементами.
    Если между ними нет элементов, возвращает 1.
    """
    first = find_first_nonzero_index(lst)
    if first == -1:
        return 0.0
    
    second = find_second_nonzero_index(lst, first + 1)
    if second == -1 or second <= first + 1:
        return 1.0
    
    product = 1.0
    for i in range(first + 1, second):
        product *= lst[i]
    return product

def main_task5():
    print("=== Задание 5: обработка вещественных списков ===")
    
    while True:
        try:
            # 1) ввод списка
            lst = input_list()
            
            # 2) проверка корректности
            if not lst:
                print("Список пуст. Завершение.")
                return
            
            # 3) вывод списка
            print_list(lst, "Исходный список")
            
            # Основное задание (19 вариант):
            # - найти номер максимального элемента
            # - произведение элементов между первым и вторым ненулевыми
            max_idx = find_max_element_index(lst)
            max_val = lst[max_idx]
            product = product_between_nonzero(lst)
            
            # 4) вывод результатов
            print(f"\nРезультаты:")
            print(f"Номер максимального элемента: {max_idx}")
            print(f"Значение максимального элемента: {max_val}")
            
            first = find_first_nonzero_index(lst)
            second = find_second_nonzero_index(lst, first + 1)
            
            if first == -1:
                print("Нет ненулевых элементов в списке.")
            elif second == -1:
                print("Есть только один ненулевой элемент.")
            elif second <= first + 1:
                print("Между первым и вторым ненулевыми элементами нет элементов.")
            else:
                print(f"Первый ненулевой элемент: индекс {first}, значение {lst[first]}")
                print(f"Второй ненулевой элемент: индекс {second}, значение {lst[second]}")
                print(f"Произведение элементов между ними: {product:.6f}")
            
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")
        
        again = input("\nВыполнить ещё раз? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main_task5()