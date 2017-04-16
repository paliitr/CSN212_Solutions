from Point import Point as p
import functools

class GrahamScan:
    def __init__(self, pts):
        self.points = pts

    def cmp(self, a, b):
        return (a > b) - (a < b)

    def orientation(self, p, q, r):
        return self.cmp((q.x-p.x)*(r.y-p.y)-(r.x-p.x)*(q.y-p.y), 0)

    def printer(self, h):
        for i in h:
            print(str(i.x)+" "+str(i.y))

    def keep_left(self, hull, r):
        while len(hull) > 1 and self.orientation(hull[-2], hull[-1], r) != 0:
            hull = hull[:-1]
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    def run(self):
        pts = self.points
        pts = sorted(pts, key=lambda p: p.x)
        h1 = functools.reduce(self.keep_left, pts, [])
        h2 = functools.reduce(self.keep_left, reversed(pts), [])

        return h1.extend(h2[i] for i in range(1, len(h2)-1)) or h1
