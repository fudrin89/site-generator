# textnode_to_htmlnode.py
from leafnode import LeafNode
from textnode import TextType


def text_node_to_html_node(text_node):
    """
    Convert a TextNode into a LeafNode based on its TextType.

    Rules:
    - TEXT  -> LeafNode(None, text)
    - BOLD  -> LeafNode("b", text)
    - ITALIC-> LeafNode("i", text)
    - CODE  -> LeafNode("code", text)
    - LINK  -> LeafNode("a", text, {"href": url})
    - IMAGE -> LeafNode("img", "", {"src": url, "alt": text})

    Raises:
    - Exception if the TextType is invalid
    - ValueError if LINK/IMAGE is missing a URL
    """
    if text_node is None:
        raise ValueError("text_node is required")

    t = text_node.text_type
    text = text_node.text
    url = text_node.url

    if t == TextType.TEXT:
        return LeafNode(None, text)

    if t == TextType.BOLD:
        return LeafNode("b", text)

    if t == TextType.ITALIC:
        return LeafNode("i", text)

    if t == TextType.CODE:
        return LeafNode("code", text)

    if t == TextType.LINK:
        if not url:
            raise ValueError("LINK TextNode must have a url")
        return LeafNode("a", text, props={"href": url})

    if t == TextType.IMAGE:
        if not url:
            raise ValueError("IMAGE TextNode must have a url")
        return LeafNode("img", "", props={"src": url, "alt": text})

    raise Exception(f"Invalid TextType: {t}")