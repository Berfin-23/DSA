# Nth Fibonacci Number (GeeksforGeeks) - Easy

[GeeksforGeeks - Nth Fibonacci Number](https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article)

Given a non-negative integer `n`, your task is to find the `n`th Fibonacci number.

The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are `0` followed by `1`.

The Fibonacci sequence is defined as follows:

- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n - 1) + F(n - 2)` for `n > 1`

## Examples

> **Example 1:**
>
> **Input:** `n = 5`
>
> **Output:** `5`
>
> **Explanation:** The 5th Fibonacci number is `5`.

> **Example 2:**
>
> **Input:** `n = 0`
>
> **Output:** `0`
>
> **Explanation:** The 0th Fibonacci number is `0`.

> **Example 3:**
>
> **Input:** `n = 1`
>
> **Output:** `1`
>
> **Explanation:** The 1st Fibonacci number is `1`.

## Constraints

- `0 ≤ n ≤ 30`

```python
class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        return self.nthFibonacci(n - 1) + self.nthFibonacci(n - 2)
```
