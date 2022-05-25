import re


if __name__ == "__main__":
	while True:
		c = input("Regular • ")
		d = input("Input • ")
		if c == "exit":
			break
		elif d == "exit":
			break
		else:
			print(f"Input: '{c}|{d}'  Output: {bool(re.findall(c, d))}")
