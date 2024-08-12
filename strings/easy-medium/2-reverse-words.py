def solve(s):
    words = []
    length = len(s)
    i = 0

    while i < length:
        # Skip any leading spaces
        while i < length and s[i] == " ":
            i += 1

        # Collect words
        start = i
        while i < length and s[i] != " ":
            i += 1

        if start < i:
            words.append(s[start:i])

    # Reverse the list of words and join them with a single space
    return " ".join(reversed(words))


if __name__ == "__main__":
    arr = "the sky is blue"
    print(solve(arr))

# word = arr.strip().split()            time and space for this is O(n)
#     return " ".join(word[::-1])

# Time Complexity =
# Space Complexity =
