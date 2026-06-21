# ErasePairs

Create the shortest possible string by erasing pairs of identical letters in a given string.

## Description

You are given a string `S`. In one move, you can erase from `S` a pair of identical letters. Find the shortest possible string that can be created this way. If there are many such strings, choose the alphabetically, also known as lexicographically, smallest one.

There is no limit to the number of moves.

Write a function:

```python
def solution(S):
    pass
```

that, given a string `S` of length `N`, returns the shortest string, or the first alphabetically in the case of a draw, created by erasing pairs of identical letters from `S`.

## Examples

### Example 1

For:

```text
S = "CBCAAXA"
```

First erase a pair of letters `C`:

```text
CBCAAXA -> BAAXA
```

Then erase a pair of letters `A`:

```text
BAAXA -> BAX
```

Thus the string `BAX` is created. There is no way to create a shorter string. The other string of length `3` that can be created is `XBA`, but `BAX` is alphabetically first.

The function should return:

```text
"BAX"
```

### Example 2

For:

```text
S = "ZYXZYZY"
```

Two moves can be made:

```text
ZYXZYZY -> ZXZYZ -> XYZ
```

First erase a pair of letters `Y`:

```text
ZYXZYZY -> ZXZYZ
```

Then erase a pair of letters `Z`:

```text
ZXZYZ -> XYZ
```

Other strings of length `3` that can be created are `YZX`, `YXZ`, and `ZXY`, but `XYZ` is alphabetically first.

The function should return:

```text
"XYZ"
```

### Example 3

For:

```text
S = "ABCBACDDAA"
```

All five pairs of identical letters can be erased.

The function should return:

```text
""
```

### Example 4

For:

```text
S = "AKFKFMOGKFB"
```

The function should return:

```text
"AFKMOGB"
```

## Assumptions

Write an efficient algorithm for the following assumptions:

- `N` is an integer within the range `[1..100,000]`.
- String `S` is made only of uppercase letters `A-Z`.
