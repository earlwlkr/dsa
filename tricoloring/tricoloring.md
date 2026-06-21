# Tricoloring

Divide an array into three parts with equal sums.

## Description

An array `A` consisting of `N` integers is given. A tricoloring of this array is a string consisting of `N` characters such that each character is either `R`, `G`, or `B`. The `K`-th character denotes the color of the `K`-th element of the array.

A tricoloring is stable if the sum of red elements is equal to the sum of green elements and to the sum of blue elements. A tricoloring does not necessarily use all three colors. The sum of elements of a color that is not used is assumed to be `0`.

Write a function:

```python
def solution(A):
    pass
```

that, given an array `A` consisting of `N` integers, returns any stable tricoloring of this array. Return the string `"impossible"` if no stable tricoloring exists.

## Examples

1. Given `A = [3, 7, 2, 5, 4]`, the function may return `"RGBBR"`, because `A[0] + A[4] = 7`, `A[1] = 7`, and `A[2] + A[3] = 7`.
2. Given `A = [3, 6, 9]`, the function should return `"impossible"`.

## Assumptions

- `N` is an integer within the range `[0..18]`.
- Each element of array `A` is an integer within the range `[-100,000,000..100,000,000]`.
