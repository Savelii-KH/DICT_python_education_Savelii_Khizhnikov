import re


w1 = ["^app", "le$", "^a", ".$", "apple$", "^apple", "^apple$", "^apple$", "^apple$", "app$", "^le"]
w2 = ["apple", "apple", "apple", "apple", "tasty apple", "apple pie", "apple", "tasty apple", "apple pie", "apple",
      "apple"]


def symbol1(word, word2) -> str:
    if re.match(word, word2[0:len(word)]):
        return "True"
    else:
        return "False"


def symbol2(word, word2) -> str:
    k = 0
    for i in reversed(word):
        if re.match(i, word2):
            k += 1
        else:
            k -= 1
    if len(word) == abs(k):
        return "True"
    else:
        return "False"


def symbol3(word, word2) -> str:
    if re.match(fr"^{word}$", word2):
        return "True"
    else:
        return "False"


def stage_4(word1, word2) -> str:
    k = []
    word = []
    for i in word1:
        if i == "^" or i == "$":
            k.append(i)
        else:
            word.append(i)
    word = "".join(word)
    if k == ["^"]:
        return symbol1(word, word2)
    elif k == ["$"]:
        return symbol2(word, word2)
    elif k == ["^", "$"]:
        return symbol3(word, word2)
    else:
        return "False"


if __name__ == "__main__":
    [print(f"Input: '{w1[i]}|{w2[i]}'       Output: {stage_4(w1[i], w2[i])}") for i in range(len(w1))]
