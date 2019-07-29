def check_brackets(str):
    stack = []
    bracket_dict = {'(': ')', '{': '}', '[': ']'}

    for i, el in enumerate(str):
        if el in bracket_dict.keys():
            stack.append((i, el))
        else:
            if el in bracket_dict.values():
                if len(stack) == 0:
                    return i+1
                _, top = stack.pop()
                if bracket_dict[top] != el:
                    return i+1
    if len(stack):
        i, _ = stack.pop()
        return i + 1
    else:
        return "Success"



