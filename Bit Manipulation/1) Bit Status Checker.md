# Bit Status Checker - Easy

Given an integer `num`, return `"ON"` if the 3rd bit (0-indexed from the right, i.e., the 4th bit) is set (`1`), otherwise return `"OFF"`.

The 3rd bit means the bit at position `3`, counting from the right and starting at `0`. For example, in binary:

`10` → `00001010` → bit at position `3` is `1` → `"ON"`

`4` → `00000100` → bit at position `3` is `0` → `"OFF"`

**Example 1:**

> **Input:** `num = 10`  
> **Output:** `"ON"`

**Example 2:**

> **Input:** `num = 4`  
> **Output:** `"OFF"`

**Constraints:**

- `0 <= num <= 10^9`

```Python
def check():
    num = 10
    
    mask = 1 << 3
    
    if mask & num:
        print("ON")
    else:
        print("OFF")
```