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
        for card in hand:
            counter[card] = counter.get(card, 0) + 1

        distinct_arr = sorted(counter.keys())
        
        for key in distinct_arr:
            if counter[key] > 0:
                freq = counter[key]
                for i in range(key, key + groupSize):
                    if i not in counter or counter[i] < freq:
                        return False
                    counter[i] -= freq
        return True



        



