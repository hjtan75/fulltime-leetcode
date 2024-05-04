class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Greedy algorithm,
        # Sort the people by weight, 
        # Use two pointer one in the front and the other at the back

        people = sorted(people)
        l, r = 0, len(people) - 1
        res = 0

        while l <= r:
            print(l, r, people[l] + people[r])
            if l == r:
                res += 1
                break
            if people[l] + people[r] <= limit:
                res += 1
                l += 1
                r -=1
            else:
                res += 1
                r -=1

        return res
            

