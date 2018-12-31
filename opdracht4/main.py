def to_word(arr):
    res = ""
    for c in arr:
        res += chr(96+c)
    return res

def main():
    for x9 in range(1, 27):
        x6 = 4 + x9
        for x8 in range(1, 27):
            x5 = x8 + 4
            x3 = x5 + x6
            for x7 in range(1, 27):
                x4 = x7 + x8
                x2 = x4 + x5
                x1 = x2 + x3

                if x1 > 26:
                    break
                arr = [x1, x2, x3, x4, x5, x6, x7, x8, 4, x9]
                w = to_word(arr)
                print(w)

if __name__ == "__main__":
    main()

