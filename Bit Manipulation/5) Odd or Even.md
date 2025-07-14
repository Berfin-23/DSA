# Odd or Even - Easy

Given a non-negative integer `num`, determine whether it is odd or even using bitwise operations.

Return `"Odd"` if the number is odd, otherwise return `"Even"`.

You must use bitwise operators only. Do not use `%`, `/`, or `*`.

**Hint:**
In binary, the least significant bit (LSB) determines whether a number is odd or even:

- If the last bit is `1`, the number is odd
- If the last bit is `0`, the number is even

**Example 1:**

> **Input:** `num = 10`  
> Binary: `1010`  
> **Output:** `"Even"`

**Example 2:**

> **Input:** `num = 7`  
> Binary: `0111`  
> **Output:** `"Odd"`

**Constraints:**

- `0 <= num <= 10^9`

```Python
def check_odd_even(num):
    if num & 1:
        return "Odd"
    else:
        return "Even"
```