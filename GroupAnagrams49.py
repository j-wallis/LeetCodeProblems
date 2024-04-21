class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)

        for s in strs:
            count = [0]*26

            for char in s:
                count[ord(char)-ord("a")] += 1

            map1[tuple(count)].append(s)

        return map1.values()
