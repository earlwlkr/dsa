# LettersGrid

Source screenshots:

- [letters-grid-1.png](letters-grid-1.png)
- [letters-grid-2.png](letters-grid-2.png)

Find an optimal path to create a word using letters from a 2D array.

## Description

You are given a string `S` and a two-dimensional array of characters of size `N x N` named `grid`. Each field in the grid is either empty, denoted by a dot (`.`), or contains an uppercase English letter. Each particular letter may appear at most twice in the grid.

Your task is to reconstruct string `S` by visiting fields of the grid. You start the reconstruction with an empty string. You can choose the field in which you want to start.

In one move, you can change the current field to an adjacent one: up, down, left, or right. If you visit a field containing a letter, you may append this letter to the end of the reconstructed string. Appending a letter is not counted as a move. Each field can be visited and each letter can be used multiple times during the reconstruction process.

What is the minimum number of moves needed to reconstruct string `S`?

Write a function:

```python
def solution(S, grid):
    pass
```

that, given a string `S` and an array `grid`, returns the minimum number of moves needed to reconstruct `S`. If it is not possible to reconstruct `S`, return `-1`.

## Examples

### Example 1

Given:

```text
S = "ABCA"
grid = [".A.C", "B...", "....", "...A"]
```

The function should return:

```text
6
```

The optimal movement during the reconstruction process is:

- Start on the field containing `A` in the first row.
- Go to the adjacent field with `B` in one move.
- Go to the field containing `C` in three moves.
- Return to the starting field with `A` in two moves.

## Assumptions

Assume that:

- The length of string `S` is within the range `[1..10]`.
- String `S` is made only of uppercase letters `A-Z`.
- `N` is an integer within the range `[1..20]`.
- All strings in `grid` are made only of uppercase English letters and/or `.` characters.
- Each letter may appear at most twice in the grid.

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
