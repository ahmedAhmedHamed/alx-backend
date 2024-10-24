#!/usr/bin/env python3
"""
Simple pagination
"""
from typing import Tuple
import csv
from typing import List
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    start = 0
    start += (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start, end = index_range(page, page_size)
        if end > len(self.dataset()):
            end = len(self.dataset()) - 1
        if start > end:
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        returns a dictionary containing page and metadata
        """
        ret = {}
        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        ret['page_size'] = len(data)
        ret['page'] = page
        ret['data'] = data
        if end >= len(self.dataset()) - 1:
            ret['next_page'] = None
        else:
            ret['next_page'] = page + 1
        if page > 1:
            ret['prev_page'] = page - 1
        else:
            ret['prev_page'] = None
        ret['total_pages'] = math.ceil(len(self.dataset()) / page_size)
        return ret
