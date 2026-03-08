# test_split_nodes_image_link.py
import unittest

from textnode import TextNode, TextType
from split_nodes_image_link import split_nodes_image, split_nodes_link


class TestSplitNodesImageLink(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode("No images here", TextType.TEXT)
        self.assertListEqual([node], split_nodes_image([node]))

    def test_split_images_non_text_passthrough(self):
        node = TextNode("bold", TextType.BOLD)
        self.assertListEqual([node], split_nodes_image([node]))

    def test_split_images_at_start_and_end(self):
        node = TextNode(
            "![a](u) middle ![b](v)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("a", TextType.IMAGE, "u"),
                TextNode(" middle ", TextType.TEXT),
                TextNode("b", TextType.IMAGE, "v"),
            ],
            new_nodes,
        )

    def test_split_links_multiple(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )

    def test_split_links_no_links(self):
        node = TextNode("No links here", TextType.TEXT)
        self.assertListEqual([node], split_nodes_link([node]))

    def test_split_links_non_text_passthrough(self):
        node = TextNode("italic", TextType.ITALIC)
        self.assertListEqual([node], split_nodes_link([node]))

    def test_split_links_does_not_split_images(self):
        node = TextNode(
            "Image ![alt](https://img.com/x.png) and link [site](https://example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Image ![alt](https://img.com/x.png) and link ", TextType.TEXT),
                TextNode("site", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()