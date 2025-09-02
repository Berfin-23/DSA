# Factorial (GeeksforGeeks) - Basic

[GeeksforGeeks - Factorial](https://www.geeksforgeeks.org/problems/factorial5739/1)

Given a positive integer `n`, find the factorial of `n`.

## Examples

> **Example 1:**
>
> **Input:** `n = 5`
>
> **Output:** `120`
>
> **Explanation:** `1 x 2 x 3 x 4 x 5 = 120`

> **Example 2:**
>
> **Input:** `n = 4`
>
> **Output:** `24`
>
> **Explanation:** `1 x 2 x 3 x 4 = 24`

## Constraints

- `0 ≤ n ≤ 12`

```python
class Solution:
    def factorial(self, n: int) -> int:
        if n <= 1:
            return 1
        else:
            return n * self.factorial(n - 1)
```