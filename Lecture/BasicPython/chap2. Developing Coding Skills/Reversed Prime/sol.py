from util.importer import Importer, get_current_path
from typing import TextIO
import math


def get_starting_values(file_stream: TextIO):
    N = int(file_stream.readline())
    nums = list(map(int, file_stream.readline().replace("\n", "").strip().split(" ")))
    return N, nums


def get_ending_values(file_stream: TextIO):
    ans = list(map(int, file_stream.readline().replace("\n", "").split(" ")))
    return ans


def solve_problem(N, nums):
    """
    2-8
    """
    rst = []
    for num in nums:
        reverse_number = reverse(num)
        if is_prime(reverse_number):
            rst.append(reverse_number)

    return rst


def reverse2(x):
    result = 0
    while x != 0:
        digit = int(math.log10(x))
        sub = x % 10
        result += (10**digit) * sub

        x = x // 10
    return result


def reverse(x):
    result = 0
    while x > 0:
        sub = x % 10
        result = result * 10 + sub

        x = x // 10
    return result


def is_prime(x):
    # 해당 수가 소수인지 판별
    for num in range(2, x):
        if x % num == 0:
            return None
    return x

if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1, 5)
