class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dic = defaultdict(int)
        
        def dfs(index, total):          
            key = (index, total)
            
            if key not in dic:
                if index == len(nums):                    
                    return 1 if total == target else 0
                else:
                    dic[key] = dfs(index + 1, total + nums[index]) + dfs(index + 1, total - nums[index])                    
                        
            return dic[key]                                                             
                
        return dfs(0, 0)
