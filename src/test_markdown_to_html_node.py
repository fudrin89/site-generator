from src.markdown_to_html_node import markdown_to_html_node


def test_codeblock(self):
    md = (
        "```\n"
        "This is text that _should_ remain\n"
        "the **same** even with inline stuff\n"
        "```"
    )
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\n"
        "the **same** even with inline stuff\n"
        "</code></pre></div>",
    )