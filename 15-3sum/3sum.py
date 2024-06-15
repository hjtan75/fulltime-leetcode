class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The brute force would be listing every possiblity of i, j, k
        # This will have time complexity of O(n^3)
        # Not ideal

        # The other method is to use the 2 sum method, 
        # Because the optmized two sum method uses O(n) but using a set
        # So we might able to use that method to slve 3sum in O(n^2) time, 
        # we create a set with the sum of every possible 2 sum
        # for every new value we search in the set weather it have a negative avalue in the set
        # this will not work because creaating every possiblity in the set would reaquire O(n^2)

        # What we can do is sort the array
        # for every possibities for every possiblities of i and j, 
        # then we create a hashmap from nums with value as key and idx as num
        # This will require O(n^2) for every possiblity because we gonna iterate every
        # possibilities for i and j and find k in hashmap only require O(1)
        # Space complexity is O(n) for hash, map
        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,1,2]

        val_dict = {}
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if nums[i] not in val_dict:
                val_dict[nums[i]] = set()
            val_dict[nums[i]].add(i)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                val = nums[i] + nums[j]
                if (-val) in val_dict:
                    if (len(val_dict[-val]) <= 2 and i not in val_dict[-val] and j not in val_dict[-val]):
                        for k in val_dict[-val]:
                             if i != k and j != k:
                                s = ','.join(sorted([str(nums[i]), str(nums[j]), str(nums[k])]))
                                res.add(s)
                                break
                                
                    if len(val_dict[-val]) > 2:
                        for k in val_dict[-val]:
                            if  i != k and j != k:
                                s = ','.join(sorted([str(nums[i]), str(nums[j]), str(nums[k])]))
                                res.add(s)
                                break
        res = list(res)
        for i in range(len(res)):
            res[i] = res[i].split(',')
            res[i] = [int(s) for s in res[i]]

        return res
