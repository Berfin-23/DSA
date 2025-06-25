## 75. Sort Colors (Leetcode) - Medium

Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

[Link for the question](https://leetcode.com/problems/sort-colors/description/)

**Example 1:**

> **Input:** `nums = [2,0,2,1,1,0]`  
> **Output:** `[0,0,1,1,2,2]`

**Example 2:**

> **Input:** `nums = [2,0,1]`  
> **Output:** `[0,1,2]`

**Constraints:**

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

#### Answer
```Python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = point = 0
        high = len(nums) - 1

        while point <= high:
            if nums[point] == 0:
                nums[low], nums[point] = nums[point], nums[low]
                low += 1
                point += 1
            elif nums[point] == 1:
                point += 1
            elif nums[point] == 2:
                nums[point], nums[high] = nums[high], nums[point]
                high -= 1     
```