# StrPrefsuf

Source screenshot: [str-prefsuf.png](str-prefsuf.png)

For a given word `S`, find the length of the longest prefix of `S` such that it is also a suffix of `S`.

## Description

A prefix of a string `S` is any leading contiguous part of `S`. A prefix is called proper if it is shorter than `S`.

A suffix of a string `S` is any trailing contiguous part of `S`. A suffix is called proper if it is shorter than `S`.

Write a function:

```python
def solution(S):
    pass
```

that, given a string `S` consisting of `N` characters, returns the length of the longest string that is both a proper prefix of `S` and a proper suffix of `S`.

## Examples

1. Given `S = "abbabba"`, the function should return `4`, because `"abba"` is both a proper prefix and a proper suffix of `S`, and it is the longest such string.
2. Given `S = "codility"`, the function should return `0`, because the empty string is the longest string that is both a proper prefix and a proper suffix.

## Assumptions

- The length of string `S` is within the range `[1..1,000,000]`.
- String `S` is made only of lowercase letters (`a-z`).
