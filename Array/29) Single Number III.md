# 260. Single Number III (LeetCode) - Medium

Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

[Link for the question](https://leetcode.com/problems/single-number-iii/description/)

**Example 1:**

> **Input:** `nums = [1,2,1,3,2,5]`  
> **Output:** `[3,5]`  
> **Explanation:** `[5, 3]` is also a valid answer.

**Example 2:**

> **Input:** `nums = [-1,0]`  
> **Output:** `[-1,0]`

**Example 3:**

> **Input:** `nums = [0,1]`  
> **Output:** `[1,0]`

**Constraints:**

- `2 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Each integer in `nums` will appear twice, only two integers will appear once.

```Python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        set_bit = xor & -xor

        a, b = 0, 0
        for num in nums:
            if num & set_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]
```
