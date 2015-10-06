from linked_list import *


class HashTable():
    def __init__(self):
        self.key_list = []
        self.value_list = []
        self.bucket_limit = 4
        self.set_up_buckets()
        self.checking_limit = False

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
            if self.checking_limit is False:
                self.check_limit()
        else:
            existing_node.value = (existing_node.value[0], val)

    def update(self, key, val):
        hash_val = self.dan_hash(key)
        bucket_idx = hash_val % self.bucket_limit
        bucket_ll = self.value_list[bucket_idx]
        # search linked_list for tuple with key
        existing_node = bucket_ll.find_node_tuple(key)
        if existing_node is None:
            raise ValueError('Key does not exist')
        else:
            # modify node to replace value.
            key_val_pair = (existing_node.value[0], val)
            existing_node.value = key_val_pair

    def get(self, key):
        return self.get_from(key, self.value_list)

    def get_from(self, key, val_list):
        hash_val = self.dan_hash(key)
        bucket_idx = hash_val % len(val_list)
        self.print_length_limit()
        print("list size before crash: " + str(len(self.value_list)))
        print("list size before crash: " + str(len(val_list)))
        print("index: " + str(bucket_idx))
        bucket_ll = val_list[bucket_idx]
        existing_node = bucket_ll.find_node_tuple(key)
        if existing_node is None:
            raise ValueError('Key does not exist')
        else:
            return existing_node.value[1]

    def keys(self):
        return self.key_list

    def values(self):
        val_arr = []
        for each_key in self.key_list:
            # print key-val pairs:
            each_val = self.get(each_key)
            val_arr.append(each_val)
        return val_arr

    def check_limit(self):
        self.checking_limit = True
        if len(self.key_list) >= (self.bucket_limit * 3 / 4):
            self.print_length_limit()
            print('ready to double')
            self.bucket_limit *= 2
            self.set_up_buckets()
        self.checking_limit = False

    def set_up_buckets(self):
        new_list = []
        old_keys = self.key_list
        old_vals = self.value_list
        for each_bucket in range(0, self.bucket_limit):
            each_linked_list = Linked_List()
            new_list.append(each_linked_list)
        self.value_list = new_list
        print("size new list: " + str(len(self.value_list)))
        for idx, each_key in enumerate(old_keys):
            each_val = self.get_from(each_key, old_vals)
            self.set(each_key, each_val)

    def dan_hash(self, input_str):
        input_arr = list(input_str)
        hash_val = 0
        for idx, each_char in enumerate(input_arr):
            char_val = ord(each_char) * (idx + 1)
            hash_val += char_val
        return hash_val

    def __str__(self):
        overall_str = "HashTable:\n"
        for each_key in self.key_list:
            # print key-val pairs:
            each_val = self.get(each_key)
            overall_str += "(" + str(each_key) + ": " + str(each_val) + ")"
            overall_str += "\n"
        return overall_str

    def print_length_limit(self):
        print("length: {0}, limit: {1}".format(len(self.key_list), self.bucket_limit))

if __name__ == '__main__':
    my_hash = HashTable()
    my_hash.set("one", 1)
    my_hash.update("one", 11)
    my_hash.set("two", 2)
    my_hash.print_length_limit()
    my_hash.set("three", 3)
    my_hash.print_length_limit()
    my_hash.set("A", "a")
    my_hash.set("pizza", "food")
    my_hash.set("avocado", "food")
    my_hash.print_length_limit()
    my_hash.set("seven", 7)
    my_hash.set("thumb", "finger")
    # my_hash.update("four", 4)  # should raise error, because "four" does not exist
    # print(my_hash.get("one"))
    # print("keys: " + str(my_hash.keys()))
    # print("vals: " + str(my_hash.values()))
    print(my_hash)
    print(my_hash.dan_hash('Test hash'))
