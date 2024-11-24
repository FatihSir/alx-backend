#!/usr/bin/python3
"""FIFO Caching Module"""


BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Initialise FIFO Caching dictionary"""
    def __init__(self):
        self.cache_data = {}
        super().__init__()

    def put(self, key, item):
        """
        A method to put item into the cache

        :param key: the key of the item
        :param item: the value of the item
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = sorted(self.cache_data)[0]
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """
        A method that gets an item from the cache using its key

        :param key: the key of the item to be accessed
        :return: the item value or None if the key does not exist
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
