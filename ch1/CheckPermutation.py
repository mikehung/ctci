import collections
import unittest


def count(s):
    cnt = {}
    for c in s:
        if c not in cnt:
            cnt[c] = 1
        else:
            cnt[c] += 1
    return cnt


def check_permutation_0(s1, s2):
    if len(s1) != len(s2):
        return False

    cnt1, cnt2 = count(s1), count(s2)
    for char, num in cnt1.items():
        if char not in cnt2 or cnt2[char] != num:
            return False
    return True


def check_permutation_0(s1, s2):
    return collections.Counter(s1) == collections.Counter(s2)


class Test(unittest.TestCase):
    def test_check_permutation(self):
        data = [
            ('', '', True),
            ('abca', 'abca', True),
            ('abac', 'baca', True),
            ('abca', 'bbca', False),
            ('abca', 'abcab', False),
        ]
        for k, v in globals().items():
            if k.startswith('check_permutation_'):
                for s1, s2, ans in data:
                    self.assertEqual(v(s1, s2), ans)


if __name__ == '__main__':
    unittest.main()
