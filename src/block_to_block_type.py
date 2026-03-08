from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    # 1) Code blocks: start with ```\n and end with ```
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    # 2) Headings: 1-6 # characters, then a space
    for i in range(1, 7):
        if block.startswith("#" * i + " "):
            return BlockType.HEADING

    lines = block.split("\n")

    # 3) Quote blocks: every line starts with ">"
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # 4) Unordered list: every line starts with "- "
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # 5) Ordered list: lines start with "1. ", "2. ", ... incrementing by 1
    is_ordered = True
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED_LIST

    # 6) Default
    return BlockType.PARAGRAPH
