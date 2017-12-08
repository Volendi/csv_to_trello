from trello import TrelloClient
import credentials


__client = TrelloClient(
    api_key=credentials.API_KEY,
    token=credentials.TOKEN,
)


def __find_board(title):
    for board in __client.list_boards():
        if board.name == title:
            return board

    raise Exception("Couldn't find test board")


def __create_label(label, tr_board):
    return tr_board.add_label(label.title, label.color)


def __add_label(label, tr_task, tr_board):
    return tr_task.add_label(__create_label(label, tr_board))


def __add_task(task, tr_column, tr_board):
    tr_task = tr_column.add_card(task.title_with_estimate(), task.description)

    for label in task.labels:
        __add_label(label, tr_task, tr_board)

    return tr_task


def __add_column(column, tr_board):
    tr_column = tr_board.add_list(column.title)

    for task in column.tasks:
        __add_task(task, tr_column, tr_board)

    return tr_column


def import_board(board):
    tr_board = __find_board(board.title)

    for column in board.columns:
        __add_column(column, tr_board)
