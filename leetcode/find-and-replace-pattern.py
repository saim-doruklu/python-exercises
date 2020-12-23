from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            if self.is_matched_one_to_one(pattern, word):
                result.append(word)
        return result

    def is_matched_one_to_one(self, word_one, word_two):
        mappings = {}
        for index in range(word_one.__len__()):
            letter_one = word_one[index]
            letter_two = word_two[index]
            forward_mapping = mappings.get(letter_one)
            backward_mapping = mappings.get(letter_two.upper())
            if forward_mapping is None and backward_mapping is None:
                mappings[letter_one] = letter_two
                mappings[letter_two.upper()] = letter_one
            elif forward_mapping == letter_two or backward_mapping == letter_one:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"), ["mee", "aqq"])
