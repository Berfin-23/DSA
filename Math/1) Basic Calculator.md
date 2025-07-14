# 224. Basic Calculator (LeetCode) - Hard

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

[Link for the question](https://leetcode.com/problems/basic-calculator/)

**Example 1:**

> **Input:** `s = "1 + 1"`  
> **Output:** `2`

**Example 2:**

> **Input:** `s = " 2-1 + 2 "`  
> **Output:** `3`

**Example 3:**

> **Input:** `s = "(1+(4+5+2)-3)+(6+8)"`  
> **Output:** `23`

**Constraints:**

- `1 <= s.length <= 3 * 10^5`
- `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.
- `s` represents a valid expression.
- `'+'` is not used as a unary operation (i.e., `"+1"` and `"+(2 + 3)"` is invalid).
- `'-'` could be used as a unary operation (i.e., `"-1"` and `"-(2 + 3)"` is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

```Python
class Solution:
    def calculate(self, s: str) -> int:
        output = 0
        current = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                current = current * 10 + int(char)

            elif char in {"-", "+"}:
                output += (current * sign)
                current = 0
                if char == "-":
                    sign = -1
                else:
                    sign = 1

            elif char == "(":
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1

            elif char == ")":
                output += (current * sign)
                output *= stack.pop()
                output += stack.pop()
                current = 0

        return output + (current * sign)
```