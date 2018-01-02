import unittest


def zeroMatrix(M):
    if not M or not M[0]:
        return M
    m, n = len(M), len(M[0])
    zeroCol = [False] * n
    zeroRow = [False] * m

    for r in range(m):
        for c in range(n):
            if M[r][c] == 0:
                zeroRow[r] = zeroCol[c] = True

    for r in range(m):
        for c in range(n):
            if zeroRow[r] or zeroCol[c]:
                M[r][c] = 0

    return M

class Test(unittest.TestCase):
    def test(self):
        matrix = [
            [1, 2, 3, 10 ,0],
            [-1, 1, 2, 1, 3],
            [-1, 0, 2, 1, 3],
        ]
        expect = [
            [0, 0, 0, 0 ,0],
            [-1, 0, 2, 1, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(zeroMatrix(matrix), expect)

if __name__ == '__main__':
    unittest.main()
