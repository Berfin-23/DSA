## 238. Product of Array Except Self (Leetcode) - Medium

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

[Link for the question](https://leetcode.com/problems/product-of-array-except-self/description/)

**Example 1:**

> **Input:** `nums = [1,2,3,4]`  
> **Output:** `[24,12,8,6]`

**Example 2:**

> **Input:** `nums = [-1,1,0,-3,3]`  
> **Output:** `[0,0,9,0,0]`

**Constraints:**

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is guaranteed to fit in a 32-bit integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array does not count as extra space for space complexity analysis.)

#### Answer
```Python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left_product = 1

        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1

        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
```