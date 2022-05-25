import re


words = ["apple", ".pple", "appl.", ".....", "peach"]
if __name__ == "__main__":
    [print(f"Input: '{i}|apple'     Output: {bool(re.match(r'[a.][p.][p.][l.][e.]', i))}") for i in words]
