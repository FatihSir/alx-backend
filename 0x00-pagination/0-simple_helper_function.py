#!/usr/bin/env python3
"""Helper function for pagination.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the start and end index for items on a given page.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
