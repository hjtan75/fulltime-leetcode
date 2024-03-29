class Solution:
    def customSortString(self, order: str, s: str) -> str:
        alpha_count = {}
        res = []
        for alpha in s:
            alpha_count[alpha] = alpha_count.get(alpha, 0) + 1


        for alpha in order:
            res.append(alpha * alpha_count.pop(alpha, 0))

        for k, v in alpha_count.items():
            for _ in range(v):
                res.append(k)

        return ''.join(res)