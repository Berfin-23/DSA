## 283. Move Zeroes (Leetcode) - Easy

Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

[Link for the question](https://leetcode.com/problems/move-zeroes/description/)

**Example 1:**

> **Input:** `nums = [0,1,0,3,12]`  
> **Output:** `[1,3,12,0,0]`

**Example 2:**

> **Input:** `nums = [0]`  
> **Output:** `[0]`

**Constraints:**

- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

#### Answer
```Python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        swap_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[swap_index] = nums[i]
                swap_index += 1

        for i in range(swap_index, len(nums)):
            nums[i] = 0
```