import pytest
from your_module import SimpleHashTable  # Replace `your_module` with the actual filename where SimpleHashTable is implemented.

class TestSimpleHashTable:
    @pytest.fixture
    def hash_table(self):
        # Create a SimpleHashTable instance with size 10
        return SimpleHashTable(10)

    def test_insert_and_get(self, hash_table):
        # Insert key-value pairs and test retrieval
        hash_table.insert("apple", 1)
        hash_table.insert("banana", 2)
        hash_table.insert("orange", 3)
        
        assert hash_table.get("apple") == 1, "Key 'apple' should return value 1"
        assert hash_table.get("banana") == 2, "Key 'banana' should return value 2"
        assert hash_table.get("orange") == 3, "Key 'orange' should return value 3"

    def test_update_existing_key(self, hash_table):
        # Insert and then update a key-value pair
        hash_table.insert("apple", 1)
        hash_table.insert("apple", 10)  # Update value for 'apple'
        
        assert hash_table.get("apple") == 10, "Key 'apple' should return updated value 10"

    def test_get_non_existent_key(self, hash_table):
        # Retrieve a non-existent key
        assert hash_table.get("nonexistent") is None, "Non-existent key should return None"

    def test_remove_key(self, hash_table):
        # Insert and then remove a key
        hash_table.insert("banana", 2)
        hash_table.remove("banana")
        
        assert hash_table.get("banana") is None, "Key 'banana' should return None after removal"

    def test_collision_handling(self, hash_table):
        # Test collision handling (keys hashing to the same index)
        key1 = "abc"  # Assuming both keys hash to the same index
        key2 = "bca"  # Depending on hash_function and size
        
        hash_table.insert(key1, 10)
        hash_table.insert(key2, 20)
        
        assert hash_table.get(key1) == 10, f"Key '{key1}' should return value 10"
        assert hash_table.get(key2) == 20, f"Key '{key2}' should return value 20"

    def test_large_number_of_keys(self, hash_table):
        # Insert many keys and test retrieval
        for i in range(100):
            hash_table.insert(f"key{i}", i)
        for i in range(100):
            assert hash_table.get(f"key{i}") == i, f"Key 'key{i}' should return value {i}"

