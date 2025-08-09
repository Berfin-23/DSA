# Array Subset (GeeksforGeeks) - Basic

[GeeksforGeeks - Array Subset](https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/)

Given two arrays `a[]` and `b[]`, your task is to determine whether `b[]` is a subset of `a[]`.

## Examples

> **Example 1:**
>
> **Input:** `a[] = [11, 7, 1, 13, 21, 3, 7, 3]`, `b[] = [11, 3, 7, 1, 7]`
>
> **Output:** `true`
>
> **Explanation:** `b[]` is a subset of `a[]`.

> **Example 2:**
>
> **Input:** `a[] = [1, 2, 3, 4, 4, 5, 6]`, `b[] = [1, 2, 4]`
>
> **Output:** `true`
>
> **Explanation:** `b[]` is a subset of `a[]`.

> **Example 3:**
>
> **Input:** `a[] = [10, 5, 2, 23, 19]`, `b[] = [19, 5, 3]`
>
> **Output:** `false`
>
> **Explanation:** `b[]` is not a subset of `a[]`.

## Constraints

- `1 <= a.size(), b.size() <= 10^5`
- `1 <= a[i], b[j] <= 10^6`

```python
#User function Template for python3

class Solution:
    def isSubset(self, a, b):
        
        if len(b) > len(a):
            return False
            
        if len(b) == 0:
            return True
            
        frequency = {}
        
        for element in a:
            frequency[element] = frequency.get(element, 0) + 1
            
        for element in b:
            if element not in frequency or frequency[element] == 0:
                return False
                
            frequency[element] -= 1
            
        return True
```