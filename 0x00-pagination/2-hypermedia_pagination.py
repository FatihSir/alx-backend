#!/usr/bin/env python3
"""
Task 1: Simple pagination with a server class for managing baby names data.
"""

import csv
from typing import List, Tuple, Dict
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return the start and end indexes for a given page and page size.
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
        Return the dataset, loading it from the CSV file if not already cached.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data based on page number and page size.

        Returns:
            A list of lists containing the requested page data. If the page is
            out of range, an empty list is returned.
        """
        assert isinstance(page, int) and isinstance(page_size, int), (
            "page and page_size must be integers."
        )
        assert page > 0 and page_size > 0, (
            "page and page_size must be greater than 0."
        )

        start, end = index_range(page, page_size)
        data = self.dataset()

        # Return an empty list if the start index is beyond dataset length
        if start >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieve a dictionary with pagination details.

        Returns:
            A dictionary with page size, current page, dataset page,
            next and previous page numbers, and total pages.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
