# SameCorners

Source screenshot: [same-corners.png](same-corners.png)

Given an array, find the subarray with the largest sum in which the leftmost and rightmost elements are the same.

## Description

You are given an array `A` consisting of `N` positive integers. Consider subarrays of `A`, with at least two elements, whose first and last elements have the same value. Your task is to find the largest possible sum of such a subarray.

For example, for `A = [1, 3, 6, 1, 6, 6, 9, 9]`, the following subarrays meet the requirements:

- `[1, 3, 6, 1]`, sum `11`.
- `[6, 1, 6]`, sum `13`.
- `[6, 1, 6, 6]`, sum `19`.
- `[6, 6]`, sum `12`.
- `[9, 9]`, sum `18`.

The subarray with the largest sum is `[6, 1, 6, 6]`, and its sum is `19`.

Write a function:

```python
def solution(A):
    pass
```

that, given an array `A` of `N` positive integers, returns the largest sum of a subarray whose first and last elements have the same value. If there is no such subarray, return `-1`.

## Examples

1. Given `A = [1, 3, 6, 1, 6, 6, 9, 9]`, the function should return `19`.
2. Given `A = [5, 1, 4, 3]`, the function should return `-1`.
3. Given `A = [2, 2, 2, 3, 2, 3]`, the function should return `11`.

## Assumptions

- `N` is an integer within the range `[2..100,000]`.
- Each element of array `A` is an integer within the range `[1..10,000]`.
