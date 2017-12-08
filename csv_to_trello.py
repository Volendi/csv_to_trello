import sys
import argparse


def main(args):
    print(args)


def parse_args():
    parser = argparse.ArgumentParser(description='Imports csv file into Trello board')
    parser.add_argument('-f', '--file', help='File for importing data', required=True)
    parser.add_argument('-b', '--board', help='Board name to which file should be imported', required=True)

    return parser.parse_args()

if __name__ == '__main__':
    main(parse_args())
