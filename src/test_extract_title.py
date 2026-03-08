# test_extract_title.py
import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_extract_title_strips(self):
        self.assertEqual(extract_title("#   Hello  "), "Hello")

    def test_extract_title_first_h1(self):
        md = "# First\n\n# Second"
        self.assertEqual(extract_title(md), "First")

    def test_no_h1_raises(self):
        md = "## Not H1\nParagraph"
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()