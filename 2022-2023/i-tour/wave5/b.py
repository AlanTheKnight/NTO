s = input()

i = 0

while i < len(s):
    sym = s[i]

    if sym == "<":
        cur = sym
        while i + 1 < len(s) and s[i + 1] == "<":
            cur += s[i + 1]
            i += 1
        while i + 2 < len(s) and s[i + 1] == "-" and s[i + 2] != ">":
            cur += s[i + 1]
            i += 1
        if i + 2 == len(s) and s[i + 1] == "-":
            cur += "-"
            i += 1
        print(cur)
        i += 1

    if sym == "-":
        cur = sym
        while i + 1 < len(s) and s[i + 1] != ">":
            cur += s[i + 1]
            i += 1
        while i + 1 < len(s) and s[i + 1] == ">":
            cur += s[i + 1]
            i += 1
        print(cur)
        i += 1
