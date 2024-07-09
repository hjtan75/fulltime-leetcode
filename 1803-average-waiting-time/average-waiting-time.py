class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # we create a current time which show the current time
        # If the new order is larger or same as current time, jump to the time
        # add the prepare time to get the finish time
        # subtract the finish time with customer's arrival time
        # Add the subtraction into the the sum
        # Divide that by the total number of customer
        # TC: O(n)
        # SC: O(1)

        num_cus, wait_sum = 0, 0
        curr_time = -1

        for arrival, time in customers:
            curr_time = max(curr_time, arrival)
            curr_time += time
            wait_sum += curr_time - arrival
            num_cus += 1

        return wait_sum / num_cus