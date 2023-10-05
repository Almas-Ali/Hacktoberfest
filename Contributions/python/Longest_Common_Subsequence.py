'''Implement LCS algorithm for A[1 .. n] and B[1 .. l] sequences.'''

def LCS(A , B, m, n):
    dp = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                dp[i][j] = 0
            elif A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    return dp[m][n]
if __name__ == '__main__':
    A = "AGGOUFYFKDJHFDTAB"
    B = "GXTXKSHDKDSKIUPAYB"
    m = len(A)
    n = len(B)
    print ("Length of LCS is", LCS(A, B, m, n) )
