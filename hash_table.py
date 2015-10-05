from linked_list import *


class HashTable():
    def __init__(self):
        self.key_list = []
        self.value_list = []
        self.bucket_limit = 20
        self.set_up_buckets()

    def index_for_key(self, key):
        for idx, each_key in enumerate(self.key_list):
            if key == each_key:
                return idx
        return None

    def set(self, key, val):
        hash_val = self.dan_hash(key)
        bucket_idx = hash_val % self.bucket_limit
        bucket_ll = self.value_list[bucket_idx]
        # search linked_list for tuple with key
        existing_node = bucket_ll.find_node_tuple(key)
        if existing_node is None:
            # so key does not exist yet
            # check for collision:
            self.key_list.append(key)
            # store a tuple with key and value
            key_val_pair = (key, val)
            bucket_ll.unshift(key_val_pair)
            self.check_limit()
        else:
            existing_node = bucket_ll.find_node(val)
            existing_node.value = val
        # how to start with

    def update(self, key, val):
        key_idx = self.index_for_key(key)
        if key_idx is None:
            pass
        else:
            self.value_list[key_idx] = val

    def get(self, key):
        hash_val = self.dan_hash(key)
        bucket_idx = hash_val % self.bucket_limit
        print("bucket_idx = {0} = {1} % {2}".format(bucket_idx, hash_val, self.bucket_limit))
        bucket_ll = self.value_list[bucket_idx]
        existing_node = bucket_ll.find_node_tuple(key)
        if existing_node is None:
            raise ValueError('Key does not exist')
        else:
            return existing_node.value[1]

    def keys(self):
        return self.key_list

    def values(self):
        return self.value_list

    def check_limit(self):
        if len(self.value_list) > (self.bucket_limit * 3 / 4):
            # self.bucket_limit *= 2
            pass

    def set_up_buckets(self):
        new_list = []
        for each_bucket in range(0, self.bucket_limit):
            each_linked_list = Linked_List()
            new_list.append(each_linked_list)
        self.value_list = new_list

    def dan_hash(self, input_str):
        input_arr = list(input_str)
        hash_val = 0
        for idx, each_char in enumerate(input_arr):
            char_val = ord(each_char) * (idx + 1)
            hash_val += char_val
        return hash_val

    def __str__(self):
        overall_str = ""
        for each_key in self.key_list:
            # print key-val pairs:
            overall_str += "(" + each_key + ": " + self.get(each_key) + ")"
            overall_str += "\n"

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
