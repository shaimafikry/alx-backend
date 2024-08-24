#!/usr/bin/env python3
""" pagintation"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """ use the index range func and return the data"""
        if not isinstance(page, int) or page <= 0:
            raise AssertionError
        if not isinstance(page_size, int) or page_size <= 0:
            raise AssertionError
        # use spread
        idx_st, idx_ed = index_range(page, page_size)
        data = self.dataset()
        # out of range handlig
        if idx_st > len(data):
            return []
        # slice the data using list [satrt: end]
        return data[idx_st: idx_ed]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        # page_size: the length of the returned dataset page
        # page: the current page number
        # data: the dataset page (equivalent to return from previous task)
        # next_page: number of the next page, None if no next page
        # prev_page: number of the previous page, None if no previous page
        # total_pages: the total number of pages in the dataset as an integer
        all = self.dataset()
        data = self.get_page(page, page_size)
        total_pge = math.ceil(len(all) / page_size)
        if page >= total_pge:
            nxt_pge = None
            page_size = 0
        else:
            nxt_pge = page + 1
        if page == 1:
            prv_pge = None
        else:
            prv_pge = page - 1
        return {'page_size': page_size, 'page': page,  'data': data,
                'next_page': nxt_pge, 'prev_page': prv_pge,
                'total_pages': total_pge}
