def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if stack:
                top_element = stack.pop()
            else:
                top_element = '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

isValid('(]')