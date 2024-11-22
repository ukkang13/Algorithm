from util.importer import Importer, get_current_path
from util.text_cleaner import spi
from typing import TextIO, List


def get_starting_values(file_stream: TextIO):
    N, M = spi(file_stream.readline())
    arr = spi(file_stream.readline())
    return [N, M, arr]


def get_ending_values(file_stream: TextIO):
    ans = list(map(int, file_stream.readline().replace("\n", "").split(" ")))
    return ans


def solve_problem(N: int, M: int, arr: List[List[int]]):
    """ 3-5 """
    """
    목표값 M
    수열의 길이 N
    실제 arr -> arr
    """
    result = 0
    # print(arr)
    for l in range(1, N+1):
        # print("길이 -->", l)
        s = 0
        e = l
        while e <= N:
            tmp = sum(arr[s:e])
            # print("partial -> ", arr[s:e], end=' ')
            # print(" --> ", tmp)
            # print()
            if tmp == M:
                result += 1
            e += 1
            s += 1
            if e == N:
                break
        # print("\n")
    print(result)
    return arr


def solve_problem2(n: int, m: int, arr: List[int]):
    lt = rt = result = 0
    tot = arr[lt]
    print(f"start rt={rt} / lt={lt} / result={result}")
    print(f"m={m} / n={n}")
    while rt < n:
        if tot < m:
            rt += 1
            if rt == n:
                break
            tot += arr[rt]
        elif tot == m:
            result += 1
            lt += 1
            tot -= arr[lt]
        else:
            lt += 1
            tot -= arr[lt]
    print(result)


def solve_problem3(n: int, m: int, arr: List[int]):
    result = lt = rt = 0
    tot = arr[lt]
    while True:
        if tot < m:
            rt += 1
            if rt == n:
                break
            tot += arr[rt]
        elif tot == m:
            result += 1
            tot -= arr[lt]
            lt += 1
        else:
            tot -= arr[lt]
            lt += 1
    return result



def solve_problem4(n: int, m: int, arr: List[int]):
    result = lt = rt = 0
    tot = arr[lt]
    print(arr)
    while True:
        if tot < m:
            rt += 1
            if rt == n:
                break
            tot += arr[rt]
        elif tot == m:
            result += 1





    return result















"""
1차원 리스트를 탐색할 때
연속적인 값을 그룹핑할 때
해아 값에 대한 속성을 찾을 때 
인덱스 i 부터 j 까지의 합이 m인 경우의 수를 찾으시오
 -> 지렁이처럼 탐색하겠다? 이생각이 날까?
-> 아니..  [1, 3, 5, 6,7,] 
1, 12, 123, 1234,12345
2, 23,234,2345
3, 34,345
4, 45
5 전체 길이를 n이라 했을 때, n + n -1 + n-2 + n-3 ... + n-(n-1) 
1 ~ n-1 까지 더하기 -> 가우스 공식
 -> n * (n-1) / 2 + n*n -> O(n^2) 라는 의미
 
-> 모든 수를 탐색하기엔 너무 숫자가 많다. 줄일 방법은?
 -> 하나하나 더해가다가 목표 숫자를 넘기면 멈춰. 
-> 다음 인덱스에서 시작해
 -> 딱 맞다? 더 더해봤자 의미 없다.
  -> 다음 인덱스에서 시작해
-> 너무 작다? 더 더해봐.
 -> 오른쪽 다음 인덱스에서 시작해.
"""


if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem4)
    importer.print_total()
    importer.start(1, 5)
