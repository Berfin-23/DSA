# 485. Max Consecutive Ones (LeetCode) - Easy

Given a binary array `nums`, return the maximum number of consecutive `1`'s in the array.

[Link for the question](https://leetcode.com/problems/max-consecutive-ones/)

**Example 1:**

> **Input:** `nums = [1,1,0,1,1,1]`  
> **Output:** `3`  
> **Explanation:** The first two digits or the last three digits are consecutive `1`s. The maximum number of consecutive `1`s is `3`.

**Example 2:**

> **Input:** `nums = [1,0,1,1,0,1]`  
> **Output:** `2`

**Constraints:**

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.


#### Answer

```Python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0

        for num in nums:
            if num:
                current_count += 1
            else:
                if current_count > max_count:
                    max_count = current_count
                current_count = 0

        if current_count > max_count:
            max_count = current_count

        return max_count
```
