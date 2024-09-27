def decode_message(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    # Create a DP table of size (m+1) x (n+1) initialized to False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: Empty pattern matches an empty message
    dp[0][0] = True
    
    # Fill the first row, handling patterns starting with *
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    # Return the final answer
    return dp[m][n]

# Taking user input for the message and the pattern
message = input("Enter the secret message: ")
pattern = input("Enter the decoder key (pattern): ")

# Calling the decode_message function with user inputs
if decode_message(message, pattern):
    print("True")
else:
    print("False")