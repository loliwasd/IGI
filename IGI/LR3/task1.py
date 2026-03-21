import math

def series_arccos(x: float, eps: float) -> tuple:
    """
    Вычисляет arccos(x) через разложение в ряд.
    Формула: arccos(x) = π/2 - arcsin(x)
    arcsin(x) = x + x³/6 + 3x⁵/40 + ...
    """
    if abs(x) > 1:
        raise ValueError("|x| должен быть <= 1")
    
    if abs(x) == 1:
        return math.acos(x), 1
    
    term = x
    arcsin_val = term
    n = 1
    max_iter = 500
    
    while abs(term) > eps and n < max_iter:
        numerator = (2*n - 1) ** 2
        denominator = (2*n) * (2*n + 1)
        term *= x * x * numerator / denominator
        arcsin_val += term
        n += 1
    
    if n == max_iter and abs(term) > eps:
        raise RuntimeError(f"Не удалось достичь точности {eps} за {max_iter} итераций")
    
    arccos_val = math.pi / 2 - arcsin_val
    return arccos_val, n

def main_task1():
    print("=== Задание 1: разложение arccos(x) ===")
    
    while True:
        try:
            x = float(input("Введите x (|x| <= 1): "))
            eps = float(input("Введите точность eps (например, 1e-6): "))
            
            if eps <= 0:
                print("Точность должна быть положительным числом.")
                continue
            
            result, n = series_arccos(x, eps)
            math_result = math.acos(x)
            
            # Табличный вывод
            print("\n" + "="*60)
            print(f"{'x':<12} {'F(x)':<15} {'Math F(x)':<15} {'eps':<12} {'n'}")
            print("-"*60)
            print(f"{x:<12.6f} {result:<15.10f} {math_result:<15.10f} {eps:<12.6f} {n}")
            print("="*60)
            
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except RuntimeError as e:
            print(f"Ошибка вычислений: {e}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")
        
        again = input("\nПовторить вычисления? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main_task1()