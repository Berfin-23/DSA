## 242. Valid Anagram (Leetcode) - Easy

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

[Link for the question](https://leetcode.com/problems/valid-anagram/description/)

**Example 1:**

> **Input:** `s = "anagram", t = "nagaram"`  
> **Output:** `true`

**Example 2:**

> **Input:** `s = "rat", t = "car"`  
> **Output:** `false`

**Constraints:**

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

#### Answer 1
```Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_hashMap = {}
        t_hashMap = {}

        for char in s:
            s_hashMap[char] = s_hashMap.get(char, 0) + 1
        
        for char in t:
            t_hashMap[char] = t_hashMap.get(char, 0) + 1

        return s_hashMap == t_hashMap
```

#### Answer 2
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        if len(s) != len(t):
            return False

        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1

        return True
```