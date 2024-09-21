class List:
    def __init__(self, name):
        self.todos = []
        self.name = name

    def debug(self):
        print(self.todos)
        print(self.name)

    def add_todo(self, obj):
        self.todos.append(obj)
        return
