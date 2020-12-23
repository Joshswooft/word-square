import unittest
from collections import Counter
from word_square import check_solution_is_valid, generate_word_square


class WordSquareTestCase(unittest.TestCase):

    def test_invalid_square(self):
        with self.assertRaises(AssertionError):
            generate_word_square(-1, "foo")

    def test_check_solution_is_valid(self):
        words = ["rose", "oven", "send", "ends"]
        n = 4
        res = check_solution_is_valid(words=words, square_size=n)
        self.assertTrue(res)

    def test_check_solution_invalid_length(self):
        words = ["rose", "oven", "send", "ends"]
        n = 8
        res = check_solution_is_valid(words, n)
        self.assertFalse(res)

    def test_check_solution_invalid_words(self):
        words = ['foo', 'bar', 'baz']
        n = 3
        res = check_solution_is_valid(words, n)
        self.assertFalse(res)

    def test_generates_square(self):
        testCases = [
            {
                "size": 4,
                "word": 'eeeeddoonnnsssrv',
                "want": ['rose', 'oven', 'send', 'ends']
            },
            {
                "size": 4,
                "word": "aaccdeeeemmnnnoo",
                "want": ["moan", "once", "acme", "need"]
            },
            {   
                "size": 5,
                "word": "aaaeeeefhhmoonssrrrrttttw",
                "want": ["feast", "earth", "armer", "steno", "throw"]
            },
            {
                "size": 5,
                "word": "aabbeeeeeeeehmosrrrruttvv",
                "want": ['heart', 'ember', 'above', 'revue', 'trees']
            },
            {
                "size": 7,
                "word": "aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy",
                "want": ["bravado", "renamed", "analogy", "valuers", "amoebas", "degrade", "odyssey"]
            },
        ]

        for test in testCases:
            res = generate_word_square(test['size'], test['word'])
            c = Counter("".join(r for r in res))
            c2 = Counter(test['word'])
            self.assertEqual(c, c2)
            self.assertTrue(check_solution_is_valid(res, test['size']))
            self.assertEqual(res, test['want'])
        
if __name__ == '__main__':
    unittest.main()
