## 316. Remove Duplicate Letters (Leetcode) - Medium

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

[Link for the question](https://leetcode.com/problems/remove-duplicate-letters/description/)

**Example 1:**

> **Input:** `s = "bcabc"`  
> **Output:** `"abc"`

**Example 2:**

> **Input:** `s = "cbacdcbc"`  
> **Output:** `"acdb"`

**Constraints:**

- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters.

```Python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Dictionary to store the last occurrence index of each character
        last_index = {char: i for i, char in enumerate(s)}
        
        stack = []       # Stores result characters
        seen = set()     # Tracks characters already in stack

        for i, char in enumerate(s):
            # If character is already in the result, skip it
            if char in seen:
                continue
            
            # While the current character is smaller than the last character in stack
            # and the last character exists later in the string again,
            # we can pop it to get a better lex order
            while stack and char < stack[-1] and i < last_index[stack[-1]]:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(char)
            seen.add(char)

        # Join stack to get result string
        return ''.join(stack)
```