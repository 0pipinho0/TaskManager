from task import Task
from datetime import datetime

class TaskManager:
    def __init__(self, name: str):

        self.__name = name
        self.__tasks = []
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self.__name = new_name
        else:
            raise ValueError("Название не может быть пустым")

    def add_task(self, task: Task):
        if isinstance(task, Task):
            self.__tasks.append(task)
            print(f"Задача '{task.title}' добавлена в {self.__name}")
        else:
            raise TypeError("Можно добавлять только объекты класса Task")

    def remove_task(self, title: str):
        for i, task in enumerate(self.__tasks):
            if task.title.lower() == title.lower():
                removed = self.__tasks.pop(i)
                print(f"Задача '{removed.title}' удалена")
                return True
        print(f"Задача '{title}' не найдена")
        return False

    def find_tasks(self, keyword: str):
        found = []
        for task in self.__tasks:
            if (keyword.lower() in task.title.lower() or
                keyword.lower() in task.description.lower()):
                found.append(task)
        return found

    def get_tasks_by_priority(self, priority: str):
        return [task for task in self.__tasks if task.priority == priority]

    def get_completed_tasks(self):
        return [task for task in self.__tasks if task.completed]

    def get_pending_tasks(self):
        return [task for task in self.__tasks if not task.completed]

    def show_all_tasks(self):
        if not self.__tasks:
            print("Список задач пуст")
            return

        print(f"\n=== {self.__name} - Все задачи ===\n")
        for i, task in enumerate(self.__tasks, 1):
            print(f"{i}. {task}")

    def __str__(self):
        total = len(self.__tasks)
        completed = len(self.get_completed_tasks())
        pending = total - completed

        return f"{self.__name}: всего {total} задач (выполнено: {completed}, осталось: {pending})"