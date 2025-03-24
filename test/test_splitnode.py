import unittest

from src.htmlnode import ParentNode, LeafNode
from src.splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link
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
        
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
            )
        split_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("This is text with an ", TextType.TEXT),
                          TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                          TextNode(" and another ", TextType.TEXT),
                          TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                          ], split_nodes)
        
    def test_split_link(self):
        node = TextNode(
            "This is text with a [click this](www.example.com) and another [and this](www.othersite.com)",
            TextType.TEXT,
        )
        split_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("This is text with a ", TextType.TEXT),
                          TextNode("click this", TextType.LINK, "www.example.com"),
                          TextNode(" and another ", TextType.TEXT),
                          TextNode("and this", TextType.LINK, "www.othersite.com")]
                          , split_nodes)
    
    def test_split_link_none(self):
        node = TextNode("This is [text](with no links at all", TextType.TEXT)
        split_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("This is [text](with no links at all", TextType.TEXT)],
                         split_nodes)