class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur_list):
            if sum(cur_list) == target:
                res.append(cur_list.copy())
                return
            
            for j in range(i, len(nums)):
                if target < sum(cur_list) + nums[j]:
                    return
                cur_list.append(nums[j])
                dfs(j, cur_list)
                cur_list.pop()
            
        
        dfs(0, [])
        return res