import unittest

from htmlnode import ParentNode, LeafNode
from splitnode import split_nodes_delimiter
from textnode import TextNode, TextType

class TestHtmlNode(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter(node, "`", TextType.CODE)
        self.assertEqual(new_nodes, 
                         [TextNode("This is text with a ", TextType.TEXT),
                          TextNode("code block", TextType.CODE),
                          TextNode(" word", TextType),
                          ])