# CommonDigit

Source screenshot: [common-digit.png](common-digit.png)

Choose as many numbers as possible so that every pair has a common digit.

## Description

There is an array consisting of `N` two-digit numbers. A group of numbers can be chosen from the array if every pair of chosen numbers has at least one common digit.

For example, numbers `25` and `56` can be chosen together as they have a common digit `5`, but `11` and `22` cannot be chosen together.

What is the maximum number of array elements that can be chosen together?

Write a function:

```python
def solution(nums):
    pass
```

that, given an array `nums` made of `N` integers, returns the maximum size of the subset in which every two numbers share at least one digit.

## Examples

1. For `nums = [50, 30, 15, 51, 10, 20, 15]`, numbers `50`, `15`, `51`, `10`, and `15` can be chosen. The function should return `5`.
2. For `nums = [11, 33, 55]`, no two numbers have a common digit. The function should return `1`.

## Assumptions

- `N` is an integer within the range `[1..1,000,000]`.
- Each element of array `nums` is an integer within the range `[10..99]`.
