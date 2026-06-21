def solution(nums):
    count = 1
    dict = {}

    for i, num in enumerate(nums):
        numStr = str(num)
        for char in numStr:
            if char in dict:
                dict[char].append(i)
            else:
                dict[char] = [i]

    print(dict)
    return count


if __name__ == "__main__":
    print(solution([50, 30, 15, 51, 10, 20, 15]))  # 5
    print(solution([11, 33, 55]))  # 1
