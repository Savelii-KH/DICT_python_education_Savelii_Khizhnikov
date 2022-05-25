import re


words = ["apple", "ap", "le", "a", ".", "apwle", "peach"]


def stage_3(word) -> str:
    k = 0
    for i in word:
        if re.match(r"[a.]|[p.]|[l.]|[e.]", i):
            k += 1
        else:
            k -= 1
    if abs(len(word)) == k:
        return "True"
    else:
        return "False"


if __name__ == "__main__":
    [print(f"Input: '{i}|apple'     Output: {stage_3(i)}") for i in words]
