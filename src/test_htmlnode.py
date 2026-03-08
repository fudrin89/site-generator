import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple_props(self):
        node = HTMLNode(
            "a",
            "Google",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_props_to_html_none(self):
        node = HTMLNode("p", "Hello", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_dict(self):
        node = HTMLNode("p", "Hello", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_repr_contains_fields(self):
        node = HTMLNode("p", "Hi", children=[], props={"class": "x"})
        r = repr(node)
        self.assertIn("tag='p'", r)
        self.assertIn("value='Hi'", r)
        self.assertIn("children=", r)
        self.assertIn("props=", r)


if __name__ == "__main__":
    unittest.main()
