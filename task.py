from datetime import datetime

class Task:
    def __init__(self, title: str, description: str = "", priority: str = "средний"):
        self.__title = title
        self.__description = description
        self.__priority = priority
        self.__completed = False
        self.__created_at = datetime.now()
        self.__completed_at = None

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title.strip()) > 0:
            self.__title = new_title
        else:
            raise ValueError("Название задачи не может быть пустым")

    # Геттеры и сеттеры для description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str):
            self.__description = new_description
        else:
            raise ValueError("Описание должно быть строкой")

    # Геттеры и сеттеры для priority
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, new_priority):
        valid_priorities = ["низкий", "средний", "высокий"]
        if new_priority in valid_priorities:
            self.__priority = new_priority
        else:
            raise ValueError(f"Приоритет должен быть одним из: {valid_priorities}")

    # Геттер для completed (только чтение)
    @property
    def completed(self):
        return self.__completed

    # Геттеры для дат
    @property
    def created_at(self):
        return self.__created_at

    @property
    def completed_at(self):
        return self.__completed_at

    def mark_completed(self):
        if not self.__completed:
            self.__completed = True
            self.__completed_at = datetime.now()
            print(f"Задача '{self.__title}' отмечена как выполненная")
        else:
            print(f"Задача '{self.__title}' уже была выполнена")

    def __str__(self):
        status = "✓" if self.__completed else "○"
        priority_symbol = {
            "низкий": "⬇️",
            "средний": "➡️",
            "высокий": "⬆️"
        }.get(self.__priority, "")

        return f"{status} [{priority_symbol}] {self.__title} - {self.__description[:30]}..."

    def get_info(self):
        """Полная информация о задаче"""
        info = f"Задача: {self.__title}\n"
        info += f"Описание: {self.__description}\n"
        info += f"Приоритет: {self.__priority}\n"
        info += f"Создана: {self.__created_at.strftime('%d.%m.%Y %H:%M')}\n"
        if self.__completed:
            info += f"Выполнена: {self.__completed_at.strftime('%d.%m.%Y %H:%M')}"
        else:
            info += "Статус: Не выполнена"

            return info

    @staticmethod
    def validate_priority(priority):
        valid_priorities = ["низкий", "средний", "высокий"]
        return priority in valid_priorities

    @staticmethod
    def get_priority_emoji(priority):
        emojis = {
            "низкий": "⬇️",
            "средний": "➡️",
            "высокий": "⬆️"
        }
        return emojis.get(priority, "❓")

    @classmethod
    def create_from_string(cls, task_string: str):
        try:
            parts = task_string.split('|')
            title = parts[0].strip()
            description = parts[1].strip() if len(parts) > 1 else ""
            priority = parts[2].strip() if len(parts) > 2 else "средний"

            if not cls.validate_priority(priority):
                priority = "средний"

            return cls(title, description, priority)
        except Exception as e:
            print(f"Ошибка создания задачи из строки: {e}")
            return None

class ImportantTask(Task):
    def __init__(self, title: str, description: str = "",
            deadline: str = "сегодня"):
        super().__init__(title, description, priority="высокий")
        self.__deadline = deadline
        self.__reminder_set = False

    @property
    def deadline(self):
        return self.__deadline
    @deadline.setter
    def deadline(self, new_deadline):
        if isinstance(new_deadline, str) and len(new_deadline.strip()) > 0:
            self.__deadline = new_deadline
        else:
            raise ValueError("Дедлайн не может быть пустым")

    def set_reminder(self):
        self.__reminder_set = True
        print(f" Напоминание установлено для задачи '{self.title}'")

        # Переопределяем метод __str__
    def __str__(self):
        base_str = super().__str__()
        reminder = " " if self.__reminder_set else "⏰"
        return f"{base_str} [Дедлайн: {self.__deadline}] {reminder}"

    def get_info(self):
        base_info = super().get_info()
        base_info += f"\nДедлайн: {self.__deadline}"
        base_info += f"\nНапоминание: {'установлено' if self.__reminder_set else 'не установлено'}"
        return base_info

