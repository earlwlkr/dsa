# FindEmptyTriangle

Source screenshots:

- [find-empty-triangle-1.png](find-empty-triangle-1.png)
- [find-empty-triangle-2.png](find-empty-triangle-2.png)

Given points on a plane, find any triplet that forms a triangle that does not have any points inside.

## Description

There are `N` points on a plane, numbered from `0` to `N - 1`; the coordinates of the `K`-th point are `(X[K], Y[K])`. Find any triangle with vertices at three of the given points such that no other point lies inside this triangle and no other point, except the vertices, lies on the boundary of the triangle. The triangle must have positive area.

Write a function:

```python
def solution(X, Y):
    pass
```

that, given two arrays `X` and `Y` consisting of `N` integers each, representing points on the plane, returns an array `B` consisting of exactly three integers, such that points with indices `B[0]`, `B[1]`, and `B[2]` form an empty triangle.

If there is no such triplet, return an empty array instead.

## Examples

1. Given `X = [1, 4, 3, 2, 3]` and `Y = [4, 3, 1, 1, 2]`, there are `N = 5` points. The function could return `[0, 1, 4]`, `[0, 3, 4]`, or `[4, 2, 3]`.
2. Given `X = [0]` and `Y = [0]`, the function should return an empty array.
3. Given `X = [0, 1, 2, 4, 5, 6]` and `Y = [0, 1, 2, 3, 4, 5, 6]`, the function could return `[2, 3, 4]`.
4. Given `X = [0, 1, 3, 0, 0, 2]` and `Y = [3, 0, 0, 1, 2, 0]`, the function could return `[1, 3, 5]`.

## Assumptions

- `N` is an integer within the range `[1..300,000]`.
- Each element of arrays `X` and `Y` is an integer within the range `[0..100,000,000]`.
- Given `N` points are pairwise distinct.
