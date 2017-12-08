from trello import TrelloClient
import credentials


__client = TrelloClient(
    api_key=credentials.API_KEY,
    token=credentials.TOKEN,
)


def test():
    print(__client.list_boards())
