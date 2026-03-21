import task1
import task2
import task3
import task4
import task5

def main():
    print("="*50)
    print("Лабораторная работа №3 (Вариант 19)")
    print("Студент: МУРАШКО")
    print("="*50)
    
    while True:
        print("\nВыберите задание:")
        print("1. Разложение arccos(x) в ряд")
        print("2. Умножение последних цифр")
        print("3. Подсчёт пробелов, цифр и знаков пунктуации")
        print("4. Анализ строки из текста")
        print("5. Обработка вещественных списков")
        print("0. Выход")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == '1':
            task1.main_task1()
        elif choice == '2':
            task2.main_task2()
        elif choice == '3':
            task3.main_task3()
        elif choice == '4':
            task4.main_task4()
        elif choice == '5':
            task5.main_task5()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()