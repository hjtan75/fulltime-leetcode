class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Face-up: used power, gain 1 score
        # Face-down: Gain power, lose 1 token
        # Purpose is to gain maximum number of token

        # The purpose is to maximize, points
        # The best way to play it is to first sort the token in increasing order
        # If we are down on power, use point to gain power, starting the last element(most power for least score)
        # if we are down in points, use power to gain score, starting the frist element(1 score for least power)
        # Max-score record the maximum score for each iteration

        score, max_score, sorted_tokens = 0, 0, deque(sorted(tokens))

        while len(sorted_tokens) > 0:
            if power >= sorted_tokens[0]:
                score += 1
                power -= sorted_tokens.popleft()
            elif score > 0:
                score -= 1
                power += sorted_tokens.pop()
            else:
                break

            max_score = max(max_score, score)

        return max_score

                


        