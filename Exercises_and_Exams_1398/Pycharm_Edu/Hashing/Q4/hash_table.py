class HashTable:
    class _Cell:
        def __init__(self, key: int, value: object) -> None:
            self._key = key
            self._value = value
            self._isDeleted = False

        def get_key(self):
            return self._key

        def get_value(self):
            return self._value

        def is_deleted(self):
            return self._isDeleted

        def delete(self):
            self._isDeleted = True

    def __init__(self, size):
        self._size = size
        self._table = [None for _ in range(size)]

    def _hash(self, key, i):
        return (key + i) % self._size

    def insert(self, key, value):
        return #Complete it

    def delete(self, key):
        return #Complete it

    def get(self, key):
        return #Complete it

