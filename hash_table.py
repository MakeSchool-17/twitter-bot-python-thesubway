class HashTable():
    def __init__(self):
        self.keys = []
        self.values = []

    def index_for_key(self, key):
        for idx, each_key in enumerate(self.keys):
            if key == each_key:
                return idx
        return None

    def set(self, key, val):
        # choose a key
        # check for collision
        key_idx = self.index_for_key(key)
        if key_idx is None:
            # so key does not exist:
            self.keys.append(key)
            self.values.append(val)
        else:
            self.values[key_idx] = val
        # how to start with

if __name__ == '__main__':
    my_hash = HashTable()
    my_hash.set("one", 1)
    my_hash.set("one", 11)
    print(my_hash.keys)
    print(my_hash.values)
