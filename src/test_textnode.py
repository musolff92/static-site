import unittest

from enum import Enum
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("this is some code", TextType.CODE)
        node2 = TextNode("this is some code", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_string_texttype(self):
        node = TextNode("this is text", "TextType.TEXT")
        node2 = TextNode("this is text with proper type", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_url_set_none(self):
        node = TextNode("test code", TextType.CODE)
        node2 = TextNode("test code", TextType.CODE, url=None)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("this is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "this is a text node")
    
    def test_bad_texttype(self):
        class FakeType(Enum):
            BAD = "bad"
        node = TextNode("This is bold text", FakeType.BAD)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
    def test_text_bold(self):
        node = TextNode("this is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "this is bold text")
        output_html = html_node.to_html()
        self.assertEqual(output_html, "<b>this is bold text</b>")
        
    
if __name__ == "__main__":
    unittest.main()