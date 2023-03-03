'''
Approach:
1. Iterate over every substring of length equal to that of the needle in the haystack using a sliding window approach
2. Check if the first letter of the current substring matches the first letter of the needle
3. If it does, compare the current substring with the needle
4. If they match, return the starting index of the current substring in the haystack
5. If no match is found, return -1

Time Complexity: O((N-L)L), where N is the length of haystack and L is the length of needle

Worst-Case: 
When all characters of the haystack are same and equal to the first character of the needle. 
In that case, we will be checking all the substrings of length L in the haystack
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay_len = len(haystack)
        needle_len = len(needle)

        for index, char in enumerate(haystack[:hay_len - needle_len + 1]):
            if char == needle[0] and haystack[index:index + needle_len] == needle:
                return index

        return -1
