# Frequencies in a Limited Array (GeeksforGeeks) - Easy

[GeeksforGeeks - Frequencies in a Limited Array](https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/)

You are given an array `arr[]` containing positive integers. The elements in the array `arr[]` range from 1 to `n` (where `n` is the size of the array), and some numbers may be repeated or absent. You have to count the frequency of all numbers in the range 1 to `n` and return an array of size `n` such that `result[i]` represents the frequency of the number `i` (1-based indexing).

## Examples

> **Example 1:**
>
> **Input:** `arr[] = [2, 3, 2, 3, 5]`
>
> **Output:** `[0, 2, 2, 0, 1]`
>
> **Explanation:**
>
> - `1` occurring `0` times
> - `2` occurring `2` times
> - `3` occurring `2` times
> - `4` occurring `0` times
> - `5` occurring `1` time

> **Example 2:**
>
> **Input:** `arr[] = [3, 3, 3, 3]`
>
> **Output:** `[0, 0, 4, 0]`
>
> **Explanation:**
>
> - `1` occurring `0` times
> - `2` occurring `0` times
> - `3` occurring `4` times
> - `4` occurring `0` times

> **Example 3:**
>
> **Input:** `arr[] = [1]`
>
> **Output:** `[1]`
>
> **Explanation:** `1` occurring `1` time, and there are no other numbers between `1` and the size of the array.

## Constraints

- `1 ≤ arr.size() ≤ 10^6`
- `1 ≤ arr[i] ≤ arr.size()`

#### Answer 1

```python
class Solution:
    def frequencyCount(self, arr):
        
        freq = [0] * len(arr)
        
        for num in arr:
            freq[num - 1] += 1
            
        return freq
```

#### Answer 2

```python
class Solution:
    def frequencyCount(self, arr):
        N = len(arr)
        
        for i in range(N):
            arr[i] -= 1

        for i in range(N):
            arr[arr[i] % N] += N
    
        for i in range(N):
            arr[i] //= N
            
        return arr
```