class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def willTheyMeet(s1, p1, s2, p2, target):
            # p1 will always be larger than p2, closer to target
            if s1 >= s2:
                return False
            
            t1 = (target - p1) / s1
            t2 = (target - p2) / s2

            if t1 >= t2:
                return True
                
            return False
            
                
        stack = []
        startingPoint = [-1] * target # map starting point to ith 
        
        for i in range(len(position)):
            startingPoint[position[i]] = i
            
        # print(startingPoint)
        startingPoint.reverse()
        
        for i in startingPoint:
            if i != -1:
                if not stack or not willTheyMeet(speed[stack[-1]], position[stack[-1]], \
                                             speed[i], position[i], target):
                    stack.append(i)

                
        return len(stack)