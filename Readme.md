# LRUCache Library

This library implements the LRU - Least Recently Used Cache, which stores only the elements which are accessed the most frequently and evicts/removes the least recently used elements from the cache. Cache has a maximum capacity specified by the user – the maximum elements it can store at any time.

## Introduction
LRUCache is written in Python 3.7.
The cache is implemented by a Doubly Linked List data structure.
The contents of the cache at any given time is maintained by a dictionary which stores Key, Node pair where Node = (key, value).
The LRU cache is a dictionary of keys and double linked nodes. The dictionary makes the time of get() to be O(1). The list of double linked nodes make the nodes put() and remove_node() operations O(1). 
Since, the size of the LRU cache(dictionary and node list) can go upto maximum capacity of LRU cache, thus the space complexity of LRU cache in worst case is O(max_capacity)

Main operations of LRUCache include:

**1.	get (key):**
* If the key is present in the cache
  * Returns True, Value
* If the key is not in the cache
 	* Returns False, None
* **Complexity:**
 	* Time Complexity: O(1)
  * Space Complexity: O(1)

**2.	put (key, value):** Takes a key, value pair to add it to the cache.
It takes into consideration following conditions:
* If capacity of cache is full:
  * Removes least recently used element/node from cache
  * Inserts this new element in cache
  * This new element is the most recently used element in cache
* If key is already present in the cache:
  * Deletes that node from cache
  * Creates new node with the key and its new value
  * Inserts this new node in front
* If none of the above conditions is true:
  * Creates a new node with the given key and value
  * Inserts this node at the front
* **Complexity:**
 	* Time Complexity: O(1)
  * Space Complexity: O(1)

Other functions include:

**3.	remove_node(node):** Removes specified element/node from LRU cache
   * **Complexity:**
  	  * Time Complexity: O(1)
     * Space Complexity: O(1)

**4.	bring_to_front(node):** Places node at the start of the doubly linked list indicating most recently used element(node)
   * **Complexity:**
  	  * Time Complexity: O(1)
     * Space Complexity: O(1)
     
**5. display() :** Displays the contents of the LRU Cache in order. Starting from Most recently used element to the Least recently used element in top-down order. Displays in format: (key -> value)
   * **Complexity:**
  	  * Time Complexity: O(1)
     * Space Complexity: O(k) where k = capacity of the LRU cache

## Requirements
* Python 3.7

* xmlrunner will be required for running the test cases.
```
import xmlrunner
```

## Usage
You can use the library by following:
```
from Prachi_LRU import LRUCache
from Prachi_LRU import Node
```
or 

You can copy paste the entire code from Prachi_LRU and paste it in your file to access the functionalities of the LRUCache.
For the code, you can go to Prachi_LRU.py

### Accessing functionalities
**1. Create an object of the LRUCache** specifying the maximum capacity of the LRU cache - max elements at any given time that the cache can contain.

  * The following command will create a LRU cache of capacity 5
```
cache1 = LRUCache(5)
```
**2. Inserting elements in the cache**
  * The following inserts the specified key, value pair in the cache by creating a Node. 
```
cache1.put(5,10)
cache1.put(1,2)
cache1.put(6,36)
```
   * The cache will store just the key, but the value can be retrieved from the key. This is possible by the usagge of the dictionary which stores the (key, node) pair, where node is basically a (key,value) pair. 

**3. Retrieving elements from the cache**
  * The following command will return if the elements exists in the cache or not. If it exists, returns the value else returns None.
  Takes key as the argument.
```
status, value = cache1.get(5)
```
   * The result will be:
```
status = True
value = 10
```
   * What if the element does not exist:
```
status, value = cache1.get(9)
```
   * The result will be:
```
status = False
value = None
```
**4. Displaying contents of the cache**
  * The following command will display elements- just the keys in the cache in order from Most recently used at the top to the least recently used at the bottom.
  ```
  cache1.display()
  ```
  * The result will be:
  ```
  (6 -> 36)
  (1 -> 2)
  (5 -> 10)
  ```
  **5. Remove node from the cache**
   * The following command will remove any specified node from the cache.
   ```
   cache1.remove_node(1)
   ```
   * This will result in:
   ```
   (6 -> 36)
   (5 -> 10)
   ```
