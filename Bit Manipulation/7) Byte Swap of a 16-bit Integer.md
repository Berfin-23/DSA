# Byte Swap of a 16-bit Integer - Easy

Given a 16-bit unsigned integer `num`, return a new integer where the higher byte and the lower byte are swapped.

A byte consists of 8 bits, and a 16-bit number has two bytes:

- High byte (most significant 8 bits)
- Low byte (least significant 8 bits)

Swapping bytes means:

- High byte becomes the low byte
- Low byte becomes the high byte

**Example 1:**

> **Input:** `num = 0xB974`  
> Binary: `10111001 01110100`  
> Swapped: `01110100 10111001`  
> **Output:** `0x74B9` or `29881` in decimal

**Example 2:**

> **Input:** `num = 0x1234`  
> Binary: `00010010 00110100`  
> Swapped: `00110100 00010010`  
> **Output:** `0x3412` or `13330` in decimal

**Constraints:**

- `0 <= num <= 0xFFFF` (16-bit unsigned integer)

```Python
def byte_swap_16bit(num: int) -> int:
    high = (num & 0xFF00) >> 8
    low = (num & 0x00FF) << 8
    return high | low
```
