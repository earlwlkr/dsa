# MaxPerfectSubtree

Given a tree, find the number of nodes in the biggest perfect subtree.

## Description

The values contained in the nodes are not relevant in this task.

A binary tree is called perfect if all of its nodes have exactly `0` or `2` children and all of its leaves are at the same level. By the size of a perfect tree we mean its number of nodes.

Your task is to calculate the size of the biggest perfect subtree that can be obtained by removing any number of nodes.

In the example shown in the source screenshot, after removing nodes `1`, `2`, `4`, and `11`, you obtain a perfect tree of size `7`. Perfect trees of size `3` are rooted at several nodes, but they are smaller than the best answer of `7`.

Write a function:

```python
def solution(T):
    pass
```

that, given a non-empty binary tree `T` consisting of `N` nodes, returns the size of the biggest perfect subtree that can be obtained by removing nodes.

## Example

For the tree shown in the source screenshots, the function should return `7`.

## Assumptions

- `N` is an integer within the range `[1..100,000]`.
- The height of tree `T` is within the range `[0..800]`.
