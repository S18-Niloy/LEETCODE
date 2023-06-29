class Solution:
    def combinationSum(self, candidates, target):
        results = []
        self.backtrack(candidates, target, [], results)
        return results
    
    def backtrack(self, candidates, target, combination, results):
        if target == 0:
            results.append(combination)
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            self.backtrack(candidates[i:], target - candidates[i], combination + [candidates[i]], results)
