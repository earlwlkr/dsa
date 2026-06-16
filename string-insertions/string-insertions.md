# StringInsertions

Source screenshot: [string-insertions.png](string-insertions.png)

Insert `$` characters into a string until there is at least one `$` between every pair of repeated letters.

## Description

There is a string `S` of length `N` consisting of lowercase English letters. We are going to insert `M` `$` characters into the string in the order described by array `C`.

The `K`-th `$` character, for `K` from `0` to `M - 1`, is inserted after the `C[K]`-th letter in `S`. The `$` character is not considered a letter. For example, given `S = "aabcba"` and `C = [1, 3, 2]`, we insert three `$` characters, obtaining:

```text
"a$abcba" -> "a$abc$ba" -> "a$ab$c$ba"
```

What is the minimum number of steps after which we can stop, such that there is at least one `$` character between every two occurrences of the same letter?

In the example above, after the first insertion there are no `$` characters between the two letters `b`, but after the second insertion there is a `$` between every two occurrences of every letter, so the answer is `2`.

Write a function:

```python
def solution(S, C):
    pass
```

that, given a string `S` of length `N` and an array `C` of length `M`, returns the number of insertions after which every two occurrences of the same letter have a `$` character between them. If the condition is not met after all insertions have been made, return `-1`.

## Examples

1. Given `S = "aabcba"` and `C = [1, 3, 2]`, the function should return `2`.
2. Given `S = "aaa"` and `C = [1, 2]`, the function should return `2`.
3. Given `S = "aabcddcb"` and `C = [3, 5, 1, 4, 7]`, the function should return `3`.
4. Given `S = "wkwk"` and `C = [1]`, the function should return `-1`.
5. Given `S = "abcd"` and `C = [1, 2]`, the function should return `0`.

## Assumptions

- `N` is an integer within the range `[2..50,000]`.
- `M` is an integer within the range `[1..N-1]`.
- String `S` is made only of lowercase letters (`a-z`).
- The elements of `C` are all distinct.
