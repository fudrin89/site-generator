import re

def extract_markdown_images(text: str):
    """
    Extract markdown images of the form: ![alt](url)
    Returns: list[tuple[str, str]] -> (alt, url)
    """
    pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text: str):
    """
    Extract markdown links of the form: [text](url)
    (but NOT images)
    Returns: list[tuple[str, str]] -> (anchor, url)
    """
    # Negative lookbehind to avoid matching images: ![...](...)
    pattern = r"(?<!!)\[([^\]]*)\]\(([^)]+)\)"
    return re.findall(pattern, text)