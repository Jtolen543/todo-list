from todo import Todo


class List:
    def __init__(self, name="New List"):
        self.todos = []
        self.name = name
        self.sort_alg = "default"

    def debug(self):
        print(self.todos)
        print(self.name)

    def add_todo(self, start, end, task, priority, message, tags):
        if not message:
            message = None
        if not tags:
            tags = None
        new_todo = Todo(start, end, task, priority, message, tags)
        self.todos.append(new_todo)
        return

    def delete_todo(self, obj):
        self.todos.remove(obj)

    def get_todos(self):
        return self.todos

    def empty(self):
        return len(self.todos) == 0

    def set_sort(self, value):
        self.sort_alg = value

    def default_sort(self):
        return self.todos

    def priority_sort(self):
        weight = {
            "normal": 1,
            "high": 2,
            "urgent": 3,
        }
        return sorted(self.todos, key=lambda todo: weight[todo.priority], reverse=True)

    def start_sort(self):
        return sorted(self.todos, key=lambda todo: todo.start)

    def end_sort(self):
        return sorted(self.todos, key= lambda todo: todo.end)

    def tag_sort(self):
        return sorted(self.todos, key=lambda todo: todo.tag)

    def sorting(self):
        sort_map = {
            "default": self.default_sort(),
            "priority": self.priority_sort(),
            "start": self.start_sort(),
            "end": self.end_sort(),
            "tags": self.tag_sort()
        }
        return sort_map[self.sort_alg]

    def get_alg(self):
        return self.sort_alg
