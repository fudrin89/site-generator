# test_split_nodes_delimiter.py
import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_splits_single(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        out = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            out,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_bold_splits_single(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        out = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            out,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_italic_splits_single(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        out = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            out,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_non_text_nodes_pass_through(self):
        nodes = [
            TextNode("keep", TextType.BOLD),
            TextNode("This is _it_", TextType.TEXT),
        ]
        out = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(
            out,
            [
                TextNode("keep", TextType.BOLD),
                TextNode("This is ", TextType.TEXT),
                TextNode("it", TextType.ITALIC),
            ],
        )

    def test_multiple_delimited_sections(self):
        node = TextNode("a `b` c `d` e", TextType.TEXT)
        out = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            out,
            [
                TextNode("a ", TextType.TEXT),
                TextNode("b", TextType.CODE),
                TextNode(" c ", TextType.TEXT),
                TextNode("d", TextType.CODE),
                TextNode(" e", TextType.TEXT),
            ],
        )

    def test_no_delimiter_no_change(self):
        node = TextNode("plain text", TextType.TEXT)
        out = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(out, [node])

    def test_unmatched_delimiter_raises(self):
        node = TextNode("This is **broken", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_empty_delimiter_raises_value_error(self):
        node = TextNode("text", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()