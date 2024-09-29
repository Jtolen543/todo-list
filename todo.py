import datetime


class Todo:
    def __init__(self, start, end, task, priority, message, tag):
        self.start = start
        self.end = end
        self.task = task
        self.message = message
        self.priority = priority
        self.button = ""
        self.tag = tag
        self.f_start = datetime.datetime.strptime(self.start, "%Y-%m-%d").strftime("%B %d, %Y")
        self.f_end = datetime.datetime.strptime(self.end, "%Y-%m-%d").strftime("%B %d, %Y")
        self.set_button()

    def debug(self):
        print(self.start)
        print(self.end)
        print(self.task)
        print(self.priority)
        print(self.tag)

    def set_button(self):
        if self.priority == "normal":
            self.button = "img/green-dot.svg"
        elif self.priority == "high":
            self.button = "img/yellow-dot.svg"
        elif self.priority == "urgent":
            self.button = "img/red-dot.svg"

    def switch_completion(self):
        image_map = {
            "normal": "img/green-dot",
            "high": "img/yellow-dot",
            "urgent": "img/red-dot",
        }
        base_image = image_map[self.priority]
        if "check" in self.button:
            self.button = f"{base_image}.svg"
        else:
            self.button = f"{base_image}-check.svg"

    def get_button(self):
        return self.button
