from interval_tree import IntervalTree

a = IntervalTree()

a.add([15, 20])
a.add([10, 30])
a.add([5, 20])
a.add([12, 15])
a.add([17, 19])
a.add([30, 40])

a.display()

a.search([14, 16])
a.search([21, 23])
