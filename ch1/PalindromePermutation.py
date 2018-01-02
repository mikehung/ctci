import collections
import unittest


def palindrome_permutation(s):
    count = {}
    for c in s:
        if c == ' ':
            continue
        lowercase = c.lower()
        if lowercase in count:
            count[lowercase] += 1
        else:
            count[lowercase] = 1

    has_odd_key = False
    for key, num in count.items():
        if num % 2 != 0:
            if has_odd_key:
                return False
            has_odd_key = True

    return True


class Test(unittest.TestCase):
    def test_palindrome_permutation(self):
        data = [
            ('Tact Coa', True),
            ('jhsabckuj ahjsbckj', True),
            ('Able was I ere I saw Elba', True),
            ('So patient a nurse to nurse a patient so', False),
            ('Random Words', False),
            ('Not a Palindrome', False),
            ('no x in nixon', True),
            ('azAZ', True)
        ]
        for s, ans in data:
            print(s, ans)
            self.assertEqual(palindrome_permutation(s), ans)


if __name__ == '__main__':
    unittest.main()

