class BellmanFord:
    def __init__(self, src, v, aList=None, eTuple=None):
        self.nV = v
        self.src = src
        self.listE = []
        self.D = {}
        if aList == None:
            listE = eTuple
        else:
            for node in aList.keys():
                self.D[node] = float('inf')
                for cnode in aList[node].keys():
                    self.listE.append((node, cnode, aList[node][cnode]))
        self.D[src] = 0
        self.nE = len(self.listE)

    def process(self):
        for i in range(0, self.nV - 1):
            for j in range(0, self.nE):
                s = self.listE[j][0]
                e = self.listE[j][1]
                w = self.listE[j][2]
                if self.D[s] + w < self.D[e]:
                    self.D[e] = self.D[s] + w

    def get_distance(self):
        return self.D
