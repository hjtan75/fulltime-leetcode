class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort the list first
        # Fill the empty space alternately, with the number 
        # if previous round was odd, skip the first empty spot
        # If the previous round was even, fill the first empty spot
        # TC: O(n log n), n is parsing through every elment to find empty space, 
        # each parsing will reduce the number by half 
        # MC: O(n)

        deck.sort(reverse=True)
        n = len(deck)
        res = [0] * n
        skip_flag = False

        while len(deck) > 0:
            for i in range(n):
                if res[i] == 0:
                    if skip_flag:
                        skip_flag = False
                        continue
                    res[i] = deck.pop()
                    skip_flag = True

        # print(res)
        return res
