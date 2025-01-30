def check_bracket(Str):
    bracket = {")": "(", "]": "["}
    bracket_stack = []

    for w in Str:
        if w == "(" or w == "[":
            bracket_stack.append(w)
        elif w == ")" or w == "]":
            bracket_pop = bracket_stack.pop() if bracket_stack else None
            if bracket[w] != bracket_pop or bracket_pop is None:
                print("no")
                return
    if bracket_stack:
        print("no")
        return
    else:
        print("yes")
        return




while True:
    Str = input()
    if Str == ".":
        break
    check_bracket(Str)


