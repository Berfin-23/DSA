# Turn OFF the 3rd Bit - Easy

Given a non-negative integer `num`, return a new integer with the 3rd bit (0-indexed from the right) turned OFF. All other bits must remain unchanged.

Turning OFF a bit means setting that particular bit to `0` using bitwise operations.

**Note:**
The 3rd bit refers to position `3`, or the `2³ = 8` place in binary.

**Example 1:**

> **Input:** `num = 13`  
> Binary: `1101`  
> Turn OFF 3rd bit: `0101`  
> **Output:** `5`

**Example 2:**

> **Input:** `num = 9`  
> Binary: `1001`  
> Turn OFF 3rd bit: `0001`  
> **Output:** `1`

**Constraints:**

- `0 <= num <= 10^9`

```Python
def turn_off_third_bit(number):
    mask = ~(1 << 3)
    new_number = number & mask
    return new_number
```
