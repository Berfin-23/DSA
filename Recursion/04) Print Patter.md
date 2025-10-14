# 4. Print Pattern (GeeksforGeeks) - Easy

Given a number `n`, print a sequence of numbers starting from `n`. Each next number in the sequence is `n - 5`, and this continues recursively until the number becomes less than or equal to 0. After that, print the sequence in reverse order, adding 5 each time, until it reaches back to the original number `n`.

**Note:** You must not use loops.

[Link for the question](https://www.geeksforgeeks.org/problems/print-pattern3549/1?page=1&category=Recursion&difficulty=Easy&sortBy=submissions)

## Examples

**Example 1:**

> **Input:** `n = -16`  
> **Output:** `[-16]`  
> **Explanation:** Since -16 is less than zero so it will remain same.

**Example 2:**

> **Input:** `n = 10`  
> **Output:** `[10, 5, 0, 5, 10]`  
> **Explanation:** The value decreases until it is greater or equal to 0. After that it increases and stops when it becomes 10 again.

## Constraints

- `-10^5 <= n <= 10^5`

## Solution (Python)

This problem demonstrates a classic recursion pattern where we need to perform actions both before and after the recursive call. The sequence goes down by 5 until it reaches ≤ 0, then comes back up.

```python
def printPattern(n):
class Solution:
    def pattern(self, n):
        result = []
        self._helper(n, result)
        return result
    
    def _helper(self, n, result):
        result.append(n)
        
        if n <= 0:
            return
        
        self._helper(n - 5, result)
        result.append(n)
```
