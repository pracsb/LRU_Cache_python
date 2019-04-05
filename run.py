from Prachi_LRU import LRUCache

def main():
    # creating an instance of LRUCache
    # Initializing capacity size
    max_capacity = 4
    c1 = LRUCache(max_capacity)
    # Doing put() operation with key => 3 and value => 6
    c1.put(3, 6)
    c1.put(5, 10)
    c1.put(2, 4)
    c1.put(7, 14)
    c1.put(5, 15)
    # Doing display() operation to show contents of LRU cache
    c1.display()
    # Doing get() operation to fetch the value corresponding to the key passed
    print(c1.get(6))
    print(c1.get(5))

main()
