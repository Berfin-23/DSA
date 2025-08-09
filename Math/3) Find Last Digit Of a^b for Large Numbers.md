# Find Last Digit Of a^b for Large Numbers (GeeksforGeeks) - Medium

You are given two integer numbers in the form of string, the base `a` and the index `b`. You have to find the last digit of `a^b`.

[Link for the question](https://www.geeksforgeeks.org/problems/find-last-digit-of-ab-for-large-numbers1936/1)

## Examples

**Example 1:**

> **Input:** `a = "3"`, `b = "10"` > **Output:** `9` > **Explanation:** `3^10 = 59049`. Last digit is `9`.

**Example 2:**

> **Input:** `a = "6"`, `b = "2"` > **Output:** `6` > **Explanation:** `6^2 = 36`. Last digit is `6`.

## Your Task

You don't need to read input or print anything. Your task is to complete the function `getLastDigit()` which takes two strings `a`, `b` as parameters and returns an integer denoting the last digit of `a^b`.

## Expected Complexity

- **Time Complexity:** `O(|b|)`
- **Auxiliary Space:** `O(1)`

## Constraints

- `1 <= |a|, |b| <= 1000`

**Note:** `|a| = length of a` and `|b| = length of b`. There will not be any test cases such that `a^b` is undefined.

```python
class Solution:
    def getLastDigit(self, a, b):
        last_digit = int(a[-1])
        if b == '0':
            return 1

        cycle = []
        val = last_digit
        while val not in cycle:
            cycle.append(val)
            val = (val * last_digit) % 10

        index = (int(b) % len(cycle)) - 1
        return cycle[index] if index >= 0 else cycle[-1]
```
