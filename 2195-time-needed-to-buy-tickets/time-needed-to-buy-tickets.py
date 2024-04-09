class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Parse the ticket from 0 to n-1 repeatedly
        # skip element with 0, decreament element > 0
        # Calculate seconds need for position k to be 0

        time = 0
        idx = 0
        n = len(tickets)
        while tickets[k] > 0:
            if idx > n - 1:
                idx = 0
                continue
            if tickets[idx] == 0:
                idx += 1
                continue
            else:
                tickets[idx] -= 1
                idx += 1
                time += 1

        return time
        