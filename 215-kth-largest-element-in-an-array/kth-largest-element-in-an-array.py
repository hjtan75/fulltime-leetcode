class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(start, end, arr, k):
            pivot_value = arr[end]
            pivot_point = start

            for i in range(start, end):
                if arr[i] <= pivot_value:
                    arr[i], arr[pivot_point] = arr[pivot_point], arr[i]
                    pivot_point += 1

            arr[pivot_point], arr[end] = arr[end], arr[pivot_point]
            if arr[start] == arr[end] and k >= start and k <= end:
                return arr[k]

            if pivot_point == len(arr) - k:
                return arr[pivot_point]
            elif pivot_point < len(arr) - k:
                return quickselect(pivot_point+1, end, arr, k)
            else:
                return quickselect(start, pivot_point-1, arr, k)

        return quickselect(0, len(nums)-1, nums, k)