class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort the list first
        # Fill the empty space alternately, with the number 
        # if previous round was odd, skip the first empty spot
        # If the previous round was even, fill the first empty spot
        # TC: O(n log n), n is parsing through every elment to find empty space, 
        # each parsing will reduce the number by half 
        # MC: O(n)

        deck.sort()
        n = len(deck)
        res = [0] * n
        qu = deque(range(n))
     
        for card in deck:
            idx = qu.popleft()
            res[idx] = card
            if qu:
                qu.append(qu.popleft())
                
        return res
