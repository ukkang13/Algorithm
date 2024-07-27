from random import randint


def make_test():
    max_cnt = 100
    rg = randint(1, max_cnt)
    rst = []
    for _ in range(rg):
        tf = str(randint(0, 1))
        rst.append(tf)
    return " ".join(rst)


def hi(ex):
    """
    2-10
    """
    nums = list(map(int, ex.split(" ")))
    cnt = 1
    rst = 0
    for num in nums:
        if num > 0:
            rst += cnt
            cnt += num
        else:
            cnt = 1
    print(nums)
    print(rst)


if __name__ == '__main__':
    example = make_test()
    hi(example)