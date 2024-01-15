class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # A dictionary created if a player participate in a match
        # The dictionary record the number of losses
        # Parse the dictionary, record play with zero or 1 loses into answer
        # Time: O(m)
        # Memory: O(P)

        loss_record = {}
        ans = []
        ans.append([])
        ans.append([])

        for winner, loser in matches:
            loss_record[winner] = loss_record.get(winner, 0)
            loss_record[loser] = loss_record.get(loser, 0) + 1

        for player, loss_cnt in loss_record.items():
            if loss_cnt == 0:
                ans[0].append(player)
            elif loss_cnt == 1:
                ans[1].append(player)

        ans[0].sort()
        ans[1].sort()
        return ans

