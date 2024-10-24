#!/usr/bin/env python3
"""
Write a function named index_range that takes
two integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    start = 0
    start += (page - 1) * page_size
    end = start + page_size
    return start, end
