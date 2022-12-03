class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a two-dimensional dp array where dp[i][j] represents
        # whether s[:i] matches p[:j].
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Initialize the first row and column of the dp array.
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

    # Fill in the dp array according to the rules described above.
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j]
                else:
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == '.') and dp[i - 1][j - 1]

        # Return whether s matches p.
        return dp[len(s)][len(p)]