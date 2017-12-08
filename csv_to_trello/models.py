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

    def title_with_estimate(self):
        if self.estimate is not None:
            return "{title} ({estimate})".format(title=self.title, estimate=self.estimate)
        else:
            return self.title


class Label:
    def __init__(self, title, color):
        self.title = title
        self.color = color
