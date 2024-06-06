class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # First we have to check if whether len(hand) % group size == 0,
        # if not return false, we have to the array

        # We can sort the array, and we need to find the trasition point in the array
        # we parse throught the array and add it to and stack.
        # we only add to stack when hand[0] == stack[i] + 1
        # if stack == groupsize, clear stack, if hand[-1] > stack[-1] + 1, return false
        # if hand[-1] <= stack[i] , i -=1
        # TC: O(n^2), that is worst case which will never happend, because in that case,
        # the function would have return false on the first run, is there is a solution
        # Imporve by binary search log n
        # TC: O()
        # SC: O(n), which can be optimized, we can have one variable marking the size and 
        # the other marking the value of the last element in the stack
        if len(hand) % groupSize != 0:
            return False

        hand = sorted(hand)
        while len(hand) > 0:
            i = 0
            stack_len, stack_val = 0, 0
            while i < len(hand) and stack_len < groupSize:
                if stack_len == 0 or hand[i] == stack_val + 1:
                    stack_val = hand[i]
                    stack_len += 1
                    del hand[i]
                elif hand[i] <= stack_val:
                    i += 1
                else:
                    print('a')
                    return False

            if stack_len != groupSize:
                print("b")
                return False

        return True



