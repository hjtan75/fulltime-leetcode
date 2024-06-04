class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # The straight forward method would be to find every factor in n
        # This could be done iterating from 1 to n, after all facters are found
        # return the kth factor or return -1 if k is larger than the number of factors

        # The idea i could think of is binary search, because the range of factors lies within
        # [1, n]
        # we only have to iterate from 1 to sqrt(n) because the factor will range from 1 ,n
        # And the largest value on the first half would be sqrt(n) because sqrt(n)*sqrt(n) = n
        # we create two array, one store from the smallest array 
        # the second store starting from the biggest array
        # from i to int(sqrt(n)), we check if n is a divisible by i, add i to small and 
        # add n / i to big
        # return value based on whether thare are in the small or big array
        # If k > small.size + big.size, return -1

        small, big = [], []
        sqrt_n = n ** 0.5
        

        for i in range(1, ceil(sqrt_n)):
            if n % i == 0:
                small.append(i)
                big.append(n // i)

        if sqrt_n == int(sqrt_n):
            small.append(int(sqrt_n))

        if k <= len(small):
            return small[k-1]
        if k <= len(small) + len(big):
            return big[len(big) - (k - len(small))]
        else:
            return -1