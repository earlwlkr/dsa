def solution(A):
    count = {}
    result = []
    for num in A:
        current = 0
        for j in range(1, num + 1):
            if num % j == 0 and j in count:
                current += count[j]

        count[num] = count.get(num, 0) + 1
        result.append(current)

    return result


if __name__ == "__main__":
    print(solution([2, 4, 3, 6]))  # [0, 1, 0, 2]
    print(solution([8, 4, 2]))  # [0, 0, 0]
    print(solution([7, 8, 7, 8, 8]))  # [0, 0, 1, 1, 2]
    print(solution([8, 1, 3, 7, 21, 2, 14]))  # [0, 0, 1, 1, 3, 1, 3]
