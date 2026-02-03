# 62. Count the Triplets (GeeksforGeeks) - Easy

Given an array `arr`, count the number of distinct triplets `(a, b, c)` such that:

- `a + b = c`

Each triplet is counted only once, regardless of the order of `a` and `b`.

[Link for the question](https://www.geeksforgeeks.org/problems/count-the-triplets4615/1)

## Examples

**Example 1:**

> **Input:** `arr = [1, 5, 3, 2]`  
> **Output:** `2`  
> **Explanation:** There are 2 triplets: `1 + 2 = 3` and `3 + 2 = 5`

**Example 2:**

> **Input:** `arr = [2, 3, 4]`  
> **Output:** `0`  
> **Explanation:** No such triplet exists

## Constraints

- `1 <= len(arr) <= 10^3`
- `1 <= arr[i] <= 10^5`

## Solution (Python)

Sort the array and iterate from the end (largest element) treating it as the sum. Use two pointers on the remaining elements to find pairs that add up to this sum. This avoids counting the same triplet multiple times.

```python
def countTriplet(arr):
    """Counts distinct triplets (a, b, c) where a + b = c.

    Time Complexity: O(n^2) due to sorting + nested loops
    Space Complexity: O(1) if not counting sort space
    """
    arr.sort()
    n = len(arr)
    count = 0

    # Iterate from the end (largest element as the sum)
    for i in range(n - 1, 1, -1):
        left = 0
        right = i - 1

        target = arr[i]

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == target:
                count += 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return count


if __name__ == "__main__":
    # Quick sanity checks
    print(countTriplet([1, 5, 3, 2]))  # 2
    print(countTriplet([2, 3, 4]))     # 0
    print(countTriplet([1, 2, 3, 4])) # 2 (1+2=3, 1+3=4)
```
