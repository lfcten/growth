class Solution:
    def regular_expression(self, s, p):
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*" and dp[i - 2][0]:
                dp[i][0] = True

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == "." or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == "*" or p[i - 1] == "+":
                    if p[i - 2] == "." or p[i - 2] == s[i - 2]:
                        if p[i - 1] == "*":
                            dp[i][j] = dp[i - 2][j] or dp[i - 2][j - 1] or dp[i][j - 1]
                        else:
                            dp[i][j] = dp[i - 2][j - 1] or dp[i][j - 1]
                    else:
                        dp[i][j] = p[i - 1] == "*" and dp[i - 2][j]


