import unittest


def isRotation(s1, s2):
    return len(s1) == len(s2) and s1 in s2*2


class Test(unittest.TestCase):
    def test(self):
        data = (
        ('a', 'abc', False),
        ('ab', 'ab', True),
        ('ab', 'ba', True),
        ('aba', 'ab', False),
        ('4bc', '4bc', True),
        ('4bc', 'bc4', True),
        ('4bc', 'cb4', True),
        ('waterbottle', 'erbottlewat', True),
        )
        pass


if __name__ == '__main__':
    unittest.main()
