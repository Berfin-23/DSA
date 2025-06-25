## Move Zeroes to Front and One to Back - Easy

You are given a binary array `arr` containing only 0s and 1s. Your task is to rearrange the array in-place such that all 0s are moved to the front and all 1s to the end. Return the modified array.

You must solve the problem using a two-pointer approach in `O(n)` time and `O(1)` extra space.

**Example 1:**

> **Input:** `arr = [1, 1, 1, 0, 0, 0]`  
> **Output:** `[0, 0, 0, 1, 1, 1]`  
> **Explanation:**  
> The 0s are moved to the front and 1s to the end using in-place swapping.

**Example 2:**

> **Input:** `arr = [0, 1, 0, 1, 1, 0]`  
> **Output:** `[0, 0, 0, 1, 1, 1]`  
> **Explanation:**  
> The relative order within 0s or 1s does not matter.

**Example 3:**

> **Input:** `arr = [0, 0, 0]`  
> **Output:** `[0, 0, 0]`  
> **Explanation:**  
> Already sorted.

**Constraints:**

- `1 <= arr.length <= 10^5`
- `arr[i]` is either `0` or `1`

#### Answer
```Python
arr = [1, 0, 1, 0, 1, 0]
start = 0
end = len(arr) - 1

while start < end:
    if arr[start] == 1 and arr[end] == 0:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    elif arr[start] == 0:
        start += 1
    else:
        end -= 1

print(arr)
```