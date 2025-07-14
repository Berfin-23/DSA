# Toggle the 3rd Bit - Easy

Given a non-negative integer `num`, return a new integer obtained by toggling the 3rd bit (0-indexed from the right). All other bits must remain unchanged.

Toggling a bit means flipping it:

- If it's `1`, it becomes `0`
- If it's `0`, it becomes `1`

**Note:**
The 3rd bit refers to bit at index `3`, or the `2³ = 8` position in binary.

**Example 1:**

> **Input:** `num = 13`  
> Binary: `1101`  
> Toggle 3rd bit: `0101`  
> **Output:** `5`

**Example 2:**

> **Input:** `num = 5`  
> Binary: `0101`  
> Toggle 3rd bit: `1101`  
> **Output:** `13`

**Constraints:**

- `0 <= num <= 10^9`

```Python
def toggle_third_bit(number):
    mask = 1 << 3         
    new_number = number ^ mask 
    return new_number
```