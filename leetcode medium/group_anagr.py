# brute force
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        used_words = set()
        for i, word1 in enumerate(strs):
            if word1 in used_words:
                continue
            used_words.add(word1)
            current = []
            for j in range(i, len(strs)):
                if (sorted(word1) == sorted(strs[j])):
                    current.append(strs[j])
                    used_words.add(strs[j])
            result.append(current)
        return result

# optimized
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        used_words = set()
        for i, word1 in enumerate(strs):
            if word1 in used_words:
                continue
            used_words.add(word1)
            current = []
            for j in range(i, len(strs)):
                if (sorted(word1) == sorted(strs[j])):
                    current.append(strs[j])
                    used_words.add(strs[j])
            result.append(current)
        return result

