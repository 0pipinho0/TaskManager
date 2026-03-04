from task import Task, ImportantTask
from manager import TaskManager

def main():
    print("=== ТЕСТИРОВАНИЕ TASK MANAGER ===\n")
    my_tasks = TaskManager("Мои задачи")
    # Создаем обычные задачи
    task1 = Task("Купить продукты", "Молоко, хлеб", "средний")
    task2 = Task("Сделать зарядку", "30 минут утром", "низкий")
    # Создаем важную задачу (наследник)
    important_task = ImportantTask(
        "Сдать проект",
        "Подготовить презентацию",
        "пятница 18:00"
    )
    important_task.set_reminder()
    # Добавляем задачи в менеджер
    my_tasks.add_task(task1)
    my_tasks.add_task(task2)
    my_tasks.add_task(important_task)
    # Показываем все задачи (полиморфизм!)
    my_tasks.show_all_tasks()
    print("\n=== ДЕТАЛЬНАЯ ИНФОРМАЦИЯ ===\n")
    print(important_task.get_info())
    print("\n=== ФИЛЬТРАЦИЯ ===\n")
    # Получаем задачи по приоритету
    high_priority = my_tasks.get_tasks_by_priority("высокий")
    print("Задачи с высоким приоритетом:")
    for task in high_priority:
        print(f" - {task}")
    # Отмечаем задачу выполненной
    task1.mark_completed()
    print("\n=== СТАТИСТИКА ===\n")
    print(my_tasks)
    # Поиск задач
    print("\n=== ПОИСК ===\n")
    found = my_tasks.find_tasks("проект")
    print("Найденные задачи:")
    for task in found:
        print(f" - {task}")

if __name__ == "__main__":
    main()