# markdown_to_html_node.py
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType

from parentnode import ParentNode
from leafnode import LeafNode

from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node


def text_to_children(text: str):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in text_nodes]


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        t = block_to_block_type(block)

        # CODE: no inline parsing, keep text exactly
        if t == BlockType.CODE:
            code_text = block[4:-3]  # remove leading "```\n" and trailing "```"
            code_leaf = LeafNode(None, code_text)
            code_node = ParentNode("code", [code_leaf])
            pre_node = ParentNode("pre", [code_node])
            block_nodes.append(pre_node)
            continue

        if t == BlockType.HEADING:
            level = len(block.split(" ")[0])
            text = block[level + 1:]
            node = ParentNode(f"h{level}", text_to_children(text))
            block_nodes.append(node)
            continue

        if t == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = []

            for line in lines:
                if line.startswith("> "):
                    cleaned_lines.append(line[2:])
                elif line.startswith(">"):
                    cleaned_lines.append(line[1:])
                else:
                    cleaned_lines.append(line)

            text = "\n".join(cleaned_lines)
            node = ParentNode("blockquote", text_to_children(text))
            block_nodes.append(node)
            continue
        if t == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            items = []

            for line in lines:
                text = line[2:]
                items.append(ParentNode("li", text_to_children(text)))

            node = ParentNode("ul", items)
            block_nodes.append(node)
            continue
        if t == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            items = []

            for line in lines:
                text = line.split(". ", 1)[1]
                items.append(ParentNode("li", text_to_children(text)))

            node = ParentNode("ol", items)
            block_nodes.append(node)
            continue


        # For now: everything else treated as a paragraph with inline parsing
        clean = block.replace("\n", " ")
        children = text_to_children(clean)
        p_node = ParentNode("p", children)
        block_nodes.append(p_node)

    return ParentNode("div", block_nodes)