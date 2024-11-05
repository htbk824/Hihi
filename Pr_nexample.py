#Array
class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def insert(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = value

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def __str__(self):
        return str(self.array)

#Linked List 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

#Queue
class Queue:
    def __init__(self):
        self.items = []  

    def enqueue(self, item):
        """Thêm phần tử vào cuối hàng đợi."""
        self.items.append(item)

    def dequeue(self):
        """Xóa và trả về phần tử ở đầu hàng đợi."""
        if not self.is_empty():
            return self.items.pop(0)  
        raise IndexError("Dequeue from an empty queue")  

    def is_empty(self):
        """Kiểm tra xem hàng đợi có rỗng hay không."""
        return len(self.items) == 0

    def peek(self):
        """Trả về phần tử ở đầu hàng đợi mà không xóa nó."""
        if not self.is_empty():
            return self.items[0]  
        raise IndexError("Peek from an empty queue")  
    def print_queue(self):
        """In ra các phần tử trong hàng đợi."""
        print("Queue:", self.items)
#Binary Tree 
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.value, end=' ')
            self.in_order_traversal(node.right)

#Binary Search Tree
class BinarySearchTree(BinaryTree):
    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)

#Bubble sỏt
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#Insertion sỏt
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#linear search
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

#binary search 
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#Hash table
'''
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        index = self.hash_function(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
                return
#4. Test Cases for Hash Table
def test_hash_table():
    ht = HashTable(10)

    # Test insertion
    ht.insert("key1", "value1")
    assert ht.get("key1") == "value1", "Test Case 1 Failed"

    # Test updating value
    ht.insert("key1", "value2")
    assert ht.get("key1") == "value2", "Test Case 2 Failed"

    # Test retrieval of non-existent key
    assert ht.get("key2") is None, "Test Case 3 Failed"

    # Test removal
    ht.remove("key1")
    assert ht.get("key1") is None, "Test Case 4 Failed"

    # Test collision resolution
    ht.insert("key1", "value1")
    ht.insert("key2", "value2")  # Assuming hash function may cause collision
    assert ht.get("key1") == "value1", "Test Case 5 Failed"
    assert ht.get("key2") == "value2", "Test Case 6 Failed"

    print("All test cases passed!")

test_hash_table()  
                '''
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # Simple hash function that maps keys to indices within the table's range
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if the key already exists and update it
        for kv in self.table[index]:
            if kv[0] == key:
                kv = (key, value)
                return
        # If key is not found, append the key-value pair to handle collisions by chaining
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        index = self.hash_function(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
                return

    def display(self):
        # Display the hash table structure for visualization
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")

def test_hash_table():
    # Create a hash table of size 5 for testing
    ht = HashTable(5)

    # Test Case 1: Insert and retrieve a key-value pair
    ht.insert("apple", "fruit")
    assert ht.get("apple") == "fruit", "Test Case 1 Failed"

    # Test Case 2: Update an existing key's value
    ht.insert("apple", "red fruit")
    assert ht.get("apple") == "red fruit", "Test Case 2 Failed"

    # Test Case 3: Retrieve a non-existent key
    assert ht.get("banana") is None, "Test Case 3 Failed"

    # Test Case 4: Remove an existing key
    ht.insert("banana", "yellow fruit")
    ht.remove("banana")
    assert ht.get("banana") is None, "Test Case 4 Failed"

    # Test Case 5: Handle collision (same index for different keys)
    # Assuming the hash function may cause collisions at the same index for these keys
    ht.insert("cat", "animal")
    ht.insert("tac", "reverse of cat")  # Possible collision if they hash to the same index
    assert ht.get("cat") == "animal", "Test Case 5 Failed"
    assert ht.get("tac") == "reverse of cat", "Test Case 6 Failed"

    # Test Case 6: Remove one item in a chain with collisions
    ht.remove("cat")
    assert ht.get("cat") is None, "Test Case 7 Failed"
    assert ht.get("tac") == "reverse of cat", "Test Case 8 Failed"

    print("All test cases passed!")

# Run the tests
test_hash_table()


#5. Performance Comparison of Sorting and Tree Traversal Algorithms
#Sorting Algorithms
import time
import random

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Performance Testing
def performance_test():
    sizes = [100, 1000, 5000, 10000]
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        # Bubble Sort
        start = time.time()
        bubble_sort(arr.copy())
        print(f"Bubble Sort {size}: {time.time() - start:.6f} seconds")

        # Merge Sort
        start = time.time()
        merge_sort(arr.copy())
        print(f"Merge Sort {size}: {time.time() - start:.6f} seconds")

        # Quick Sort
        start = time.time()
        quick_sort(arr.copy())
        print(f"Quick Sort {size}: {time.time() - start:.6f} seconds")

performance_test()

#Tree Traversal Algorithms
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Depth-First Search
def dfs(node):
    if node:
        print(node.val, end=' ')
        dfs(node.left)
        dfs(node.right)

# Breadth-First Search
def bfs(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Performance Testing for Tree Traversal
def tree_performance_test():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    start = time.time()
    dfs(root)
    print(f"\nDFS Time: {time.time() - start:.6f} seconds")

    start = time.time()
    bfs(root)
    print(f"BFS Time: {time.time() - start:.6f} seconds")

tree_performance_test()

#6. Basic Hash Functions and Collision Resolution Techniques
class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value  # Update existing key
                return
        self.table[index].append([key, value])  # New key-value pair

    def get(self, key):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        index = self.hash_function(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
                return

# Example usage
hash_table = SimpleHashTable(10)
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)

print(hash_table.get("banana"))  # Output: 2
hash_table.remove("banana")
print(hash_table.get("banana"))  # Output: None
