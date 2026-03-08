import unittest
from block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):

    # -------- Paragraph --------
    def test_paragraph(self):
        block = "This is just a paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # -------- Heading --------
    def test_heading_single_hash(self):
        block = "# Heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_six_hashes(self):
        block = "###### Heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_invalid_seven_hashes(self):
        block = "####### Heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_no_space(self):
        block = "#Heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # -------- Code --------
    def test_code_block(self):
        block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_invalid_no_newline(self):
        block = "```print('hello')```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # -------- Quote --------
    def test_quote_block(self):
        block = "> line one\n> line two\n> line three"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_block_invalid(self):
        block = "> line one\nline two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # -------- Unordered List --------
    def test_unordered_list(self):
        block = "- item one\n- item two\n- item three"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_invalid(self):
        block = "- item one\nitem two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # -------- Ordered List --------
    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_invalid_wrong_start(self):
        block = "2. first\n3. second"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_invalid_not_incrementing(self):
        block = "1. first\n3. second"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_invalid_missing_space(self):
        block = "1.first\n2.second"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()