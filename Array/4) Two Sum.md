## 1. Two Sum (Leetcode) - Easy

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

[Link for the question](https://leetcode.com/problems/two-sum/description/)

**Example 1:**

> **Input:** `nums = [2,7,11,15], target = 9`  
> **Output:** `[0,1]`  
> **Explanation:**  
> Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

**Example 2:**

> **Input:** `nums = [3,2,4], target = 6`  
> **Output:** `[1,2]`  
> **Explanation:**  
> Because `nums[1] + nums[2] == 6`, we return `[1, 2]`.

**Example 3:**

> **Input:** `nums = [3,3], target = 6`  
> **Output:** `[0,1]`  
> **Explanation:**  
> Because `nums[0] + nums[1] == 6`, we return `[0, 1]`.

**Constraints:**

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

#### Answer
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in hashMap:
                return [hashMap[difference], index]
            hashMap[value] = index
```

# Time Complexity of `key in` for Python Data Types

This table shows the average and worst-case time complexity of the `in` operator for different Python data types.

| Data Type | Operation          | Average Case | Worst Case | Notes |
|-----------|--------------------|--------------|------------|-------|
| list      | `key in list`      | O(n)         | O(n)       | Linear search through elements |
| tuple     | `key in tuple`     | O(n)         | O(n)       | Same as list (sequential check) |
| set       | `key in set`       | O(1)         | O(n)       | Hash table-based lookup |
| dict      | `key in dict`      | O(1)         | O(n)       | Checks for presence of key (not value); also uses hash table |
