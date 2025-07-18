# 215. Kth Largest Element in an Array (LeetCode) - Medium

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?

[Link for the question](https://leetcode.com/problems/kth-largest-element-in-an-array/)

**Example 1:**

> **Input:** `nums = [3,2,1,5,6,4]`, `k = 2`  
> **Output:** `5`

**Example 2:**

> **Input:** `nums = [3,2,3,1,2,4,5,5,6]`, `k = 4`  
> **Output:** `4`

**Constraints:**

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

```Python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        l = len(nums)
        c = l - k
        c1 = 0

        while c1 < c:
            heapq.heappop(nums)
            c1 += 1
            
        return heapq.heappop(nums)
```