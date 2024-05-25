class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        adj = [[] for _ in range(n)]
        
        # Build the adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # dp[node][0] - max sum when node is not XORed
        # dp[node][1] - max sum when node is XORed
        dp = [[0, 0] for _ in range(n)]
        visited = [False] * n
        
        def dfs(node):
            visited[node] = True
            dp[node][0] = nums[node]
            dp[node][1] = nums[node] ^ k
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
                    
                    # If the current node is not XORed
                    dp[node][0] += max(dp[neighbor][0], dp[neighbor][1])
                    
                    # If the current node is XORed
                    dp[node][1] += max(dp[neighbor][0], dp[neighbor][1])
        
        dfs(0)
        
        return max(dp[0][0], dp[0][1])

# Example usage
solution = Solution()
nums = [24, 78, 1, 97, 44]
k = 6
edges = [[0, 2], [1, 2], [4, 2], [3, 4]]
result = solution.maximumValueSum(nums, k, edges)
print(f"The maximum possible sum is {result}")
