class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            cnt = [0] * 26
            for current in s:
                # get the ascii value and store it as index
                cnt[ord(current) - ord("a")] += 1
            
            res[tuple(cnt)].append(s)
        return res.values()
        