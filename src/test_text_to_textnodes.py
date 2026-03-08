# test_text_to_textnodes.py
import unittest

from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_full_example(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            text_to_textnodes(text),
        )

    def test_plain_text(self):
        self.assertListEqual(
            [TextNode("hello", TextType.TEXT)],
            text_to_textnodes("hello"),
        )

    def test_only_image(self):
        text = "![alt](https://x.com/a.png)"
        self.assertListEqual(
            [TextNode("alt", TextType.IMAGE, "https://x.com/a.png")],
            text_to_textnodes(text),
        )

    def test_only_link(self):
        text = "[a](https://x.com)"
        self.assertListEqual(
            [TextNode("a", TextType.LINK, "https://x.com")],
            text_to_textnodes(text),
        )


if __name__ == "__main__":
    unittest.main()