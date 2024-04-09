class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Parse the ticket from 0 to n-1 repeatedly
        # skip element with 0, decreament element > 0
        # Calculate seconds need for position k to be 0

        n = len(tickets)
        queue = [x for x in range(n)]
        time = 0

        while tickets[k] > 0:
            front_queue = queue.pop(0)
            tickets[front_queue] -= 1
            time += 1

            if tickets[front_queue] > 0:
                queue.append(front_queue)

        return time
