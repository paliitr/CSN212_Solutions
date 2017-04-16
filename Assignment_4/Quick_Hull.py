from Point import Point as p

class QuickHull:
    def __init__(self, points):
        self.points = points
        self.hull = []

    def printer(self, h):
        for i in h:
            print(str(i.x)+" "+str(i.y))

    def run(self):
        A = self.points
        N = len(A)
        A = sorted(A, key=lambda p:p.x)
        Top = [[]]
        Bot = [[]]
        Xmax = A[N-1]
        Xmin = A[0]
        M = self.slope(Xmin, Xmax)
        if M == False:
            return
        for i in range(1, N-1):
            if A[i] == A[i+1]:
                A.remove(A[i])
            if M < self.slope(Xmin, A[i]):
                Top.append(A[i])
            elif self.slope(Xmin, A[i]) == False:
                if A[i].y > Xmin.y:
                    Top.append(A[i])
                else:
                    Bot.append(A[i])
            elif M > self.slope(Xmin, A[i]):
                Bot.append(A[i])
        Top.remove(Top[0])
        Bot.remove(Bot[0])
        # print(Xmin)
        self.findhull_T(Top, Xmin, Xmax)
        self.findhull_B(Bot, Xmin, Xmax)
        # print(Xmax)

    def findhull_T(self, A, v1, v2):
        if len(A) == 1:
            # print(A[0])
            return A[0]
        if len(A) == 0:
            return
        C = self.Ymax(A)
        M1 = self.slope(v2, C)
        M2 = self.slope(v1, C)
        L = [[]]
        R = [[]]
        for i in range(len(A)):
            if A[i].x * M1 < A[i].x:
                if A[i].x < C.x:
                    R.append(A[i])
            if A[i].x * M2 < A[i].y:
                if A[i].x < C.x:
                    L.append(A[i])
        L.remove(L[0])
        R.remove(R[0])
        self.findhull_T(L, v1, C)
        self.findhull_T(R, v2, C)
        # print(C)
        return C

    def findhull_B(self, A, v1, v2):
        if len(A) == 1:
            # print(A[0])
            return A[0]
        if len(A) == 0:
            return
        C = self.Ymin(A)
        M1 = self.slope(v2, C)
        M2 = self.slope(v1, C)
        L = [[]]
        R = [[]]
        for i in range(len(A)):
            if A[i].x * M1 > A[i].y:
                if A[i].x > C.x:
                    R.append(A[i])
            if A[i].x * M2 > A[i].y:
                if A[i].x < C.x:
                    L.append(A[i])
        L.remove(L[0])
        R.remove(R[0])
        self.findhull_B(L, v1, C)
        self.findhull_B(R, v2, C)
        # print(C)
        return C

    def slope(self, a, b):
        if b.x == a.x:
            return False
        try:
            return float(b.y - a.y / b.x - a.x)
        except ZeroDivisionError:
            return False

    def Ymax(self, A):
        C = A[0]
        for i in range(len(A)):
            if C.y < A[i].y:
                C = A[i]
        return C

    def Ymin(self, A):
        C = A[0]
        for i in range(len(A)):
            if C.y > A[i].y:
                C=A[i]
        return C
