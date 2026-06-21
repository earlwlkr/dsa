# RectangleLabyrinth

Given a list of coordinates of rectangular obstacles placed on a board, find the shortest path from the bottom-left to the top-right corner of the board.

## Description

There is a rectangular board with `R` rectangular obstacles placed on it. The board consists of `N x M` square cells; the bottom-left corner of the board is cell `(0, 0)`, and the top-right cell has coordinates `(N - 1, M - 1)`.

Each obstacle is described by the coordinates of its bottom-left and top-right corners. In other words, the obstacle described by coordinates `(X1, Y1) - (X2, Y2)` blocks all cells with coordinates `(x, y)` such that `X1 <= x <= X2` and `Y1 <= y <= Y2`.

Obstacles may intersect with each other.

You can move from a cell to any other cell with which it shares a side, as long as the destination is not blocked by an obstacle and is not outside the bounds of the board.

Write a function:

```python
def solution(N, M, X1, Y1, X2, Y2):
    pass
```

that returns the minimum number of steps required to move from cell `(0, 0)` to cell `(N - 1, M - 1)`. The `K`-th obstacle is described by `(X1[K], Y1[K]) - (X2[K], Y2[K])`. If it is not possible to move from the bottom-left to the top-right corner, return `-1`.

## Examples

1. Given `N = 6`, `M = 4`, `X1 = [2, 1, 4]`, `Y1 = [0, 1, 3]`, `X2 = [2, 3, 4]`, and `Y2 = [2, 1, 3]`, the function should return `10`.
2. Given `N = 5`, `M = 5`, `X1 = [0, 3]`, `Y1 = [2, 0]`, `X2 = [2, 4]`, and `Y2 = [4, 1]`, the function should return `-1`.
3. Given `N = 7`, `M = 9`, and the obstacle arrays shown in the second source screenshot, the function should return `16`.
