# 191. Number of 1 Bits (LeetCode) - Easy

Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

[Link for the question](https://leetcode.com/problems/number-of-1-bits/)

## Examples

**Example 1:**

> **Input:** `n = 11` > **Output:** `3` > **Explanation:** The input binary string `1011` has a total of three set bits.

**Example 2:**

> **Input:** `n = 128` > **Output:** `1` > **Explanation:** The input binary string `10000000` has a total of one set bit.

**Example 3:**

> **Input:** `n = 2147483645` > **Output:** `30` > **Explanation:** The input binary string `1111111111111111111111111111101` has a total of thirty set bits.

## Constraints

- `1 <= n <= 2^31 - 1`

```Python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            if (n >> i) & 1:
                res += 1

        return res
```