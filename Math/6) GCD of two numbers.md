# GCD of Two Numbers (GeeksforGeeks) - Basic

[GeeksforGeeks - GCD of Two Numbers](https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/)

Given two positive integers `a` and `b`, find GCD of `a` and `b`.

**Note:** Don't use the inbuilt gcd function

## Examples

> **Example 1:**
>
> **Input:** `a = 20`, `b = 28`
>
> **Output:** `4`
>
> **Explanation:** GCD of `20` and `28` is `4`

> **Example 2:**
>
> **Input:** `a = 60`, `b = 36`
>
> **Output:** `12`
>
> **Explanation:** GCD of `60` and `36` is `12`

## Constraints

- `1 ≤ a, b ≤ 10^9`

```python
class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
```
