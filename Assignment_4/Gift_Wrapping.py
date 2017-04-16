from Point import Point as p

class GiftWrapping:
    def __init__(self, points):
        self.points = points
        self.hull = []

    def orientation(self, p, q, r):
        diff = (r.x-p.x)*(q.y-p.y)-(q.x-p.x)*(r.y-p.y)
        return diff

    def printer(self, h):
        for i in h:
            print(str(i.x)+" "+str(i.y))

    def run(self):
        pts = self.points
        start = pts[0]
        min_x = start.x
        for p in pts[1:]:
            if p.x < min_x:
                min_x = p.x
                start = p

        point = start
        self.hull.append(start)

        fp = None
        while fp is not start:
            p1 = None
            for p in pts:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            fp = p1

            for p2 in pts:
                if p2 is point or p2 is p1:
                    continue
                else:
                    dn = self.orientation(point, fp, p2)
                    if dn > 0:
                        fp = p2

            self.hull.append(fp)
            point = fp
        return self.hull
