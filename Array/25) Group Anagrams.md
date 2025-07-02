## 49. Group Anagrams (Leetcode) - Medium

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

[Link for the question](https://leetcode.com/problems/group-anagrams/description/)

**Example 1:**

> **Input:** `strs = ["eat","tea","tan","ate","nat","bat"]`  
> **Output:** `[["bat"],["nat","tan"],["ate","eat","tea"]]`  
> **Explanation:**
>
> - There is no string in `strs` that can be rearranged to form `"bat"`.
> - The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
> - The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:**

> **Input:** `strs = [""]`  
> **Output:** `[[""]]`

**Example 3:**

> **Input:** `strs = ["a"]`  
> **Output:** `[["a"]]`

**Constraints:**

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

#### Answer 1
```Python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())
```

#### Answer 2
```Python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        anagram_groups = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1

            anagram_groups[tuple(count)].append(word)

        return list(anagram_groups.values())
```
