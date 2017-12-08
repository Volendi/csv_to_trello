import csv
import numpy
from models import Board, Column, Task, Label, LabelColor


class CsvParser:
    def __init__(self,
                 board_title,
                 n_column=0,
                 n_task_title=1,
                 n_task_estimate=2,
                 n_task_description=None,
                 n_label=3,
                 skip_title=True):
        self.__n_column = n_column
        self.__n_task_title = n_task_title
        self.__n_task_description = n_task_description
        self.__n_task_estimate = n_task_estimate
        self.__n_label = n_label
        self.__skip_title = skip_title
        self.__board = Board(board_title)

    def parse(self, path_to_file):
        file_content = numpy.array(list(csv.reader(open(path_to_file, "rb"), delimiter=","))).astype("string")
        if self.__skip_title:
            file_content = file_content[1:]

        column = None

        if self.__n_column is None:
            column = Column('Backlog')
            self.__board.columns.append(column)

        for row in file_content:
            column_title = self.__get_content(row, self.__n_column)
            if column_title is not None:
                column = Column(column_title)
                self.__board.columns.append(column)

            task_title = self.__get_content(row, self.__n_task_title)
            if task_title is not None:
                task = Task(task_title)
                task.estimate = self.__get_content(row, self.__n_task_estimate)
                task.description = self.__get_content(row, self.__n_task_description)
                labels = self.__get_content(row, self.__n_label)
                if labels is not None:
                    for l_name in labels.split(','):
                        task.labels.append(Label(l_name, LabelColor.TRANSPARENT))
                column.tasks.append(task)

        return self.__board

    def __get_content(self, row, column_index):
        if column_index is not None:
            if row[column_index] != '':
                return row[column_index]
