class Solution:
    def combinationSum2(self, candidates, target):
        def backtrack(remain, curr_combination, start):
            if remain == 0:
                result.append(list(curr_combination))
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                curr_combination.append(candidates[i])
                backtrack(remain - candidates[i], curr_combination, i + 1)
                curr_combination.pop()

        result = []
        candidates.sort()
        backtrack(target, [], 0)
        return result
