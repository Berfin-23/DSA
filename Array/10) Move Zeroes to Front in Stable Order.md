## Move Zeroes to Front (Stable Order) - Easy

Given an integer array `arr`, move all the 0s to the beginning of the array while maintaining the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

**Example 1:**

> **Input:** `arr = [10, 20, 0, 40, 80, 0]`  
> **Output:** `[0, 0, 10, 20, 40, 80]`  
> **Explanation:**  
> The two zeros are moved to the front, and the order of non-zero elements is preserved.

**Example 2:**

> **Input:** `arr = [0, 1, 2, 0, 3, 4]`  
> **Output:** `[0, 0, 1, 2, 3, 4]`

**Example 3:**

> **Input:** `arr = [1, 2, 3]`  
> **Output:** `[1, 2, 3]`  
> **Explanation:**  
> No zero present, so the array remains unchanged.

**Constraints:**

- `1 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`


#### Answer
```Python
arr = [10, 20, 0, 40, 80, 0]

n = len(arr)
insert_pos = n - 1

for i in range(n - 1, -1, -1):
    if arr[i] != 0:
        arr[insert_pos] = arr[i]
        insert_pos -= 1

for i in range(insert_pos + 1):
    arr[i] = 0

print(arr)
```