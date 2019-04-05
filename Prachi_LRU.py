class Node:
    def __init__(self, key, value):
        """
        This function will create a Node with the given key and value

        :param key: The key to be inserted
        :param value: The value corresponding to that key

         next : Pointer to point to the next node in doubly linked list
                Initialized to None while creating any new node
         prev : Pointer to point to the previous node in the doubly linked list
                Initialized to None while creating any new node
        """
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :param capacity: The maximum elements/nodes the cache can store at any given time

        This function will create:
        1) Dictionary: Stores key, Node corresponding to that key - which are currently present in the cache.
                       Used so that get() takes O(1) time to retrieve the value for a given key.
        2) head : Dummy variable to represent the start of the cache represented as a doubly linked list.
                  Has key=0, val=0 always.
        3) tail : Dummy variable to represent the end of the cache represented as a doubly linked list.
                  Has key=0, val=0 always.
        Initially, the LRU cache contains only the head and tail as follows:
        head <--> tail
        head's next pointer points to tail and tail's prev pointer points to head & no node is in between

        # Time Complexity : O(1)
        # Space Complexity: O(1)
        # as it initializes a capacity variable, dictionary and 2 dummy nodes for DLL (head and tail)
        """

        self.capacity = capacity
        self.dictionary = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        """
        :param node: Key, Value pair
                     Object of Node class

        This function removes the specified node from the cache.

        # Time Complexity => O(1)
        # as it only changes the pointer
        # and the removed node is garbage collected by python
        """

        node.prev.next = node.next
        node.next.prev = node.prev

    def bring_to_front(self, node):
        """
        :param node: Key, Value pair
                     Object of Node class

        This function moves the specified node from its current position to the front of the doubly linked list
        indicating that its the Most Recently Used element/node in the Cache.

        # Complexity:
        # Time Complexity => O(1)
        # Space Complexity => O(1) as it creates only one temporary node
        """

        temp = self.head.next
        node.next = temp
        temp.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key):
        """
        :param key: The key for which we want to know the corresponding value.
        :return: True, Value : if the key is present in the Cache
                 False, None : if the key is not present in the Cache

        This function retrieves the value for a key from the Cache, if it is present.

        # Complexity:
        # Time Complexity => O(1)
        # Space Complexity => O(1)
        # This entire operation is constant time
        """

        if key in self.dictionary:
            node_to_get = self.dictionary[key]
            # O(1) operation
            self.remove_node(node_to_get)
            # O(1) operation
            self.bring_to_front(node_to_get)
            return True, node_to_get.val
        return False, None

    def put(self, key, value):
        """
        :param key: The key to insert in Cache
        :param value: The value corresponding to the key to insert in the Cache

        This function adds the key, value pair as a Node in the Cache.
        # Time Complexity => O(1)
        # space Complexity => O(1)
        """
        # O(1) operation ==> checking in dictionary
        if key in self.dictionary:
            # O(1) operation in terms of time and space
            self.remove_node(self.dictionary[key])
        node_to_add = Node(key, value)
        self.dictionary[key] = node_to_add
        # O(1) operation
        self.bring_to_front(node_to_add)
        # O(1) operation
        if len(self.dictionary) > self.capacity:
            # O(1) operation
            self.remove_node(self.tail.prev)
            # O(1) operation
            del self.dictionary[self.tail.prev.key]

    def display(self):
        """
        This function displays the contents of the LRU Cache in order.
        Starting from Most recently used element to the Least recently used element in top-down order.
        Complexity =>
        Space Complexity => O(1)
        Time Complexity => printing all nodes in LRU cache
                           no of nodes = Max nodes => capacity of LRU Cache
                           if k refers to MAX_CAPACITY
                           => O(k)
        """
        i = self.head.next
        while i != self.tail:
            print("(", i.key, "->", i.val, ")")
            i = i.next

