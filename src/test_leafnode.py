import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_node_with_tag(self):
        node = LeafNode("p", "Hello")
        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_leaf_node_with_props(self):
        node = LeafNode(
            "a",
            "Link",
            props={"href": "https://example.com"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://example.com">Link</a>',
        )

    def test_leaf_node_no_tag(self):
        node = LeafNode(value="Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_node_no_value_raises(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
