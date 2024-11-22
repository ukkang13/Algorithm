from util.importer import Importer, get_current_path
from typing import TextIO, List


def get_starting_values(file_stream: TextIO):
    arr = []
    n = int(file_stream.readline().strip())
    for i in range(n):
        arr.append(list(map(int, file_stream.readline().strip().split(" "))))
    return [n, arr]


def get_ending_values(file_stream: TextIO):
    ans = file_stream.readline()
    return ans


def solve_problem(n: int, grid: List[List[int]]):
    """
    3-6
    NxN 격자판 최대값구하기
    """
    mv = -1
    # 가로줄 합 비교
    for line in grid:
        m = 0
        for ele in line:
            m += ele

        # print("sum=" + str(m) + " vs mv=" + str(mv) + " line = ", line)
        if mv < m:
            mv = m
    print()

    # 세로줄 합 비교
    for i in range(n):
        m = 0
        app = []
        for j in range(n):
            m += grid[j][i]
            app.append(grid[j][i])
        # print("sum=" + str(m) + " vs mv=" + str(mv) + " line = ", app)
        if mv < m:
            mv = m
    print()
    # 두 대각선의 합 비교
    m = 0
    m2 = 0
    for i in range(n):

        m += grid[i][i]
        m2 += grid[n-1-i][i]
    if mv < m:
        mv = m
    if mv < m2:
        mv = m2
    return mv


if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1, 5)
