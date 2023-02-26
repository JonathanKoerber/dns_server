from hash_map import HashTable
from b_tree import BTree
import random, string
import time
import csv

# get zone object
def zone_object(URL):
    return  {
     "$origin": f"{URL}."#,
    # "$ttl": 3600,
    # "soa": {
    #     "mname": "ns1.something.org.",
    #     "rname": "admin.somethin.org.",
    #     "serial": "{time}",
    #     "refresh": 3600,
    #     "retry": 600,
    #     "expire": 604800,
    #     "minimum": 86400
    # },
    # "ns": [
    #     { "host": "ns1.something.org." },
    #     { "host": "ns2.something.org." }
    # ],
    # "a": [
    #     { "name": "@", "ttl": 400, "value": "255.255.255.255" },
    #     { "name": "@", "ttl": 400, "value": "127.0.0.1" },
    #     { "name": "@", "ttl": 400, "value": "127.0.0.1" },
    #     { "name": "@", "ttl": 400, "value": "127.0.0.1" },
    #     { "name": "@", "ttl": 400, "value": "10.10.10.10" }
    #]
}

def random_string(length):
    pool: str = string.ascii_letters
    return pool

def build_hash_map(stack_size, buckets, needle):

    hay_stack = BTree(buckets)
    pool = random_string(52)
    unique_key = set()
    while len(unique_key) < stack_size:
        url = ''.join(random.choice(pool) for i in range(20))
        if url in unique_key:
            return
        hay_stack.set_val((url, zone_object(url)))
        unique_key.add(url)
    return hay_stack
def build_btree(stack_size, levels, needle):
    '''
    Takes stack_size how many values in'''
    hay_stack = BTree(levels)
    hay_stack.insert((needle, zone_object(needle)))
    pool = random_string(52)
    unique_key = set()
    while len(unique_key) < stack_size:
        url = "".join(random.choice(pool) for i in range(20))
        if url in unique_key:
            return 
        hay_stack.insert((url, zone_object(url + ".com")))
        unique_key.add(url)
    print('reurning hay stack')
    return hay_stack



def main():
    data = {}
    for st in range(101, 1000, 100):
        
        # for l in range(5, 21, 5):
        # haystack = build_btree(st, 2, 'hello_world')
        #     start = time.perf_counter()
        # haystack.print_tree(haystack.root)
            # data = haystack.search_key('hello_world')
        #     stop = time.perf_counter()
        #     if data:
        #         print('time', stop-start, data)
        print(data)
if __name__ == "__main__":
    main()