from util.importer import Importer, get_current_path
from typing import TextIO, List


def get_starting_values(file_stream: TextIO):
    arr = []
    for interval in file_stream:
        strs = interval.replace("\n", "")
        if strs:
            num = list(map(int, interval.replace("\n", "").split(" ")))
            arr.append(num)
    return [arr]


def get_ending_values(file_stream: TextIO):
    ans = list(map(int, file_stream.readline().replace("\n", "").split(" ")))
    return ans


def solve_problem(interval_arr: List[List[int]]):
    """
     3-5
    """
    original_list = [i+1 for i in range(20)]

    return original_list


if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1, 5)
