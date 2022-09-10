class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Instead of sorting all the word, just use an array to build a hashed map
        
        hashmap = {}
        for w in strs:
            arr = [0] * 26
            
            for c in w:
                arr[ord(c) - ord('a')] += 1
                
            hk = tuple(arr)
            if hk in hashmap:
                hashmap[hk].append(w)
            else:
                hashmap[hk] = [w]
                
        return hashmap.values()