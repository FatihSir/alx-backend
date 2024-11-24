#!/usr/bin/python3
""" Basic dictionary """


from main import BaseCaching


class BasicCache(BaseCaching):
    """ Basic dictionary class"""
    def put(self, key, item):
        """
        A method that assign to the dictionary self.cache_data
        the item value for the key

        :param key: the key of the item to be assigned
        :param item: the item to be assigned
        """
        if key and item:
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
