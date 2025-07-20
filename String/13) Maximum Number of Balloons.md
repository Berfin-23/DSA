# 1189. Maximum Number of Balloons (LeetCode) - Easy

Given a string `text`, you want to use the characters of `text` to form as many instances of the word `"balloon"` as possible.

You can use each character in `text` at most once. Return the maximum number of instances that can be formed.

[Link for the question](https://leetcode.com/problems/maximum-number-of-balloons/)

## Examples

**Example 1:**

![Maximum Number of Balloons Example 1](../images/maximum_number_of_balloons_1.png)

> **Input:** `text = "nlaebolko"` > **Output:** `1`

**Example 2:**

![Maximum Number of Balloons Example 2](../images/maximum_number_of_balloons_2.png)

> **Input:** `text = "loonbalxballpoon"` > **Output:** `2`

**Example 3:**

> **Input:** `text = "leetcode"` > **Output:** `0`

## Constraints

- `1 <= text.length <= 10^4`
- `text` consists of lower case English letters only.

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashMap = {}
        for letter in text:
            hashMap[letter] = hashMap.get(letter, 0) + 1

        balloon = {}
        for letter in "balloon":
            balloon[letter] = balloon.get(letter, 0) + 1

        result = len(text)

        for letter in balloon:
            if letter not in hashMap:
                return 0
            result = min(result, hashMap[letter] // balloon[letter])

        return result
```
