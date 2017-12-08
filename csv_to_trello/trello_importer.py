from trello import TrelloClient
import credentials


class TrelloImporter:
    def __init__(self):
        self.__client = TrelloClient(
            api_key=credentials.API_KEY,
            token=credentials.TOKEN,
        )
        self.__labels = []
        self.__tr_board = None

    def __find_board(self, title):
        for board in self.__client.list_boards():
            if board.name == title:
                return board

        raise Exception("Couldn't find test board")

    def __create_label(self, label):
        for l in self.__labels:
            if l.name == label.title and l.color == label.color:
                return l

        return self.__tr_board.add_label(label.title, label.color)

    def __add_label(self, label, tr_task):
        return tr_task.add_label(self.__create_label(label))

    def __add_task(self, task, tr_column):
        tr_task = tr_column.add_card(task.title_with_estimate(), task.description)

        for label in task.labels:
            self.__add_label(label, tr_task)

        return tr_task

    def __add_column(self, column):
        tr_column = self.__tr_board.add_list(column.title)

        for task in column.tasks:
            self.__add_task(task, tr_column)

        return tr_column

    def import_board(self, board):
        self.__tr_board = self.__find_board(board.title)
        self.__labels = self.__tr_board.get_labels()

        for column in board.columns:
            self.__add_column(column)
