# MaxTrailingZeros

Source screenshots:

- [max-trailing-zeros-1.png](max-trailing-zeros-1.png)
- [max-trailing-zeros-2.png](max-trailing-zeros-2.png)
- [max-trailing-zeros-3.png](max-trailing-zeros-3.png)

Find a path in a given matrix of integers such that the product of all the numbers on the path has the maximum number of trailing zeros.

## Description

You are given a matrix `A` consisting of `N` rows and `M` columns. Each field of the matrix contains a positive integer.

You want to find a path consisting of neighboring fields. Two fields are neighboring if they share a common side. The path can start and end on any field and can turn left or right at most once.

The product of a path is an integer obtained by multiplying all the integers on the path. Find such a path whose product contains the maximum possible number of trailing zeros.

Write a function:

```python
def solution(A):
    pass
```

that, given a matrix of integers consisting of `N` rows and `M` columns, returns the maximum number of trailing zeros that some path with at most one turn contains.

## Examples

1. For the `3 x 3` matrix shown in the second source screenshot, the function should return `5`.
2. For the `3 x 4` matrix shown in the second source screenshot, see the screenshot for the expected result and path details.
3. For the `4 x 4` matrix shown in the third source screenshot, the function should return `2`.
4. For the `4 x 4` matrix shown in the third source screenshot, the function should return `13`.

## Assumptions

- `N` and `M` are integers within the range `[1..400]`.
- Each element of matrix `A` is an integer within the range `[1..1,000,000,000]`.
