import unittest

def unique_0(s):
    dic = {}
    for c in s:
        if c in dic:
            return False
        dic[c] = True
    return True


def unique_1(s):
    return len(s) == len(set(s))


class Test(unittest.TestCase):
    def test_unique(self):
        data = [
            ('', True),
            ('abc', True),
            ('aaa', False),
            ('abcbad', False),
        ]
        for k, v in globals().items():
            if k.startswith('unique_'):
                for s, r in data:
                    self.assertEqual(v(s), r)


if __name__ == '__main__':
    unittest.main()
