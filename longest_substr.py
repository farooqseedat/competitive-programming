# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_mapping = {}
        current_length = 0
        i = 0

        for character in s:
            if character in char_mapping:
                max_length = max(current_length, max_length)

                start_index = i-current_length
                end_index = char_mapping[character]
                for k in range(start_index, end_index):
                    char_mapping.pop(s[k])

                current_length = i - char_mapping[character]
                char_mapping[character] = i

            else:
                char_mapping[character] = i
                current_length += 1
            i = i+1

        return max(max_length, current_length)
