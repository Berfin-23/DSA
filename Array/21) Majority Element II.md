## 229. Majority Element II (Leetcode) - Medium

Given an integer array of size `n`, find all elements that appear more than `⌊n/3⌋` times.

[Link for the question](https://leetcode.com/problems/majority-element-ii/description/)

**Example 1:**

> **Input:** `nums = [3,2,3]`  
> **Output:** `[3]`

**Example 2:**

> **Input:** `nums = [1]`  
> **Output:** `[1]`

**Example 3:**

> **Input:** `nums = [1,2]`  
> **Output:** `[1,2]`

**Constraints:**

- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

```Python
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # Counters for the potential majority elements
        count1 = count2 = 0     
        # Potential majority element candidates
        candidate1 = candidate2 = 0

        # First pass to find potential majority elements.
        for num in nums:
            # If count1 is 0 and the current number is not equal to candidate2, update candidate1.
            if count1 == 0 and num != candidate2:
                count1 = 1
                candidate1 = num

            # If count2 is 0 and the current number is not equal to candidate1, update candidate2.
            elif count2 == 0 and num != candidate1:
                count2 = 1
                candidate2 = num
            
            # Update counts for candidate1 and candidate2.
            elif candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

            # If the current number is different from both candidates, decrement their counts.
            else:
                count1 -= 1
                count2 -= 1

        result = []
        threshold = len(nums) // 3  # Threshold for majority element

        # Second pass to count occurrences of the potential majority elements.
        count1 = count2 = 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

        # Check if the counts of potential majority elements are greater than n/3 and add them to the result.
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)

        return result
```