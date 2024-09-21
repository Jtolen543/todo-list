class Todo:
    def __init__(self, start, end, text, importance, tag=None):
        self.start = start
        self.end = end
        self.text = text
        self.importance = importance
        self.tag = tag

    def debug(self):
        print(self.start)
        print(self.end)
        print(self.text)
        print(self.importance)
        print(self.tag)

