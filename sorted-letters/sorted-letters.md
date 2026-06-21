# SortedLetters

Given a string, remove as few letters as possible to yield a word whose letters are sorted in ascending order.

## Description

Given a word, calculate the smallest number of letters that must be removed in order for the letters of the remaining word to be sorted in lexicographical order. The resulting word need not appear in the dictionary of any particular language.

Write a function:

```python
def solution(S):
    pass
```

that, given string `S`, returns the minimum number of letters that must be removed.

For example, given `"banana"` the function should return `3`, because we can remove three letters to get the word `"aan"`, which is sorted. It is not possible to remove fewer than three letters.

## Assumptions

- The length of string `S` is within the range `[1..100,000]`.
- String `S` consists only of lower-case letters (`a-z`).
