# RiceCultivation

Source screenshots:

- [rice-cultivation-1.png](rice-cultivation-1.png)
- [pattern-grid-2.png](../tricoloring/pattern-grid-2.png)

Count the maximum number of unblocked cells on a given board that can be covered by two non-intersecting stripes.

## Description

A map of a village is split into a rectangular grid with `N` rows, numbered from `0` to `N - 1`, and `M` columns, numbered from `0` to `M - 1`. Establish at most two rice cultivation areas in the village, using only cells dedicated to this purpose.

The map is described by an array of strings. The `C`-th character of the `R`-th string can be either:

- `.` meaning that the square of land in the `R`-th row and `C`-th column is a place where rice cultivation can be established.
- `#` meaning that it is an agricultural building.

The shape of each cultivation area should be a narrow rectangle: vertical with one cell width, or horizontal with one cell height. The areas cannot share cells, but can share a side.

What is the maximum number of cells that can be used for cultivation by choosing at most two areas?

Write a function:

```python
def solution(A):
    pass
```

that, given an array of strings `A`, returns the maximum number of cells that can be used for cultivation by choosing at most two areas.

## Examples

1. Given a board shown in the source screenshot, the function should return `7`.
2. Given a board shown in the source screenshot, the function should return `4`.
3. Given a board shown in the source screenshot, the function should return `7`.

## Assumptions

Write an efficient algorithm for the following assumptions:

- `N` is an integer within the range `[1..500]`.
- All strings in `A` are of the same length `M`, within the range `[1..500]`.
- All strings in `A` consist only of the characters `.` and/or `#`.
