import sys
from functools import reduce


def permute(arr, prefix=[]):
    if len(arr) == 1:
        yield prefix + arr
    for i, el in enumerate(arr):
        remainder = arr[:i]+arr[i+1:]
        yield from permute(remainder, prefix + [el])

def word_value(word, d):
    l = len(word)
    res = 0
    for i, letter in enumerate(word):
        p = l - i - 1
        res += d[letter] * 10 ** p
    return res

def get_dict(permutation):
    keys = ['k', 'e', 'r', 's', 't', 'n', 'm', 'i', 'l', '-']
    dict = {}
    for i, v in enumerate(permutation):
        dict[keys[i]] = v
    return dict


def main():
    vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    min_diff = sys.maxsize
    dictionaries = []
    for p in permute(vals):
        d = get_dict(p)
        left = word_value("kerst", d)
        right = word_value("rekenen", d) + word_value("met", d) * word_value("tien", d) - word_value("letters", d)
        diff = abs(left - right)
        if diff <= min_diff:
            min_diff = diff
            if diff == 0:
                dictionaries.append(d)
    if min_diff == 0:
        print(dictionaries)
        minstreel = word_value("minstreel", dictionaries[0])
        print("minstreel: %d" % minstreel)
        rekenlessen = []
        for d in dictionaries:
            rekenles = word_value("rekenles", d)
            rekenlessen.append(rekenles)
            print("rekenles: %d" % rekenles)
        print("product: %d" % reduce(lambda x, y: x*y, rekenlessen))

if __name__ == "__main__":
    main()