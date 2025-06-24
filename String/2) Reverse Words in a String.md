## 151. Reverse Words in a String (Leetcode) - Medium

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

[Link for the question](https://leetcode.com/problems/reverse-words-in-a-string/description/)

**Example 1:**

> **Input:** `s = "the sky is blue"`  
> **Output:** `"blue is sky the"`

**Example 2:**

> **Input:** `s = "  hello world  "`  
> **Output:** `"world hello"`  
> **Explanation:**  
> Your reversed string should not contain leading or trailing spaces.

**Example 3:**

> **Input:** `s = "a good   example"`  
> **Output:** `"example good a"`  
> **Explanation:**  
> You need to reduce multiple spaces between two words to a single space in the reversed string.

**Constraints:**

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

#### Answer 1
```Python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        return ' '.join(reversed(words))
```

#### Answer 2
```Python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = 0
        j = 0
        string = ""

        while j <= len(s):
            if j == len(s) or s[j] == " ":
                if i != j:
                    word = s[i:j]
                    string = word + " " + string
                i = j + 1
            j += 1
            
        return string.strip()
```

**Note: The time complexity of strip() in Python is O(n), where n is the length of the string. This is because Python scans from both ends of the string to remove leading and trailing whitespace, which can take linear time in the worst case.**