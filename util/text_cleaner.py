
# clean
def cl(text: str):
    return text.replace("\n", "").strip()


# split + int convert
def spi(text: str):
    t = cl(text)
    return list(map(int, t.split(" ")))