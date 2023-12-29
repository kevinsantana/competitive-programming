def solve(s: str):
    if len(s) % 2:
        return False
    stack = list(s)

    for b in stack:
        if b == "(":
            stack.pop()
            if not ")" in s[stack.index(b) + 1 :]:
                return False
        elif b == "[":
            stack.pop()
            if not "]" in s[stack.index(b) + 1 :]:
                return False
        elif b == "{":
            stack.pop()
            if not "}" in s[stack.index(b) + 1 :]:
                return False
        else:
            stack.append(b)
    return True
