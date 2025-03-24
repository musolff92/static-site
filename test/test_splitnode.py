import unittest

from src.htmlnode import ParentNode, LeafNode
from src.splitnode import split_nodes_delimiter
from src.textnode import TextNode, TextType

class TestHtmlNode(unittest.TestCase):
    def test_code_split(self):
        code_node = TextNode("This is text with a `code block` word", TextType.TEXT)
        bold_node = TextNode("This is text with a *bold* word", TextType.TEXT)
        code_nodes = split_nodes_delimiter([code_node], "`", TextType.CODE)
        bold_nodes = split_nodes_delimiter([bold_node], "*", TextType.BOLD)
        self.assertEqual(code_nodes, 
                         [TextNode("This is text with a ", TextType.TEXT),
                          TextNode("code block", TextType.CODE),
                          TextNode(" word", TextType.TEXT),
                          ])
        self.assertEqual(bold_nodes,
                         [TextNode("This is text with a ", TextType.TEXT),
                          TextNode("bold", TextType.BOLD),
                          TextNode(" word", TextType.TEXT)
                          ])
        