class ListManager:
    def __init__(self):
        self.lists = []
        self.current = None

    def add_list(self, arr):
        self.lists.append(arr)

    def remove_list(self, number):
        arr = self.lists[number]
        self.lists.remove(arr)

    def set_current(self, arr):
        self.current = arr

    def get_current(self):
        return self.current

    def get_lists(self):
        return self.lists

    def empty(self):
        return len(self.lists) == 0

    def size(self):
        return len(self.lists)
