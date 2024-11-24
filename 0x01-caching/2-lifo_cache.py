#!/usr/bin/python3
"""LIFO Caching Module"""


BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ Initializing LIFO Caching Module """
    recent = None

    def __init__(self):
        """"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        A method to put item into the cache using LIFO Caching Policy

        :param key: key of the item to be stored
        :param item: item to be stored

        """
        if key and item:
            if key not in self.cache_data.keys():
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                        and LIFOCache.recent:
                    self.cache_data.pop(LIFOCache.recent)
                    print("DISCARD: {}".format(LIFOCache.recent))
                    self.cache_data[key] = item
                    LIFOCache.recent = key
                else:
                    self.cache_data[key] = item
                    LIFOCache.recent = key
            else:
                self.cache_data[key] = item
                LIFOCache.recent = key

    def get(self, key):
        """
        A method to get item from the cache using LIFO Caching Policy
        :param key: the key of the item to be returned

        :return: item from the cache
        """
        return self.cache_data.get(key, None)
