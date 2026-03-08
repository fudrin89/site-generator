# split_nodes_image_link.py
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    """
    Split TextType.TEXT nodes into TEXT + IMAGE + TEXT ... based on markdown images: ![alt](url)
    Non-TEXT nodes pass through unchanged.
    """
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_images(text)

        # No images -> keep node as-is
        if not matches:
            new_nodes.append(node)
            continue

        remainder = text
        for alt, url in matches:
            markdown = f"![{alt}]({url})"

            # Split only on the first occurrence (important when multiple images exist)
            before, after = remainder.split(markdown, 1)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            remainder = after

        if remainder:
            new_nodes.append(TextNode(remainder, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    """
    Split TextType.TEXT nodes into TEXT + LINK + TEXT ... based on markdown links: [text](url)
    Non-TEXT nodes pass through unchanged.
    """
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_links(text)

        # No links -> keep node as-is
        if not matches:
            new_nodes.append(node)
            continue

        remainder = text
        for anchor, url in matches:
            markdown = f"[{anchor}]({url})"

            before, after = remainder.split(markdown, 1)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(anchor, TextType.LINK, url))

            remainder = after

        if remainder:
            new_nodes.append(TextNode(remainder, TextType.TEXT))

    return new_nodes