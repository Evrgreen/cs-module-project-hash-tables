import string


punc_list = (":", ";", ",", ".", "-", "+", "=", "/", "\\",
             "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\"")


def word_count(s):
    # Your code here
    tally = {}

    for item in punc_list:
        s = s.replace(item, "")
    result = [word.lower() for word in s.split()]

    for item in result:
        tally[item] = tally[item]+1 if item in tally else 1
    return tally


if __name__ == "__main__":
    print(word_count('a a\ra\na\ta \t\r\n'))
