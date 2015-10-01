class HashTable():
    def __init__(self):
        self.key_list = []
        self.value_list = []

    def index_for_key(self, key):
        for idx, each_key in enumerate(self.key_list):
            if key == each_key:
                return idx
        return None

    def set(self, key, val):
        # choose a key
        # check for collision
        key_idx = self.index_for_key(key)
        if key_idx is None:
            # so key does not exist:
            self.key_list.append(key)
            self.value_list.append(val)
        else:
            self.value_list[key_idx] = val
        # how to start with

    def update(self, key, val):
        key_idx = self.index_for_key(key)
        if key_idx is None:
            pass
        else:
            self.value_list[key_idx] = val

    def get(self, key):
        key_idx = self.index_for_key(key)
        return self.value_list[key_idx]

    def keys(self):
        return self.key_list

    def values(self):
        return self.value_list

if __name__ == '__main__':
    my_hash = HashTable()
    my_hash.set("one", 1)
    my_hash.update("one", 11)
    my_hash.set("two", 2)
    my_hash.set("three", 3)
    my_hash.update("four", 4)  # should do nothing, because "four" does not exist
    print(my_hash.get("one"))
    print(my_hash.keys())
    print(my_hash.values())
