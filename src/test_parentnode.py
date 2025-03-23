import unittest

from htmlnode import ParentNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )
        
    def test_to_html_with_multiple_children(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold"),
            LeafNode(None, " plain "),
            LeafNode("i", "italic"),
        ])
        self.assertEqual(node.to_html(), "<p><b>Bold</b> plain <i>italic</i></p>")

    def test_parentnode_raises_without_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None)
            node.to_html()

    def test_parentnode_raises_without_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("p", "text")])
            node.to_html()

    def test_parentnode_with_mixed_children(self):
        node = ParentNode("p", [
            LeafNode("b", "bold"),
            LeafNode(None, " and "),
            LeafNode("i", "italic"),
        ])
        self.assertEqual(
            node.to_html(),
            "<p><b>bold</b> and <i>italic</i></p>"
        )