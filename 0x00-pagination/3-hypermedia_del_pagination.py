#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


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

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict:
        """
        get the page of the dataset with remove hypermedia pagination
        """
        assert isinstance(index, int) and index >= 0, \
            "Index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        indexed_dataset = self.indexed_dataset()
        max_index = len(indexed_dataset) - 1
        if index > max_index:
            raise AssertionError("Index out of range")

        data = []
        next_index = index
        while len(data) < page_size and next_index <= max_index:
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
            if next_index <= max_index else None,
        }


if __name__ == "__main__":
    # Task 3
    server = Server()

    server.indexed_dataset()

    try:
        server.get_hyper_index(300000, 100)
    except AssertionError:
        print("AssertionError raised when out of range")

    index = 3
    page_size = 2

    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server._Server__indexed_dataset[res.get('index')]
    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 4- request agaian initial index -> the first data is not last one
    print(server.get_hyper_index(index, page_size))

    # 5- request again initial next index -> same data page as the request 2-
    print(server.get_hyper_index(res.get('next_index'), page_size))
