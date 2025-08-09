# Armstrong Numbers (GeeksforGeeks) - Easy

[GeeksforGeeks - Armstrong Numbers](https://www.geeksforgeeks.org/problems/armstrong-numbers2727/)

You are given a 3-digit number `n`, Find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. `371` is an Armstrong number since `3^3 + 7^3 + 1^3 = 371`.

## Examples

> **Example 1:**
>
> **Input:** `n = 153`
>
> **Output:** `true`
>
> **Explanation:** `153` is an Armstrong number since `1^3 + 5^3 + 3^3 = 153`.

> **Example 2:**
>
> **Input:** `n = 372`
>
> **Output:** `false`
>
> **Explanation:** `372` is not an Armstrong number since `3^3 + 7^3 + 2^3 = 378`.

> **Example 3:**
>
> **Input:** `n = 100`
>
> **Output:** `false`
>
> **Explanation:** `100` is not an Armstrong number since `1^3 + 0^3 + 0^3 = 1`.

## Constraints

- `100 ≤ n < 1000`

```python
class Solution:
    def armstrongNumber (self, n):
        original_n = n
        sum = 0
        
        while n > 0:
            digit = n % 10
            n = n // 10
            
            sum = sum + digit ** 3
            
        return sum == original_n
```