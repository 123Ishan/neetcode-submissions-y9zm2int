class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            current_str = ""
            for j in range(i, len(s)):
                if s[j] in current_str:
                    break
                current_str += s[j]
                max_len = max(max_len, len(current_str))
        return max_len
        