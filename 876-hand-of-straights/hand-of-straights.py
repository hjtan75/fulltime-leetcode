class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # First we have to check if whether len(hand) % group size == 0,
        # if not return false, we have to the array

        # We use a hashmap to store the frequency of each number in hand
        # Then we sort all the distinct number in the array
        # first we take a number from the front of the array, then find weather
        # val + 1 is in the hashmap, if yes decrement, if not return false
        # if hashmap decreament until 0, remove from the array
        # O(n log n) for sorting
        # SP: O(n)

        if len(hand) % groupSize != 0:
            return False

        counter = {}
        distinct_arr = []
        for card in hand:
            if card in counter:
                counter[card] += 1
            else:
                counter[card] = 1
                distinct_arr.append(card)

        distinct_arr = sorted(distinct_arr, reverse=True)
        while len(distinct_arr) > 0:
            stack_len, stack_val = 0, 0
            while stack_len < groupSize:
                if stack_len == 0:
                    if len(distinct_arr) == 0:
                        return False
                    stack_val = distinct_arr[-1]
                else:
                    if (stack_val + 1) not in counter or counter[stack_val + 1] == 0:
                        return False
                    else:
                        stack_val += 1

                counter[stack_val] -= 1
                stack_len += 1
                if counter[stack_val] == 0:
                    distinct_arr.pop()

        return True



        



