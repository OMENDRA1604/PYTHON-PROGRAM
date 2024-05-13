def is_match(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    # Create a 2D DP table to store intermediate results
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty pattern matches empty string
    dp[0][0] = True
    
    # Initialize the first row (empty string s)
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill in the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
    
    return dp[m][n]

# Example usage
s1, p1 = "aa", "a"
print(f"Output for s = '{s1}', p = '{p1}': {is_match(s1, p1)}")

s2, p2 = "aa", "*"
print(f"Output for s = '{s2}', p = '{p2}': {is_match(s2, p2)}")

s3, p3 = "adceb", "*a*b"
print(f"Output for s = '{s3}', p = '{p3}': {is_match(s3, p3)}")
