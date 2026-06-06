def solution(S):
    count = {}
    for char in S:
        count[char] = count.get(char, 0) + 1

    needed = {k for k, v in count.items() if v % 2 != 0}
    stack = []

    for char in S:
        count[char] -= 1
        if char not in needed:
            continue
        if char in stack:
            continue

        while stack and stack[-1] > char and count[stack[-1]] > 0:
            stack.pop()

        stack.append(char)

    return "".join(stack)


print(solution("CBCAAXA"))  # BAX
print(solution("ABACCXC"))  # BCX
print(solution("ZYXZYZY"))  # XYZ
print(solution("XXZYXZYZY"))  # XYZ
print(solution("ABBBCCC"))  # ABC
print(solution("ABCBACDDAA"))  #
print(solution("AKFKFMOGKFB"))  # AFKMOGB
