s = input()
res = ""

start = None
for index, sym in enumerate(s):
    if sym == "(":
        start = index + 1
    elif sym == ")":
        res += "".join(reversed(s[start:index]))
        start = None
    elif start is None:
        res += sym

print(res)
