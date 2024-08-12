def solve(s):
    res, opened = [], 0
    for c in s:
        if c == "(" and opened > 0:
            res.append(c)
            print(res)
        if c == ")" and opened > 1:
            res.append(c)
            print(res)

        if c == "(":
            opened += 1
        else:
            opened -= 1
    return "".join(res)


if __name__ == "__main__":
    arr = "(()())(())"
    print(solve(arr))

# Time Complexity =
# Space Complexity =
