# Odd or Even (GeeksforGeeks) - Basic

Given a positive integer `n`, determine whether it is odd or even. Return `true` if the number is even and `false` if the number is odd.

[Link for the question](https://www.geeksforgeeks.org/problems/odd-or-even3618/1)

## Examples

**Example 1:**

> **Input:** `n = 15` > **Output:** `false` > **Explanation:** The number is not divisible by `2`, Odd number.

**Example 2:**

> **Input:** `n = 44` > **Output:** `true` > **Explanation:** The number is divisible by `2`, Even number.

## Constraints

- `1 ≤ n ≤ 10^4`

#### Answer 1
```python
class Solution:
    def isEven (self, n):
        return not n & 1
```

#### Answer 2
```python
class Solution:
    def isEven (self, n):
        if n % 2 == 0:
            return True
        else:
            return False
```