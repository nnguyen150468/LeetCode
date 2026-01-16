class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            seen[tuple(sorted(word))].append(word)
        res = []
        for key, words in seen.items():
            res.append(words)
        return res