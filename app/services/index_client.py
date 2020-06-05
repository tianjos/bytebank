class IndexClient:
    def __init__(self):
        # {username: index clients position} ex. {'foo': 10}
        self._index = {}

    def get_client_position(self, username: str) -> int:
        return self._index.get(username)
