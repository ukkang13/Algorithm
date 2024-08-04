from util.importer import Importer, get_current_path
from typing import TextIO, List


def get_starting_values(file_stream: TextIO):
    arr1_length = int(file_stream.readline().replace("\n", ""))
    arr1 = list(map(int, file_stream.readline().replace("\n", "").strip().split(" ")))
    arr2_length = int(file_stream.readline().replace("\n", ""))
    arr2 = list(map(int, file_stream.readline().replace("\n", "").strip().split(" ")))
    return [arr1_length, arr1, arr2_length, arr2]


def get_ending_values(file_stream: TextIO):
    ans = list(map(int, file_stream.readline().replace("\n", "").split(" ")))
    return ans


def solve_problem(arr1_length: int, arr1: List[int], arr2_length: int, arr2: List[int]):
    """ 3-4 """
    # 1 ~ 100 사이 숫자 왔다갔다 하면서 넣으면 됌.
    idx2 = 0
    result = []
    flag = False
    for idx, ele1 in enumerate(arr1):
        while ele1 > arr2[idx2]:
            result.append(arr2[idx2])
            idx2 += 1
            if idx2 == arr2_length:
                break
        if flag:
            result.extend(arr1[idx:])
            break
        else:
            result.append(ele1)

    if idx2 < arr2_length:
        result.extend(arr2[idx2:])
    return result


def solve_problem2(arr1_length: int, arr1: List[int], arr2_length: int, arr2: List[int]):
    p1 = p2 = 0
    result = []
    while p1 < arr1_length and p2 < arr2_length:
        if arr1[p1] <= arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1
    if p1 < arr1_length:
        result += arr1[p1:]
    elif p2 < arr2_length:
        result += arr2[p2:]
    return result


if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem2)
    importer.print_total()
    importer.start(1, 5)
