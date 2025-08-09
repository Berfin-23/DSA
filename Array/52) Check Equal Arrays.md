# Check Equal Arrays (GeeksforGeeks) - Easy

[GeeksforGeeks - Check Equal Arrays](https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article)

Given two arrays `a[]` and `b[]` of equal size, the task is to find whether the elements in the arrays are equal.

Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.

**Note:** If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

## Examples

> **Example 1:**
>
> **Input:** `a[] = [1, 2, 5, 4, 0]`, `b[] = [2, 4, 5, 0, 1]`
>
> **Output:** `true`
>
> **Explanation:** Both the arrays can be rearranged to `[0, 1, 2, 4, 5]`.

> **Example 2:**
>
> **Input:** `a[] = [1, 2, 5]`, `b[] = [2, 4, 15]`
>
> **Output:** `false`
>
> **Explanation:** `a[]` and `b[]` have only one common value.

## Constraints

- `1 ≤ a.size(), b.size() ≤ 10^7`
- `0 ≤ a[i], b[i] ≤ 10^9`

```python
class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
    
        frequency = {}
        for element in a:
            frequency[element] = frequency.get(element, 0) + 1
        
        for element in b:
            if element not in frequency:
                return False
            
            frequency[element] -= 1
            
            if frequency[element] == 0:
                del frequency[element]
    
        return len(frequency) == 0
```