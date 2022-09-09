class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            w = "".join(sorted(word))
            # print(w)
            if w in dic:
                dic[w].append(word)
            else:
                dic[w] = [word]
                
        res = []
        for k, v in dic.items():
            res.append(v)
            
        return res