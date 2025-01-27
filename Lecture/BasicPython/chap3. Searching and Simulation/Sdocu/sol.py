from util.importer import Importer, get_current_path
from util.text_cleaner import spi, cl
from typing import TextIO, List


def get_starting_values(file_stream: TextIO):
    arr = []
    for stream in file_stream:
        val = spi(stream)
        if val:
            arr.append(val)
    return [arr]


def get_ending_values(file_stream: TextIO):
    return cl(file_stream.readline())

def solve_problem(matrix: List[List[int]]):
    """
    3-10
    """
    N = len(matrix)

    try:
        for i in range(N):
            for j in range(N):
                target = matrix[i][j]
                path = [i for i in range(1, 10)]
                try:
                    t = path[target - 1]
                    if t == 0:
                        raise IndexError
                    path[target - 1] = 0
                except IndexError:
                    raise InterruptedError
    except InterruptedError:
        return "NO"
    return "YES"


    # 모든 가로둘 세로줄 1 ~ 9 까지 확인

    # 3x3 1~9 확인

    # 대각선 1~9 까지 확인

    return [1]


if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1)
