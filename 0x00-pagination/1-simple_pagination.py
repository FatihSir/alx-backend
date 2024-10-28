#!/usr/bin/env python3
"""Task 1: Simple pagination with a server class for managing baby names data.
"""


import csv
from math import ceil
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns start and end indexes for a given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """
    Server class to handle pagination of a popular baby names dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the dataset, loading it if not already cached.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of data, based on page number and page size.
        """
        assert isinstance(page, int) and isinstance(page_size, int),
        assert page > 0 and page_size > 0,

        start, end = index_range(page, page_size)
        data = self.dataset()

        # Return an empty list if start index is beyond dataset length
        if start >= len(data):
            return []

        return data[start:end]
