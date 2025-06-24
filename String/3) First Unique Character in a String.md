## 387. First Unique Character in a String (Leetcode) - Easy

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

[Link for the question](https://leetcode.com/problems/first-unique-character-in-a-string/description/)

**Example 1:**

> **Input:** `s = "leetcode"`  
> **Output:** `0`  
> **Explanation:**  
> The character `'l'` at index 0 is the first character that does not occur at any other index.

**Example 2:**

> **Input:** `s = "loveleetcode"`  
> **Output:** `2`

**Example 3:**

> **Input:** `s = "aabb"`  
> **Output:** `-1`

**Constraints:**

- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

#### Answer
```Python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}

        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1

        for index, char in enumerate(s):
            if hashMap[char] == 1:
                return index
        
        return -1
```