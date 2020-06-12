

class IndexClient:
    def __init__(self):
        self._index = {}

    def get(self, username: str) -> int:
        return self._index.get(username)

    def add(self, username: str, index_position: int):
        self._index[username] = index_position
