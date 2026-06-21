# SquareBuilding

Find the biggest square that can be constructed from the given segments, knowing they can be merged but cannot be cut into smaller pieces.

## Description

There are `N` segments numbered from `0` to `N - 1`; the length of the `K`-th segment is `A[K]`.

Segments cannot be split into shorter segments, but can be merged to create longer ones. Merging segments of lengths `X` and `Y` creates a segment of length `X + Y`. The task is to find the largest square that can be built using those segments.

For example, with `A = [3, 3, 3, 2, 1, 1]`, we can pick three segments of length `3` and merge segments of lengths `1` and `2` to create another segment of length `3`. Having four segments of length `3`, we can build a square. One segment of length `1` remains unused.

Write a function:

```python
def solution(A):
    pass
```

that, given an array `A` consisting of `N` integers, returns the maximum possible length of the side of a square we can build. If no square can be built using the provided segments, return `0`.

## Examples

1. Given `A = [3, 3, 3, 2, 1, 1]`, the function should return `3`.
2. Given `A = [5, 4, 3, 2, 1, 10]`, the function should return `0`.
3. Given `A = [2, 3, 5, 1, 1, 6, 3, 5]`, the function should return `6`.
4. Given `A = [2, 2, 2, 2, 2, 10, 10, 10]`, the function should return `10`.

## Assumptions

- `N` is an integer within the range `[4..8]`.
- Each element of array `A` is an integer within the range `[1..100,000,000]`.

Focus on correctness; performance is not the focus of the assessment.
