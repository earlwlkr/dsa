# WordGame

Count well-structured anagrams of a given word.

## Description

A couple of friends decided to play an anagram-finding word game. The point of the game is to find all the anagrams of a given word. Unfortunately, the friends are not fluent in English, so instead of finding all the English words, they decided to look for all the well-structured words.

We say that a word is well-structured if it:

- Starts with a consonant.
- Does not contain two consecutive vowels.
- Does not contain two consecutive consonants.

Assume that the letters `A`, `E`, `I`, `O`, and `U` are vowels, and that all other letters are always consonants. Note that `Y` is treated as a consonant.

For example, the following words are well-structured:

- `PUTOR`
- `RUME`
- `TABEK`
- `BABABAB`
- `BABABA`
- `YAMAR`

However, the following words are not well-structured:

- `ABAR`, because it does not start with a consonant.
- `BAAR`, because it contains two consecutive vowels.
- `KAKKE`, because it contains two consecutive consonants.
- `AARO`, because it does not start with a consonant and contains two consecutive vowels.
- `BOARD`, because it contains two consecutive vowels and two consecutive consonants.

A word does not have to be a valid English word in order to be well-structured, and there are valid English words that are not well-structured.

Count the number of well-structured words that can be obtained by rearranging the letters of the input word. Since the answer can be very large, provide it modulo `1,000,000,007` (`10^9 + 7`).

Write a function:

```python
def solution(S):
    pass
```

that, given a string `S`, returns the number of well-structured words modulo `1,000,000,007` that can be obtained by rearranging the letters of `S`.

## Examples

### Example 1

For:

```text
S = "BAR"
```

The function should return:

```text
2
```

There are two well-structured words that can be formed:

- `BAR`
- `RAB`

### Example 2

For:

```text
S = "AABB"
```

The function should return:

```text
1
```

There is only one well-structured word that can be formed:

- `BABA`

### Example 3

For:

```text
S = "AABCY"
```

The function should return:

```text
6
```

There are six well-structured words that can be formed:

- `BACAY`
- `BAYAC`
- `CABAY`
- `CAYAB`
- `YABAC`
- `YACAB`

### Example 4

For:

```text
S = "AAAB"
```

The function should return:

```text
0
```

There are no well-structured words that can be formed.

## Assumptions

Write an efficient algorithm for the following assumptions:

- `N` is an integer within the range `[1..30]`.
- String `S` is made only of uppercase letters `A-Z`.
