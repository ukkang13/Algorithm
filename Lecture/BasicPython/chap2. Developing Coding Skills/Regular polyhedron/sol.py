from util.importer import Importer, get_current_path
from typing import TextIO


def get_starting_values(file_stream: TextIO):
    polyhedron_types = tuple(map(int, file_stream.readline().replace("\n", "").split(" ")))
    return polyhedron_types


def get_ending_values(file_stream: TextIO):
    ans = list(map(int, (file_stream.readline()).replace("\n", "").split(" ")))
    return ans


def solve_problem(N, M):
    """ 2-5 """
    if N >= M:
        up = N
        down = M
    else:
        up = M
        down = N

    rst = [0 for _ in range(N+M)]
    for n1 in range(up):
        for n2 in range(down):
            rst[n1+n2] += 1

    ans = []
    m_cnt = -1
    for i, cnt in enumerate(rst):
        if cnt > m_cnt:
            ans.clear()
            m_cnt = cnt
            ans.append(i+2)
        elif cnt == m_cnt:
            ans.append(i+2)

    print(rst)
    return ans


if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1, 5)
