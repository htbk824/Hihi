import pytest
from data_structures import HashTable

class TestHashTable:
    @pytest.fixture
    def hash_table(self):
        # Create and return a HashTable instance
        ht = HashTable(10)
        return ht

    def test_insert_and_get(self, hash_table):
        # Insert a key-value pair and retrieve it
        hash_table.insert("key1", "value1")
        assert hash_table.get("key1") == "value1", "Key 'key1' should return 'value1'"

    def test_update_existing_key(self, hash_table):
        # Insert and then update the value for an existing key
        hash_table.insert("key1", "value1")
        hash_table.insert("key1", "value2")
        assert hash_table.get("key1") == "value2", "Key 'key1' should return 'value2' after update"

    def test_get_non_existent_key(self, hash_table):
        # Attempt to retrieve a key that doesn't exist
        assert hash_table.get("nonexistent") is None, "Non-existent key should return None"

    def test_remove_key(self, hash_table):
        # Remove a key and verify it no longer exists
        hash_table.insert("key1", "value1")
        hash_table.remove("key1")
        assert hash_table.get("key1") is None, "Key 'key1' should return None after removal"

    def test_collision_handling(self, hash_table):
        # Test collision resolution
        key1 = "a"  # These two keys may hash to the same bucket
        key2 = "b"  # depending on the hash function and table size
        hash_table.insert(key1, 1)
        hash_table.insert(key2, 2)
        assert hash_table.get(key1) == 1, f"Key '{key1}' should return 1"
        assert hash_table.get(key2) == 2, f"Key '{key2}' should return 2"

    def test_large_number_of_keys(self, hash_table):
        # Insert many keys and verify they are all retrievable
        for i in range(100):
            hash_table.insert(f"key{i}", i)
        for i in range(100):
            assert hash_table.get(f"key{i}") == i, f"Key 'key{i}' should return {i}"
