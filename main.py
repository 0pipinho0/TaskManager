from task import Task

def main():

    print("=== СОЗДАНИЕ ЗАДАЧ ===\n")

    task1 = Task(
    "Купить продукты",
    "Молоко, хлеб, яйца, сыр",
    "высокий"
    )

    task2 = Task(
    "Сделать домашнее задание",
    "Решить задачи по математике",
    "средний"
    )
    task3 = Task(
    "Позвонить родителям",
        priority="низкий"
    )

    print("Краткая информация:")
    print(task1)
    print(task2)
    print(task3)

    print("\n=== ТЕСТИРОВАНИЕ МЕТОДОВ ===\n")

    print(f"Старый приоритет task1: {task1.priority}")
    task1.priority = "средний"
    print(f"Новый приоритет task1: {task1.priority}")

    task2.mark_completed()
    task2.mark_completed()

    print("\n=== ПОЛНАЯ ИНФОРМАЦИЯ ===\n")

    print(task1.get_info())
    print("\n" + "="*40 + "\n")
    print(task2.get_info())

    print("\n=== ПРОВЕРКА ВАЛИДАЦИИ ===\n")

    try:
        task3.priority = "очень высокий"
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        task3.title = ""
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()