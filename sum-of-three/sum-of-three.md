# SumOfThree

Choose three non-adjacent array elements with a maximum sum.

## Description

You are given an array `A` of `N` integers. Three elements of `A` are called non-adjacent if their consecutive indexes all differ by more than `1`.

For example, given `A = [8, -4, -7, -5, -5, -4, 8, 8]`:

- Elements at positions `0`, `3`, and `6` are non-adjacent and sum to `11`.
- Elements at positions `0`, `6`, and `7` sum to `24`, but are not non-adjacent.
- Elements at positions `0`, `5`, and `7` are non-adjacent and sum to `12`.

The third choice is optimal.

Write a function:

```python
def solution(A):
    pass
```

that, given an array `A` of `N` integers, returns the maximum sum of three non-adjacent elements from `A`.

## Examples

1. Given `A = [8, -4, -7, -5, -5, -4, 8, 8]`, the function should return `12`.
2. Given `A = [-2, -8, 1, 5, -8, 4, 7, 6]`, the function should return `15`.
3. Given `A = [-3, 0, -6, -7, -9, -5, -2, -6]`, the function should return `-9`.
4. Given `A = [-10, -10, -10, -10, -10]`, the function should return `-30`.

## Assumptions

- `N` is an integer within the range `[5..100,000]`.
- Each element of array `A` is an integer within the range `[-100,000,000..100,000,000]`.
