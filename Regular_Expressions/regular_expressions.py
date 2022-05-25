import re


a = ["colou?r", "colou?r", "colou?r", "colou*r", "colou*r", "colou*r", "col.*r", "col.*r", "col.*r", "col.*r", "col.*$"]
b = ["color", "colour", "colouur", "color", "colour", "colouur", "color", "colour", "colr", "collar", "colors"]


if __name__ == "__main__":
	[print(f"Input: '{a[i]}|{b[i]}'  Output: {bool(re.match(a[i], b[i]))}") for i in range(len(a))]
