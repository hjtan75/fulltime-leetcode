class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # The limitation of the question is only use linear time, and constant space
        # Because the xor of a operation could be reverse by it's own operation
        # Only two number will remain in the final result, the xor of the different number
        # how to do find the answer for each number, because both is different number
        # they have at least one bit different, we need the find that index of the bit
        # And then seperate the number into two groups, 
        # first group that has the bit to zero, the other is the bit to be one,
        # we xor every element in each group, the final value for both group will be the answer
        # if one number if negative 

        diff_idx = 0
        group_0, group_1 = 0, 0
        tmp = 0
        
        # xor all nums
        for n in nums:
            tmp ^= n

        while tmp > 0:
            if tmp & (1 << diff_idx) > 0:
                break
            diff_idx += 1

        print(diff_idx)
        if tmp > 0 :
            for n in nums:
                if n & (1 << diff_idx) == 0:
                    group_0 ^= n
                else:
                    group_1 ^= n

                print(group_0, group_1)
        else:
            for n in nums:
                if n >= 0:
                    group_0 ^= n
                else:
                    group_1 ^= n

        return [group_0, group_1]
            


