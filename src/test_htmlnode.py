import unittest

from htmlnode import HTMLNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is text")
        node2 = HTMLNode("p", "this is text")
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        props = {"href": "https://example.com", "target": "_blank"}
        node = HTMLNode("a", "click here", props=props)
        output = node.props_to_html()
        expected = ' href="https://example.com" target="_blank"'
        self.assertEqual(output, expected)
    
    def test_props_to_html_empty(self):
        node = HTMLNode("div", "content", props={})
        output = node.props_to_html()
        self.assertEqual(output, "")

    def test_repr(self):
        node = HTMLNode("p", "hello", props={"class": "intro"})
        output = repr(node)
        #expected = 'HTMLNode(p, hello, None, {"class": "intro"})'
        self.assertIn("HTMLNode(", output)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "click here", props={"href": "https://example.com"})
        expected = '<a href="https://example.com">click here</a>'
        self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()