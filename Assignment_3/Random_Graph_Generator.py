import random as r

class RandomGraphGenerator():
    def __init__(self, v=None, e=None):
        self.edge_list = []
        self.adjacency_list = {}
        self.max_w = 200

        if v is None:
            self.v = r.randint(1, 100)
        else:
            self.v = v

        if e is None:
            self.e = r.randint(1, 9900)
        else:
            self.e = e

        if self.e > self.v * (self.v - 1):
            self.e = self.v * (self.v - 1)

    def generate_edge_list(self):
        generated = []
        for i in range(self.e):
            a = r.randint(1, self.v)
            b = r.randint(1, self.v)
            while ((a, b) in generated) or (a == b):
                a = r.randint(1, self.v)
                b = r.randint(1, self.v)
            generated.append((a, b))
            w = r.randint(1, self.max_w)
            self.edge_list.append((a, b, w))

    def generate_adjacency_list(self):
        generated = []
        for i in range(1, self.v+1):
            self.adjacency_list.update({i:{}})
        for i in range(self.e):
            a = r.randint(1, self.v)
            b = r.randint(1, self.v)
            while ((a, b) in generated) or (a == b):
                a = r.randint(1, self.v)
                b = r.randint(1, self.v)
            generated.append((a, b))
            w = r.randint(1, self.max_w)
            self.adjacency_list[a].update({b:w})

    def get_edge_list(self):
        return self.edge_list

    def get_adjacency_list(self):
        return self.adjacency_list
