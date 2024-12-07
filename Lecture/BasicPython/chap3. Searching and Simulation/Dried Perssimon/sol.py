from util.importer import Importer, get_current_path
from util.text_cleaner import cl, spi
from util.prettier import show_list
from typing import TextIO, List


def get_starting_values(file_stream: TextIO):
    N = int(cl(file_stream.readline()))
    matrix = [spi(file_stream.readline()) for _ in range(N)]

    M = int(cl(file_stream.readline()))
    rotate = [spi(line) for line in file_stream]

    show_list(matrix, "matrix")
    show_list(rotate, "rotate")
    return [N, matrix, M, rotate]


def get_ending_values(file_stream: TextIO):
    ans = int(file_stream.readline().replace("\n", ""))
    return ans

def solve_problem(size: int, matrix: List[List[int]]):
    """ 3-8 """


    print("size :: ", size)
    return [123]



if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1, 5)
