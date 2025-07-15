# 342. Power of Four (LeetCode) - Easy

Given an integer `n`, return `true` if it is a power of four. Otherwise, return `false`.

An integer `n` is a power of four, if there exists an integer `x` such that `n == 4^x`.

[Link for the question](https://leetcode.com/problems/power-of-four/)

## Examples

**Example 1:**

> **Input:** `n = 16` > **Output:** `true`

**Example 2:**

> **Input:** `n = 5` > **Output:** `false`

**Example 3:**

> **Input:** `n = 1` > **Output:** `true`

## Constraints

- `-2^31 <= n <= 2^31 - 1`

```Python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
```
