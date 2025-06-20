## 448. Find All Numbers Disappeared in an Array (Leetcode) - Easy

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in `nums`.

[Link for the question](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)

**Example 1:**

> **Input:** `nums = [4,3,2,7,8,2,3,1]`  
> **Output:** `[5,6]`  
> **Explanation:**  
> The array has 8 elements, so all numbers should be in the range `[1,8]`. The numbers 5 and 6 do not appear in the array.

**Example 2:**

> **Input:** `nums = [1,1]`  
> **Output:** `[2]`  
> **Explanation:**  
> The array has 2 elements, so all numbers should be in the range `[1,2]`. The number 2 does not appear in the array.

**Constraints:**

- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`

#### Answer
```Python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)

        return res
```

**Note: The time complexity of len(list) is O(1) since Python saves the length internally**
**Note: The time complexity of list.append is O(1) because Python pre-allocates extra space to avoid resizing on every append.**