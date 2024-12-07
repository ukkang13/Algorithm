def show_list(arr, meta=None):
    link = "======" if meta is None else meta
    print("========= ", link, " =========")
    for line in arr:
        print(line)
    print("========= ", "=====", " =========")
