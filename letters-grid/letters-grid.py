def solution(S, grid):
    positions = {}
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == ".":
                continue
            if char in positions:
                positions[char].append((i, j))
            else:
                positions[char] = [(i, j)]

    # dp maps current position to minimum cost after forming prefix up to current char
    dp = {}

    # Starting on any occurrence of the first character costs 0 moves
    for pos in positions[S[0]]:
        dp[pos] = 0

    for char in S[1:]:
        new_dp = {}
        for pos in positions[char]:
            best = float("inf")
            for prev_pos, cost in dp.items():
                best = min(best, cost + distance(prev_pos, pos))
            new_dp[pos] = best
        dp = new_dp

    return min(dp.values())


def distance(fr, to):
    return abs(fr[0] - to[0]) + abs(fr[1] - to[1]) - 1


if __name__ == "__main__":
    print(solution("ABCA", [".A.C", "B...", "....", "...A"]))  # 6
# .A.C
# B...
# ....
# ...A
