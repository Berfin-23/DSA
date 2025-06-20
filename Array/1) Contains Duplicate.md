## 217. Contains Duplicates (Leetcode) - Easy

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

[Link for the question](https://leetcode.com/problems/contains-duplicate/description/)

**Example 1:**

> **Input:** `nums = [1,2,3,1]`  
> **Output:** `true`  
> **Explanation:**  
> The element 1 occurs at the indices 0 and 3.

**Example 2:**

> **Input:** `nums = [1,2,3,4]`  
> **Output:** `false`  
> **Explanation:**  
> All elements are distinct.

**Example 3:**

> **Input:** `nums = [1,1,1,3,3,4,3,2,4,2]`  
> **Output:** `true`


#### Answer

```Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True
```

**Note: converting list to set take O(n) time**