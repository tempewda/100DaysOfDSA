## [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Example 1:**
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```
**Example 2:**
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
``` 

**Constraints:**

- `1 <= haystack.length, needle.length <= 104`
- `haystack` and `needle` consist of only lowercase English characters.

**Solutions:**
<table>
  <tr>
    <th></th> <th>Time Complexity</th> <th>Approach Used</th> <th>Solution</th>
  </tr>
    <tr>
    <td>1</td> <td>O((N-L)L)</td> <td>Brute Force</td> <td><a href="https://github.com/ArrowA1/100DaysOfDSA/blob/master/Day3/Brute_Force.py">Click Here</a></td>
  </tr>

</table>
