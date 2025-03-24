import unittest

from src.inline_parser import extract_markdown_links, extract_markdown_images

class TestHtmlNode(unittest.TestCase):
    def test_extract_link(self):
        node = "Here is a [search engine](https://google.com) and a [news site](https://news.com)"
        self.assertEqual(extract_markdown_links(node),
                         [("search engine", "https://google.com"),
                          ("news site", "https://news.com")])
        
    def test_extract_images(self):
        node = "Here is a ![cat picture](cat.jpeg) and a ![dog picture](dog.jpeg)"
        self.assertEqual(extract_markdown_images(node),
                         [("cat picture", "cat.jpeg"),
                          ("dog picture", "dog.jpeg")])
    
    def test_no_links(self):
        node = "here is some text with no link"
        self.assertEqual(extract_markdown_links(node), [])