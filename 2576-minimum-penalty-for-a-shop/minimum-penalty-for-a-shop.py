class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Calculate the penalty if the shop close at the lastest hour
        # Which is opened for the entire day
        # Shifting the closing time, but one unit earlier each time
        # Calculate the new penalty
        # If the penalty is lower, choose this closing time, if not shift again
        # Until it closes at the first hour
        # Time: O(n)
        # Memory: O(1)

        min_penalty, earliest_time = customers.count('N'), len(customers)
        total_penalty = min_penalty

        for i in range(len(customers)-1, -1, -1):
            if customers[i] == "Y":
                total_penalty += 1
            else:
                total_penalty -= 1
            if total_penalty <= min_penalty:
                earliest_time = i
                min_penalty = total_penalty

        return earliest_time

