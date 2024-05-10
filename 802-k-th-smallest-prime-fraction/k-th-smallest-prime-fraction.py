class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # I think this will be a two pointer question
        # The fact that the array in sorted make it that we don't have to solve it in try
        # Every possibility
        n = len(arr)
        low, high = 0, 1.0

        while low < high:
            mid = (low + high) / 2
            count, num, den = self.helper(arr, mid)

            if k < count:
                high = mid
            elif k > count:
                low = mid
            else:
                return [num, den]

        return []

    def helper(self, arr, target):
        count, i, n = 0, 0, len(arr)
        num, den = arr[0], arr[n - 1]

        for j in range(1, n):
            while i < j and arr[i] <= arr[j] * target:
                i += 1
            count += i
            if i > 0 and arr[i - 1] * den > arr[j] * num:
                num = arr[i - 1]
                den = arr[j]

        return [count, num, den]