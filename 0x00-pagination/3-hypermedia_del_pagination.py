#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        returns a dictionary containing page and metadata
        using an index, deletion resistant.
        """
        ret = {}
        full_data = self.indexed_dataset()
        count_done = 0
        end_of_dataset = max(full_data.keys())
        data = []
        given_idx = index
        assert index <= end_of_dataset

        while count_done < page_size and index < end_of_dataset:
            if full_data.get(index) is None:
                index += 1
                continue
            data.append(full_data.get(index))
            count_done += 1
            index += 1
        ret['index'] = given_idx
        ret['data'] = data
        ret['page_size'] = len(data)
        if index > end_of_dataset:
            ret['next_index'] = None
        else:
            ret['next_index'] = index
        return ret
