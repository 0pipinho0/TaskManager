import json

from task import Task, ImportantTask
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

    def add_task(self, task: Task):
        try:
            if not isinstance(task, Task):
                raise TypeError("Можно добавлять только объекты класса Task")

            for existing_task in self.__tasks:
                if existing_task.title.lower() == task.title.lower():
                    raise ValueError(f"Задача '{task.title}' уже существует")

            self.__tasks.append(task)
            print(f"✓ Задача '{task.title}' добавлена в {self.__name}")

        except TypeError as e:
            print(f"✗ Ошибка типа: {e}")
        except ValueError as e:
            print(f"✗ Ошибка значения: {e}")
        except Exception as e:
            print(f"✗ Непредвиденная ошибка: {e}")

    def get_task_by_index(self, index: int):
        try:
            if not isinstance(index, int):
                raise TypeError("Индекс должен быть целым числом")

            if index < 0:
                raise IndexError("Индекс не может быть отрицательным")

            return self.__tasks[index]

        except IndexError:
            print(f"✗ Задача с индексом {index} не найдена")
            return None
        except TypeError as e:
            print(f"✗ {e}")
            return None

    def __len__(self):
        return len(self.__tasks)

    def __getitem__(self, index):
        return self.get_task_by_index(index)

    def __contains__(self, title):
        return any(task.title.lower() == title.lower() for task in self.__tasks)

    def save_to_file(self, filename: str = "tasks.json"):
        try:
            data = []
            for task in self.__tasks:
                task_data = {
                    'type': 'Important' if isinstance(task, ImportantTask) else 'Regгlar',
                    'title': task.title,
                    'description': task.description,
                    'priority': task.priority,
                    'completed': task.completed,
                    'created_at': task.created_at.isoformat() if task.created_at else None,
                    'completed_at': task.completed_at.isoformat() if task.completed_at else None
                }

                if isinstance(task, ImportantTask):
                    task_data['deadline'] = task.deadline

                data.append(task_data)

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            print(f"✓ Задачи сохранены в файл {filename}")
        except PermissionError:
            print(f"✗ Нет прав для записи в файл {filename}")
        except Exception as e:
            print(f"✗ Ошибка при сохранении: {e}")

    @classmethod
    def load_from_file(cls, name: str, filename: str = "tasks.json"):
        manager = cls(name)
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            for item in data:
                try:
                    if item['type'] == 'Important':
                        task = ImportantTask(
                            item['title'],
                            item['description'],
                            item.get('deadline', 'не указан')
                        )
                    else:
                        task = Task(
                            item['title'],
                            item['description'],
                            item['priority']
                        )
                    if item['completed']:
                        task._Task__completed = True
                        if item['completed_at']:
                            task._Task__completed_at = datetime.fromisoformat(item['completed_at'])

                    manager._TaskManager__tasks.append(task)

                except Exception as e:
                    print(f"✗ Ошибка при загрузке задачи {item.get('title', 'unknown')}: {e}")
                    continue
            print(f"✓ Загружено {len(manager)} задач из файла {filename}")

        except FileNotFoundError:
            print(f"✗ Файл {filename} не найден")
        except json.JSONDecodeError:
            print(f"✗ Ошибка формата JSON в файле {filename}")
        except Exception as e:
            print(f"✗ Ошибка при загрузке: {e}")
        return manager