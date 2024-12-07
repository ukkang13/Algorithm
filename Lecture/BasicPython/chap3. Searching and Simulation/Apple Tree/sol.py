from util.importer import Importer, get_current_path
from typing import TextIO, List


def get_starting_values(file_stream: TextIO):
    N = int(file_stream.readline().replace("\n", ""))
    inparam = []
    for i in range(N):
        arr = list(map(int, file_stream.readline().replace("\n", "").strip().split(" ")))
        inparam.append(arr)
    return [N, inparam]


def get_ending_values(file_stream: TextIO):
    ans = int(file_stream.readline().replace("\n", ""))
    return ans

def test(size: int, matrix: List[List[int]]):
    aa = [1, 2, 3, 4]
    print(aa[1:2])

def solve_problem(size: int, matrix: List[List[int]]):
    """ 3-7 """

    print("size :: ", size)
    p = 0
    total_apples = 0
    for i in range(size):
        mid = size // 2
        line_sum = sum(matrix[i][mid-p:mid+1+p])
        # 내가 몇개를 더해야하는지 증감한다.
        total_apples += line_sum
        if i < mid:
            p += 1
        else:
            p -= 1
    return [total_apples]



if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1, 5)
