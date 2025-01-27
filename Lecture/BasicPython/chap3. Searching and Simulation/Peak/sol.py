from util.importer import Importer, get_current_path
from util.text_cleaner import cl, spi
from typing import TextIO, List


def get_starting_values(file_stream: TextIO):
    arr = []
    N = int(cl(file_stream.readline()))
    for interval in file_stream:
        strs = cl(interval)
        if strs:
            num = spi(interval)
            num.append(0)
            num.insert(0, 0)
            arr.append(num)
    arr.append([0 for _ in range(N+2)])
    arr.insert(0, [0 for _ in range(N+2)])

    return [N, arr]


def get_ending_values(file_stream: TextIO):
    return cl(file_stream.readline())


def solve_problem(N: int, mountain: List[List[int]]):
    """
    3-9
    """
    dx = [0, 0 , 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 0

    for i in range(1, N):
        for j in range(1, N):
            check = [mountain[i][j] > mountain[i+dy[a]][j+dx[a]] for a in range(4)]
            # target = mountain[i][j]
            if all(check):
                cnt += 1
            # check = [mountain[i + dy[a]][j + dx[a]] for a in range(4)]
    return [cnt]


if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1)
