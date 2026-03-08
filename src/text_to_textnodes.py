# text_to_textnodes.py
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image_link import split_nodes_image, split_nodes_link


def text_to_textnodes(text: str):
    """
    Convert a raw markdown-ish string into a list of TextNodes by applying
    all splitting steps in a safe order.

    Order matters:
    - Split images first (so image syntax doesn't get treated like links)
    - Split links next
    - Then split inline code, bold, italic delimiters on remaining TEXT nodes
    """
    if text is None:
        raise ValueError("text is required")

    nodes = [TextNode(text, TextType.TEXT)]

    # Images first, then links (important)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    # Inline code first, then bold, then italic (common safe order)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return nodes