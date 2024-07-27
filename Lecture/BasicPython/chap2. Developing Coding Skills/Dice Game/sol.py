from util.importer import Importer, get_current_path
from typing import TextIO


def get_starting_values(file_stream: TextIO):
    N = int(file_stream.readline())
    games = []
    for i in range(N):
        dices = list(map(int, file_stream.readline().replace("\n", "").strip().split(" ")))
        games.append(dices)
    return N, games


def get_ending_values(file_stream: TextIO):
    ans = int(file_stream.readline())
    return ans


def solve_problem(N, games):
    """ 2-9 """
    rst = 0
    for dices in games:
        counter = {}
        # 같은 눈의 수 count
        for num in dices:
            alive = counter.get(num)
            if alive:
                counter[num] += 1
            else:
                counter[num] = 1

        length = len(counter.keys())
        # 같은 눈의 수가 하나라면
        if length == 1:
            val = max(counter.keys()) * 100
            if rst <= val:
                rst = val
        elif length == 2:
            # 같은 눈의 수가 2개라면
            val =1

            pass
        else:
            pass



    return rst


if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), False)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1)
