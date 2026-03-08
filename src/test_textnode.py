import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node1 = TextNode("A", TextType.BOLD)
        node2 = TextNode("B", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_url(self):
        node1 = TextNode("Same text", TextType.LINK, None)
        node2 = TextNode("Same text", TextType.LINK, "https://example.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()