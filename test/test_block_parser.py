import unittest
import textwrap

from src.block_parser import markdown_to_blocks, text_node_to_html_node, markdown_to_html_node

class TestHtmlNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = textwrap.dedent("""
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """).strip()
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
            [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
            ],
            )
    
    def test_text_node_to_html_node(self):
        md = textwrap.dedent("""\
            # Welcome
                               
            This is a paragraph.


        """).strip()

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><h1>Welcome</h1><p>This is a paragraph.</p></div>"
        self.assertEqual(expected, html)

    def test_bold_italic_blocks(self):
        md = textwrap.dedent("""\
            **Bold Text**
                             
            _italic text_

        """).strip()

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><p><b>Bold Text</b></p><p><i>italic text</i></p></div>"
        self.assertEqual(expected, html)

    def test_multistyle_line(self):
        md = textwrap.dedent("""\
            This is _italic_, and this is **bold**, and this is `code`.
        """).strip()
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><p>This is <i>italic</i>, and this is <b>bold</b>, and this is <code>code</code>.</p></div>"
        self.assertEqual(html, expected)