class Board:
    def __init__(self, title):
        self.title = title
        self.columns = []


class Column:
    def __init__(self, title):
        self.title = title
        self.tasks = []


class Task:
    def __init__(self, title):
        self.title = title
        self.estimate = None
        self.description = None
        self.labels = []


class Label:
    def __init__(self, title, color):
        self.title = title
        self.color = color
