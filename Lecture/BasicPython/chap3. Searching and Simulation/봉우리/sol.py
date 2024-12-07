

def solve_problem():
    arr = []
    cnt = 0
    for i in range(1, len(arr)):
        for j in range(1, len(arr[i])):
            target = arr[i][j]
            left = arr[i][j-1]
            right = arr[i][j+1]
            top = arr[i-1][j]
            bottom = arr[i+1][j]

            if is_large(target, left) and is_large(target, right) \
                    and is_large(target, top) and is_large(target, bottom):
                cnt += 1




def is_large(a, b):
    if a > b:
        return True
    return False
