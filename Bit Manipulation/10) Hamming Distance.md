# 461. Hamming Distance (LeetCode) - Easy

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers `x` and `y`, return the Hamming distance between them.

[Link for the question](https://leetcode.com/problems/hamming-distance/)

## Examples

**Example 1:**

> **Input:** `x = 1`, `y = 4` > **Output:** `2` > **Explanation:**
>
> ```
> 1 (0 0 0 1)
> 4 (0 1 0 0)
>   ↑   ↑
> ```
>
> The above arrows point to positions where the corresponding bits are different.

**Example 2:**

> **Input:** `x = 3`, `y = 1` > **Output:** `1`

## Constraints

- `0 <= x, y <= 2^31 - 1`

```Python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor:
            count += xor & 1
            xor >>= 1
        return count
```
