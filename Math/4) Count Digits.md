# Count Digits (GeeksforGeeks) - Easy

[GeeksforGeeks - Count Digits](https://www.geeksforgeeks.org/problems/count-digits5716/)

Given a positive integer `n`, count the number of digits in `n` that divide `n` evenly (i.e., without leaving a remainder). Return the total number of such digits.

A digit `d` of `n` divides `n` evenly if the remainder when `n` is divided by `d` is 0 (`n % d == 0`).
Digits of `n` should be checked individually. If a digit is 0, it should be ignored because division by 0 is undefined.

## Examples

> **Example 1:**
>
> **Input:** `n = 12`
>
> **Output:** `2`
>
> **Explanation:**
>
> - Digits: `1` and `2`
> - Both `1` and `2` divide `12` evenly (remainder 0)

> **Example 2:**
>
> **Input:** `n = 2446`
>
> **Output:** `1`
>
> **Explanation:**
>
> - Digits: `2`, `4`, `4`, `6`
> - Only `2` divides `2446` evenly, while `4` and `6` do not

> **Example 3:**
>
> **Input:** `n = 23`
>
> **Output:** `0`
>
> **Explanation:**
>
> - Digits: `2` and `3`
> - Neither `2` nor `3` divide `23` evenly

## Constraints

- `1 <= n <= 10^5`

```python
class Solution:
    def evenlyDivides(self, n):
        count = 0
        original_n = n
        
        while n > 0:
            digit = n % 10
            n = n // 10
            
            if (digit != 0) and (original_n % digit == 0):
                count += 1
                
        return count
```