import os

IN = "in"
OUT = "out"


INPUT = 0
EXPECTED_VALUE = 1


class Importer:
    def __init__(self, path, show):
        self.path = path
        self.show = show
        self.file_map = self._get_file_map(self._get_file_list())

        self.initial = None
        self.ans = None
        self.solve = None

    def set_all(self, initial, ans, solve):
        self.initial = initial
        self.ans = ans
        self.solve = solve

    def print_total(self):
        print(f"total Size -> {len(self.file_map)}")

    def start(self, start, end=None):
        # file_map = self._get_file_map(self._get_file_list())
        if end is None:
            end = start

        sliced_map = self.file_map[start-1:end]
        for i, se in enumerate(sliced_map):
            s = se[INPUT]
            e = se[EXPECTED_VALUE]

            with open(s, "rt", encoding='utf-8') as f:
                init_values = self.initial(f)

            # 문제풀이
            my_answer = self.solve(*init_values)

            with open(e, "rt", encoding='utf-8') as f:
                expected_answer = self.ans(f)

            if self.show:
                print(f"======== {i+1} check ============")
                print(my_answer)
                print(expected_answer)
                print("===============================\n")

    def _get_file_map(self, file_list):
        # file_list = self._get_file_list()
        file_map = []
        for i in range(len(file_list)):
            name = file_list[i].replace(".txt", "")
            number = ''.join(filter(str.isdigit, name))

            if not name.find("out") == -1:
                continue

            s = f"{name}.txt"
            e = f"out{number}.txt"
            for n in file_list:
                if e == n:
                    file_map.append([s, e])
                    break
        return file_map

    def _get_file_list(self):
        if os.path.exists(self.path):
            file_list = [f_name for f_name in os.listdir(self.path) if not f_name.find(".txt") == -1]
            return file_list
        else:
            raise Exception("경로가 존재하지 않습니다.")

    def hi(self):
        print(self.path)


def get_current_path(file):
    current_path = os.path.dirname(os.path.realpath(file))
    return current_path
