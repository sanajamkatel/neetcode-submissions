class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for strings in strs:
            sorted_str = " ".join(sorted(strings))

            if sorted_str not in hash_map:
                hash_map[sorted_str] = []

            hash_map[sorted_str].append(strings)

        return list(hash_map.values())

