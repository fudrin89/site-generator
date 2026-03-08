import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_block(self):
        md = "Just one paragraph"
        self.assertEqual(markdown_to_blocks(md), ["Just one paragraph"])

    def test_multiple_blank_lines(self):
        md = "One\n\n\n\nTwo"
        self.assertEqual(markdown_to_blocks(md), ["One", "Two"])

    def test_leading_trailing_whitespace(self):
        md = "\n\n  Hello  \n\n  World \n\n"
        self.assertEqual(markdown_to_blocks(md), ["Hello", "World"])

    def test_empty_input(self):
        self.assertEqual(markdown_to_blocks(""), [])


if __name__ == "__main__":
    unittest.main()