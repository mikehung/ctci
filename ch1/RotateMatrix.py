import unittest


def rotate(M):
    m = len(M)
    r0, c0, r1, c1 = 0, 0, m-1, m-1
    for r in range(m//2):
        for c in range(r, m-r-1):
            M[r0+r][c0+c], M[r0+c][c1-r], M[r1-r][c1-c], M[r1-c][c0+r] = \
                M[r1-c][c0+r], M[r0+r][c0+c], M[r0+c][c1-r], M[r1-r][c1-c]

    return M


class Test(unittest.TestCase):
    def test(self):
        M = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        expect = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5],
        ]
        self.assertEqual(rotate(M), expect)
        M = [
            [1, 2, 3, 4],
            [6, 7, 8, 9],
            [11, 12, 13, 14],
            [16, 17, 18, 19],
        ]
        expect = [
            [16, 11, 6, 1],
            [17, 12, 7, 2],
            [18, 13, 8, 3],
            [19, 14, 9, 4],
        ]
        self.assertEqual(rotate(M), expect)
        M = [
            [1, 2, 3],
            [6, 7, 8],
            [11, 12, 13],
        ]
        expect = [
            [11, 6, 1],
            [12, 7, 2],
            [13, 8, 3],
        ]
        self.assertEqual(rotate(M), expect)


if __name__ == '__main__':
    unittest.main()
