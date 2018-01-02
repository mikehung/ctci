import unittest


def urlify(url, length):
    beg = end = length - 1
    while url[beg] == ' ':
        beg -= 1

    while beg >= 0 <= end:
        if url[beg] == ' ':
            url[end-2:end+1] = '%20'
            beg, end = beg - 1, end - 3
        else:
            url[end] = url[beg]
            beg, end = beg - 1, end - 1

    return url


class Test(unittest.TestCase):
    def test_urlify(self):
        data = [
            (list('Mr. Mike Hung    '), 3+4+4+2*3, list('Mr.%20Mike%20Hung')),
            (list('Space at the end      '), 5+2+3+3+3*3, list('Space%20at%20the%20end')),
        ]
        for url, length, ans in data:
            self.assertEqual(urlify(url, length), ans)


if __name__ == '__main__':
    unittest.main()
