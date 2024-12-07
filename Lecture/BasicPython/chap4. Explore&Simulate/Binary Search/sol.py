from util.importer import Importer, get_current_path
from util.text_cleaner import spi
from typing import TextIO, List


def get_starting_values(file_stream: TextIO):
    N, M = spi(file_stream.readline())
    arr = spi(file_stream.readline())
    return [N, M, arr]


def get_ending_values(file_stream: TextIO):
    ans = list(map(int, file_stream.readline().replace("\n", "").split(" ")))
    return ans


def solve_problem(N: int, M: int, arr: List[List[int]]):
    """ 4-1 """

    return arr


if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1, 5)
