def longestSequence(seq):

    '''
    The functions input should be an array containing integers.
    It will return the length of longest iterating subsequence.

    >>>longestSequence([5 3 4 2 5 6 7])
    5
    '''
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

def main():
    '''
    Input should be in the format of integers seperated by commas
    Prints an output denoting length of longest iterating subsequence
    '''
    print(longestSequence([int(a) for a in str(input()).split(",")]))

if __name__=="__main__":
    main()
