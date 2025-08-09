# Rotate Array by One (GeeksforGeeks) - Basic

[GeeksforGeeks - Rotate Array by One](https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article)

Given an array `arr`, rotate the array by one position in clockwise direction.

## Examples

> **Example 1:**
>
> **Input:** `arr[] = [1, 2, 3, 4, 5]`
>
> **Output:** `[5, 1, 2, 3, 4]`
>
> **Explanation:** If we rotate `arr` by one position in clockwise direction, `5` comes to the front and remaining elements are shifted to the end.

> **Example 2:**
>
> **Input:** `arr[] = [9, 8, 7, 6, 4, 2, 1, 3]`
>
> **Output:** `[3, 9, 8, 7, 6, 4, 2, 1]`
>
> **Explanation:** After rotating clockwise, `3` comes in first position.

## Constraints

- `1 <= arr.size() <= 10^5`
- `0 <= arr[i] <= 10^5`

```python
class Solution:
    def rotate(self, arr):
        last_element = arr[-1]
        
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]
            
        arr[0] = last_element
        
        return arr
```