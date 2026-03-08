def markdown_to_blocks(markdown: str):
    """
    Split a full markdown document into block-level sections.

    Blocks are separated by one or more blank lines.
    Leading/trailing whitespace inside each block is stripped.
    Empty blocks are removed.
    """
    if markdown is None:
        raise ValueError("markdown is required")

    # Split on double newlines (block separator)
    raw_blocks = markdown.split("\n\n")

    blocks = []
    for block in raw_blocks:
        cleaned = block.strip()
        if cleaned:  # remove empty blocks
            blocks.append(cleaned)

    return blocks