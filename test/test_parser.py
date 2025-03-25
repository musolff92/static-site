import unittest

from src.block_parser import BlockType, block_to_block_type
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






    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_code_block(self):
        block = "```\ndef hello():\n    return 'hi'\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = ">This is a block\n >of quoted text"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- item 1\n- item 2\n- item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "This is just a normal paragraph.\nStill part of the same block."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)