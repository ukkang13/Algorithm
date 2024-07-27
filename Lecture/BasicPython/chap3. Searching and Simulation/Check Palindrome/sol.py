def is_palindrome(s):
    print(s)
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return 'NO'

    return 'YES'


def test():
    """
        3-1
    """
    exam = """5\nlevel\nmoon\nabcba\nsoon\ngooG"""
    all_line = exam.split("\n")
    for s in all_line[1:]:
        rst = is_palindrome(s)
        print(rst)


if __name__ == '__main__':
    test()