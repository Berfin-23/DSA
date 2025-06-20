## 268. Missing Number (Leetcode) - Easy

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

[Link for the question](https://leetcode.com/problems/missing-number/description/)

**Example 1:**

> **Input:** `nums = [3,0,1]`  
> **Output:** `2`  
> **Explanation:**  
> `n = 3` since there are 3 numbers, so all numbers are in the range `[0,3]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 2:**

> **Input:** `nums = [0,1]`  
> **Output:** `2`  
> **Explanation:**  
> `n = 2` since there are 2 numbers, so all numbers are in the range `[0,2]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 3:**

> **Input:** `nums = [9,6,4,2,3,5,7,0,1]`  
> **Output:** `8`  
> **Explanation:**  
> `n = 9` since there are 9 numbers, so all numbers are in the range `[0,9]`. 8 is the missing number in the range since it does not appear in `nums`.

#### Answer

```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1)//2

        current = sum(nums)

        return expected - current

```

**Note: This solution uses the mathematical formula for sum of first n natural numbers: n * ( n+1 ) /2**
**Note: The time complexity of len(list) is O(1) since Python saves the length internally and sum(list) is O(n) since Python iterated through every element**

