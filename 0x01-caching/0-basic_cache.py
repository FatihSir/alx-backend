#!/usr/bin/python3
""" Basic dictionary """


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise (NotImplementedError
               ("put must be implemented in your cache class"))

    def get(self, key):
        """ Get an item by key
        """
        raise (NotImplementedError
               ("get must be implemented in your cache class"))


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
