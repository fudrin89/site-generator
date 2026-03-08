# split_nodes_delimiter.py
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Split TextType.TEXT nodes by a markdown delimiter into alternating TEXT and `text_type` nodes.

    Example:
      TextNode("a **b** c", TEXT) with delimiter="**", text_type=BOLD
      -> [TextNode("a ", TEXT), TextNode("b", BOLD), TextNode(" c", TEXT)]

    Rules:
    - Only split nodes whose text_type is TextType.TEXT. Others pass through unchanged.
    - If a TEXT node has an unmatched delimiter (odd number of delimiter occurrences), raise Exception.
    - Empty segments are allowed and typically skipped (except plain text segments can be empty in theory).
    """
    if delimiter is None or delimiter == "":
        raise ValueError("delimiter must be a non-empty string")

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        # If no delimiter present, keep node as-is
        if delimiter not in text:
            new_nodes.append(node)
            continue

        parts = text.split(delimiter)

        # Valid markdown requires pairs of delimiters => odd number of parts
        # Example: "a **b** c" split by "**" -> ["a ", "b", " c"] (len=3, odd) OK
        # Example: "a **b c" split by "**" -> ["a ", "b c"] (len=2, even) INVALID
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid markdown syntax: missing closing delimiter '{delimiter}' in '{text}'")

        # parts at even indices are TEXT, odd indices are the delimited content
        for i, part in enumerate(parts):
            if part == "":
                # skip empty segments to avoid creating empty nodes
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes