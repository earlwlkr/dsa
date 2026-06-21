# Rome

Given a map with directed roads, return the id of the city that is reachable from all other cities.

## Description

You are given a map of the Roman Empire. There are `N + 1` cities, numbered from `0` to `N`, and `N` directed roads between them. The road network is connected; that is, ignoring the directions of roads, there is a route between each pair of cities.

The capital of the Roman Empire is Rome. We know that all roads lead to Rome. This means that there is a route from each city to Rome. Your task is to find Rome on the map, or decide that it is not there.

The roads are described by two arrays `A` and `B` of `N` integers each. For each integer `K`, where `0 <= K < N`, there exists a road from city `A[K]` to city `B[K]`.

Write a function:

```python
def solution(A, B):
    pass
```

that, given two arrays `A` and `B`, returns the number of the city which is Rome: the city that can be reached from all other cities. If no such city exists, return `-1`.

## Examples

1. Given `A = [1, 2, 3]` and `B = [0, 0, 0]`, the function should return `0`.
2. Given `A = [0, 1, 2, 4, 5]` and `B = [2, 3, 3, 3, 2]`, the function should return `3`.
3. Given `A = [2, 3, 3, 4]` and `B = [1, 1, 0, 0]`, the function should return `-1`.

## Assumptions

Write an efficient algorithm for the following assumptions:

- `N` is an integer within the range `[1..200,000]`.
- Each element of arrays `A` and `B` is an integer within the range `[0..N]`.
- The road network is connected.
