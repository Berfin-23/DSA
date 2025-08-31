# Print 1 To N Without Loop (GeeksforGeeks) - Basic

[GeeksforGeeks - Print 1 To N Without Loop](https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1)

You are given an integer `n`. You have to print all numbers from `1` to `n`.

**Note:** You must use recursion only, and print all numbers from `1` to `n` in a single line, separated by spaces.

## Examples

> **Example 1:**
>
> **Input:** `n = 10`
>
> **Output:** `1 2 3 4 5 6 7 8 9 10`

> **Example 2:**
>
> **Input:** `n = 5`
>
> **Output:** `1 2 3 4 5`

> **Example 3:**
>
> **Input:** `n = 1`
>
> **Output:** `1`

## Constraints

- `1 ≤ n ≤ 10^3`

```python
class Solution:    
    def printNos(self,n):
        if n <= 0:
            return
        self.printNos(n - 1)
        print(n, end=" ")
```