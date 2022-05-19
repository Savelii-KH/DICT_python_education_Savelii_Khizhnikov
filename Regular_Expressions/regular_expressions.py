s1 = ["a", ".", "", "", "a"]
s2 = ["a", "a", "a", "", ""]
result = []
for i in range(len(s1)):
    if s2[i] == s1[i] or s1[i] == "." or s1[i] == "":
        result.append("True")
    else:
        result.append("False")
[print(f"""Input: '{s1[i]}|{s2[i]}'     Output: {result[i]}""") for i in range(len(s1))]
