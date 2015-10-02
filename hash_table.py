class HashTable():
    def __init__(self):
        self.key_list = []
        self.value_list = []
        self.bucket_limit = 10

    def index_for_key(self, key):
        for idx, each_key in enumerate(self.key_list):
            if key == each_key:
                return idx
        return None

    def set(self, key, val):
        key_idx = self.index_for_key(key)
        if key_idx is None:
            # so key does not exist yet
            hash_val = self.dan_hash(val)
            bucket_idx = hash_val % self.bucket_limit
            # check for collision:
            self.key_list.append(key)
            self.value_list.append(val)
            self.check_limit()
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

    def check_limit(self):
        if len(self.value_list) > (self.bucket_limit * 3 / 4):
            self.bucket_limit *= 2

    def dan_hash(self, input_str):
        input_arr = list(input_str)
        hash_val = 0
        for idx, each_char in enumerate(input_arr):
            char_val = ord(each_char) * (idx + 1)
            hash_val += char_val
        return hash_val

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
    print(my_hash.dan_hash('Test hash'))
