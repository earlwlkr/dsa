# Rehabilitation

Source screenshot: [rehabilitation.png](rehabilitation.png)

Find the minimum cost of rehabilitation that consists of a specific number of sessions.

## Description

A patient needs rehabilitation within the next `N` days, numbered from `0` to `N - 1`.

The rehabilitation consists of `X` sessions. For every rehabilitation session other than the last one, the next session is exactly `Y` days later.

You are given an array `A` of `N` integers listing the costs of the individual rehabilitation sessions on the `N` days: rehabilitation on the `K`-th day costs `A[K]`.

Write a function:

```python
def solution(A, X, Y):
    pass
```

that, given array `A` and two integers `X` and `Y`, returns the minimum total cost of rehabilitation.

It is guaranteed that it is always possible to complete all `X` rehabilitation sessions.

## Examples

1. Given `A = [4, 2, 3, 7]`, `X = 2`, and `Y = 2`, the function should return `7`, which is the sum of the costs on days `0` and `2`: `7 = 4 + 3`.
2. Given `A = [10, 3, 4, 7]`, `X = 2`, and `Y = 3`, the function should return `17`, since rehabilitation is possible only on days `0` and `3`: `17 = 10 + 7`.
3. Given `A = [4, 2, 5, 4, 3, 5, 1, 4, 2, 7]`, `X = 3`, and `Y = 2`, the function should return `6`, which is the sum of the costs on days `4`, `6`, and `8`: `6 = 3 + 1 + 2`.

## Assumptions

Write an efficient algorithm for the following assumptions:

- `N` and `X` are integers within the range `[2..200,000]`.
- Each element of array `A` is an integer within the range `[1..1,000]`.
- `Y` is an integer within the range `[1..199,999]`.
- `N` is higher than `(X - 1) * Y`.
