class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Calculate the rank of each city
        # Sort the city by rank
        # Take i and i+1 city, add their rank, if they are connected minus 1
        # if n > 2, and rank(i) + rank(i+1) > rank(i+1) + rank(i+2)
        # return rank(i) + rank(i+1)
        # Time: O(n^2) road parsing
        # Memory: O(n) record rank of each city
        if n == 2:
            return len(roads)

        rank = {}
        rank_to_pair = [] # (rank, a)

        for i in range(n):
            rank[i] = set()

        for a, b in roads:
            rank[a].add(b)
            rank[b].add(a)

        for k, v in rank.items():
            rank_to_pair.append([len(v), k])

        rank_to_pair = sorted(rank_to_pair, reverse=True)

        max_rank = 0
        # for i in range(1, len(rank_to_pair)-1):
        #     combined_rank = rank_to_pair[0][0] + rank_to_pair[i][0]
        #     if rank_to_pair[0][1] in rank[rank_to_pair[i][1]]:
        #         combined_rank -= 1

        #     max_rank = max(max_rank, combined_rank)

        for i in range(n):
            for j in range(i+1, n):
                combined_rank = rank_to_pair[i][0] + rank_to_pair[j][0]
                if rank_to_pair[i][1] in rank[rank_to_pair[j][1]]:
                    combined_rank -= 1

                max_rank = max(max_rank, combined_rank)


        return max_rank
        