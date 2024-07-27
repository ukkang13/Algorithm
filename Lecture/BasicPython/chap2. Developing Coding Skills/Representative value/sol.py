from util.importer import Importer, get_current_path
from typing import TextIO


def get_starting_values(file_stream: TextIO):
    N = int(file_stream.readline().replace("\n", ""))
    scores = list(map(int, (file_stream.readline()).replace("\n", "").split(" ")))
    return N, scores


def get_ending_values(file_stream: TextIO):
    ans = list(map(int, (file_stream.readline()).replace("\n", "").split(" ")))
    return ans


def solve_problem(N, scores):
    """
    2-4
    """

    avg = sum(scores) / N
    rst = 2147000000
    idx = 2147000000
    for i, score in enumerate(scores):
        diff = abs(score - avg)
        # print(f"avg:{avg} / diff:{diff} / score:{score} / idx:{i}")
        if diff < rst:
            rst = diff
            idx = i

    return scores[idx], idx+1


if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1, 5)
