# Reverse Digits (GeeksforGeeks) - Basic

[GeeksforGeeks - Reverse Digits](https://www.geeksforgeeks.org/problems/reverse-digit0316/)

You are given an integer `n`. Your task is to reverse the digits, ensuring that the reversed number has no leading zeroes.

## Examples

> **Example 1:**
>
> **Input:** `n = 122`
>
> **Output:** `221`
>
> **Explanation:** By reversing the digits of the number, the number will change into `221`.

> **Example 2:**
>
> **Input:** `n = 200`
>
> **Output:** `2`
>
> **Explanation:** By reversing the digits of the number, the number will change into `2` (leading zeros removed).

> **Example 3:**
>
> **Input:** `n = 12345`
>
> **Output:** `54321`
>
> **Explanation:** By reversing the digits of the number, the number will change into `54321`.

## Constraints

- `1 <= n <= 10^6`

```python
class Solution:
	def reverseDigits(self, n):
	    if n < 10:
	        return n
	    
	    rev = 0
	    
	    while n > 0:
		    digit = n % 10
		    n = n // 10
		    
		    rev = rev * 10 + digit
		    
        return rev
```