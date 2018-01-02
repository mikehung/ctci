import unittest

def compression(string):
    if not string:
        return string
    lst = []
    char, count = string[0], 1
    for c in string[1:]:
        if c == char:
            count += 1
        else:
            lst.append('{}{}'.format(char, count))
            char, count = c, 1
    lst.append('{}{}'.format(char, count))
    return min(string, ''.join(lst), key=len)


class Test(unittest.TestCase):
    def test(self):
        data = (
            ('a', 'a'),
            ('aa', 'aa'),
            ('ab', 'ab'),
            ('aabcccccaaa', 'a2b1c5a3'))

        for string, expect in data:
            self.assertEqual(compression(string), expect)

if __name__ == '__main__':
    unittest.main()
