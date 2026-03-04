from task import Task, ImportantTask
from manager import TaskManager
def demonstrate_advanced_features():
    print("=== ДЕМОНСТРАЦИЯ ПРОДВИНУТЫХ ВОЗМОЖНОСТЕЙ ===\n")
# Создаем менеджер задач
    manager = TaskManager("Рабочие задачи")
    print("1. ОБРАБОТКА ОШИБОК:")
    manager.add_task("не задача") # Ошибка типа
    manager.add_task(Task("Купить молоко")) # OK
    manager.add_task(Task("Купить молоко")) # Дубликат
    # 2 Добавляем разные задачи
    print("\n2. ДОБАВЛЕНИЕ ЗАДАЧ:")
    manager.add_task(Task("Сделать отчет", "Заполнить таблицы", "высокий"))
    manager.add_task(ImportantTask("Встреча с клиентом", "Подготовить презентацию", "завтра 10:00"))
    # 3 Демонстрация магических методов
    print("\n3. МАГИЧЕСКИЕ МЕТОДЫ:")
    print(f"Количество задач: {len(manager)}")
    print(f"Первая задача: {manager[0]}")
    print(f"'Купить молоко' в списке? {'Да' if 'Купить молоко' in manager else 'Нет'}")
    # 4 Создание задачи из строки (статический метод)
    print("\n4. СОЗДАНИЕ ИЗ СТРОКИ:")
    task_str = "Позвонить партнеру | Обсудить контракт | высокий"
    new_task = Task.create_from_string(task_str)
    if new_task:
        manager.add_task(new_task)
    # 5 Сохранение в файл
    print("\n5. СОХРАНЕНИЕ В ФАЙЛ:")
    manager.save_to_file("my_tasks.json")
    # 6 Загрузка из файла (создаем новый менеджер)
    print("\n6. ЗАГРУЗКА ИЗ ФАЙЛА:")
    loaded_manager = TaskManager.load_from_file("Загруженные задачи", "my_tasks.json")
    loaded_manager.show_all_tasks()
    # 7 Демонстрация работы с исключениями
    print("\n7. РАБОТА С ИНДЕКСАМИ:")
    task = manager.get_task_by_index(10) # Несуществующий индекс
    task = manager.get_task_by_index("два") # Неверный тип

if __name__ == "__main__":
    demonstrate_advanced_features()
    print("\n" + "="*50)
    print("ПРОЕКТ УСПЕШНО ЗАВЕРШЕН!")