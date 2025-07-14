# Set the 3rd Bit - Easy

Given a non-negative integer `num`, return the integer obtained by setting the 3rd bit (0-indexed from the right) to `1`. All other bits should remain unchanged.

This means you're performing a bitwise operation to turn ON the 4th bit (index `3`) regardless of whether it was previously `0` or `1`.

You may assume that the 3rd bit refers to the bit at position `3` (`2³`), counting from `0` on the right.

**Example 1:**

> **Input:** `num = 5`  
> Binary: `0101`  
> Set 3rd bit: `1101`  
> **Output:** `13`

**Example 2:**

> **Input:** `num = 9`  
> Binary: `1001`  
> Set 3rd bit: `1001` (bit already ON)  
> **Output:** `9`

**Constraints:**

- `0 <= num <= 10^9`

```Python
def set_bit():
    number = 5            
    mask = 1 << 3     
    new_number = number | mask 
    print(new_number)
```