# TwoSquareSolarPanels

Source screenshots:

- [two-square-solar-panels-1.png](two-square-solar-panels-1.png)
- [two-square-solar-panels-2.png](two-square-solar-panels-2.png)

Find the biggest square that appears twice on a given map.

## Description

We have a map of an area where two square solar power plants are planned to be built. The map is given as a rectangular matrix `A` of boolean values. `A[R][C]` is `True` if a place in the `R`-th row and `C`-th column can be covered by a solar power plant, and `False` otherwise.

Each solar power plant must be built in a square shape. A single cell is sufficient for a valid solar power plant. Solar power plants cannot share any cell and should be of the same size.

The task is to find the area of each of the two biggest solar power plants that can be built.

Write a function:

```python
def solution(A):
    pass
```

that, given a matrix `A` consisting of `N` rows and `M` columns, returns the area of the largest possible solar power plants that can be built in a square shape. If no two square solar power plants can be built, return `0`.

## Examples

1. For the `4 x 4` map shown in the first source screenshot, the function should return `4`.
2. For the `6 x 4` all-available map shown in the second source screenshot, the function should return `9`.
3. For the `3 x 5` map shown in the second source screenshot, the function should return `0`.
