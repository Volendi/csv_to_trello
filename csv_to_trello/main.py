import argparse
from trello_importer import TrelloImporter
from csv_parser import CsvParser


def main(args):
    board = CsvParser(args.board,
                      n_column=args.n_column,
                      n_label=args.n_task_labels,
                      n_task_description=args.n_task_description,
                      n_task_estimate=args.n_task_estimate,
                      n_task_title=args.n_task_title).parse(args.file)
    TrelloImporter().import_board(board)


def parse_args():
    parser = argparse.ArgumentParser(description='Imports csv file into Trello board')
    parser.add_argument('-f', '--file',
                        help='File for importing data',
                        required=True)
    parser.add_argument('-b', '--board',
                        help='Board name to which file should be imported',
                        required=True)
    parser.add_argument('--n-column',
                        help='Index of of column that specifies title for column',
                        type=int,
                        default=0)
    parser.add_argument('--n-task-title',
                        help='Index of of column that specifies title for task',
                        type=int,
                        default=1)
    parser.add_argument('--n-task-description',
                        help='Index of of column that specifies description for task',
                        type=int,
                        default=None)
    parser.add_argument('--n-task-estimate',
                        help='Index of of column that specifies estimate for task',
                        type=int,
                        default=2)
    parser.add_argument('--n-task-labels',
                        help="Index of of column that specifies labels for task. Each label should be separated by ','",
                        type=int,
                        default=3)

    return parser.parse_args()

if __name__ == '__main__':
    main(parse_args())
