class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # We first have to sort the ballon based on the x_start
        # Then we see wheather the next balloon's x_start falls within the previous balloon's x_end
        # if is change end
        # else add one more arrow, then change the end to the new end

        points.sort(key= lambda x : x[0])
        end = points[0][1]
        arrows = 1

        for balloon in points[1:]:
            if balloon[0] > end:
                arrows += 1
                end = balloon[1]
            else:
                end = min(end, balloon[1])

        return arrows
