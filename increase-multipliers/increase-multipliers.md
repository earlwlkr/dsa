# IncreaseMultipliers

For every element of an array of integers, calculate the number of preceding elements that are its divisors.

## Description

You are given an array `A` containing `N` integers. For every element in the array, calculate how many elements preceding it are its divisors.

For example, given `A = [2, 4, 3, 6]`, the number of divisors preceding each element is as follows:

- `0`: There are no elements before `A[0] = 2`; hence there are `0` divisors.
- `1`: The only element before `A[1] = 4` is `A[0] = 2`, which is its divisor.
- `0`: None of the elements before `A[2] = 3` are its divisors.
- `2`: Elements `A[0]` and `A[2]` are divisors of `A[3] = 6`. Element `A[1] = 4` does not divide `6`.

The result should be formulated as an array of length `N`. For the example above, it should contain `[0, 1, 0, 2]`.

Write a function:

```python
def solution(A):
    pass
```

that, given an array `A` of `N` integers, returns an array in which the `K`-th element is equal to the number of divisors of `A[K]` preceding it in `A`.

## Examples

1. Given `A = [2, 4, 3, 6]`, the function should return `[0, 1, 0, 2]`.
2. Given `A = [8, 4, 2]`, the function should return `[0, 0, 0]`. None of the numbers in array `A` is divisible by any of the numbers preceding it.
3. Given `A = [7, 8, 7, 8, 8]`, the function should return `[0, 0, 1, 1, 2]`.
4. Given `A = [8, 1, 3, 7, 21, 2, 14]`, the function should return `[0, 0, 1, 1, 3, 1, 3]`.

## Assumptions

Write an efficient algorithm for the following assumptions:

- `N` is an integer within the range `[1..50,000]`.
- Each element of array `A` is an integer within the range `[1..50,000]`.
