def no_dups(s):
    duplicate_array = {}
    new_string = ''

    for char in s.split(" "):
        if char not in duplicate_array:
            new_string += char+" "
            duplicate_array[char] = 1
    return new_string.rstrip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
