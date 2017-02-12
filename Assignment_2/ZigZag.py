def longestSequence(seq):
    result = 1
    dp = []
    for i in range(len(seq)):
        dp.append([0, 0])
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(len(seq)):
        j = i-1
        while j>=0:
            if seq[j] < seq[i]:
                dp[i][0] = dp[j][1] + 1 if dp[j][1] + 1 >= dp[i][0] else dp[i][0]
            if seq[j] > seq[i]:
                dp[i][1] = dp[j][0] + 1 if dp[j][0] + 1 >= dp[i][1] else dp[i][1]
            j -= 1
        result0 = dp[i][0] if dp[i][0] >= dp[i][1] else dp[i][1]
        result = result0 if result0 >= result else result
    return result

print(longestSequence([int(a) for a in str(input()).split(",")]))
