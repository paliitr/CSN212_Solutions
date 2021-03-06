class AvoidRoads:
    def checkIfBlocked(a, b, c, d, blockedRoads):
        '''
        Checks if travelling the road between (a, b) and (c, d) is forbidden
        '''
        if a < 0 or b < 0 or c < 0 or d < 0:
            return True
        check = [a, b, c, d]
        if check in blockedRoads:
            return True
        else:
            return False

    def calc(width, height, blockedRoads):
        '''
        Populates table with path lengths
        '''
        dp = []
        for i in range(height+1):
            row = []
            for j in range(width+1):
                row.append(0)
            dp.append(row)

        dp[0][0] = 1

        for i in range(0, height+1):
            for j in range(0, width+1):
                if not checkIfBlocked(i-1, j, i, j, blockedRoads):
                    dp[i][j] += dp[i-1][j]

                if not checkIfBlocked(i, j-1, i, j, blockedRoads):
                    dp[i][j] += dp[i][j-1]

        return dp[height][width]


    def processBlocked(string):
        '''
        Processes the input blocked path string into an array
        '''
        roads = string[1:-1].split(",")
        if roads[0] == '':
            return []
        finalRoads = []
        count = 0
        for road in roads:
            if count == 0:
                start = 1
            else:
                start = 2
            e = [int(a) for a in road[start:-1].split()]
            if e[0] > e[2] or e[1] > e[3]:
                e = e[2:] + e[:2]
            finalRoads.append(e)
            count += 1
        return finalRoads
