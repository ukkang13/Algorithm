from util.importer import Importer, get_current_path
from typing import TextIO


def get_starting_values(file_stream: TextIO):
    N = int(file_stream.readline())
    return [N]


def get_ending_values(file_stream: TextIO):
    ans = int(file_stream.readline())
    return ans


def solve_problem(N):
    """
    2-7
    """
    if N < 2:
        return 0
    elif N == 2:
        return 1

    total = [True for _ in range(N+1)]
    cnt = 0
    for i in range(2, N+1):
        if total[i] is False:
            continue

        loop = int(N/i)
        # print(f'i={i}/loop={loop}', end=' -> ')
        for j in range(2, loop+1):
            # print(i*j, end=' ')
            total[i*j] = False
        # print(i, end=' ')

    rst = 0
    for i in total[2:]:
        if i is True:
            rst += 1
    return rst


def sol2(N):
    ch = [0]*(N+1)
    cnt = 0
    for i in range(2, N+1):
        if ch[i] == 0:
            cnt += 1
            for j in range(i, N+1, i):
                ch[j] = 1
    return cnt


def sol3(N):
    """
        n 이상의 어떤 정수 x가 n의 소수가 아닌 인수라면
        x = a*b(a>0, b>0) 이다.
        즉 a,b 둘 중 하나는 root(n) 이상의 값을 갖는다.

    """
    ch = [0] * (N+1)
    for i in range(2, int(N**0.5)+1):
        if ch[i] == 0:
            for j in range(i*i, N+1, i):
                ch[j] = 1

            # for j in range(i, N+1, i):
            #     ch[j] = 1
    cnt = 0
    for i in ch:
        cnt += i
    return cnt

if __name__ == '__main__':
    importer = Importer(get_current_path(__file__), True)
    importer.set_all(get_starting_values, get_ending_values, solve_problem)
    importer.print_total()
    importer.start(1, 5)
