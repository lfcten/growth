import unittest


def wizard(g, start=0, end=9):
    cur = {start: 0}
    res = float("inf")
    while cur:
        temp = {}
        for ind, val in cur.items():
            for nx in g[ind]:
                cost = val + (nx - ind) ** 2
                if nx == end:
                    if res > cost:
                        res = cost
                else:
                    if nx not in temp:
                        temp[nx] = cost
                    else:
                        temp[nx] = min(temp[nx], cost)
        cur = temp
    return res


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(41, wizard({0: [4, 5], 4: [9], 5: [9]}))

