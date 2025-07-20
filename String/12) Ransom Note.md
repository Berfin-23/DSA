# 383. Ransom Note (LeetCode) - Easy

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

[Link for the question](https://leetcode.com/problems/ransom-note/)

## Examples

**Example 1:**

> **Input:** `ransomNote = "a"`, `magazine = "b"` > **Output:** `false`

**Example 2:**

> **Input:** `ransomNote = "aa"`, `magazine = "ab"` > **Output:** `false`

**Example 3:**

> **Input:** `ransomNote = "aa"`, `magazine = "aab"` > **Output:** `true`

## Constraints

- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

#### Answer 1

```Python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}

        for letter in magazine:
            hashMap[letter] = hashMap.get(letter, 0) + 1

        for letter in ransomNote:
            if letter in hashMap and hashMap[letter] > 0:
                hashMap[letter] -= 1
            else:
                return False

        return True
```

#### Answer 2

```Python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for ch in ransomNote:
            if  ch not in magazine:
                return False
            else:
                magazine=magazine.replace(ch,"",1)
        return True
```
