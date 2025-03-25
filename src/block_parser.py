import re
from enum import Enum
from src.textnode import LeafNode, text_node_to_html_node
from src.splitnode import text_to_textnodes
from src.htmlnode import ParentNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"



def markdown_to_blocks(text):
    new_blocks = []
    blocks = text.split("\n\n")
    for block in blocks:
        stripped = block.strip()
        if stripped:
            new_blocks.append(stripped)
    return new_blocks

def block_to_block_type(block):
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    lines = block.split("\n")
    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.strip().startswith("-") for line in lines):
        return BlockType.UNORDERED_LIST
    for index, line in enumerate(lines):
        expected_prefix = f"{index + 1}. "
        if not line.strip().startswith(expected_prefix):
            break
    else:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def markdown_to_html_node(markdown):
    block_nodes = []
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            code_content = "\n".join(block.split("\n")[1:-1])
            code_node = LeafNode("code", code_content)
            pre_node = LeafNode("pre", code_node.to_html())
            block_nodes.append(pre_node)
        elif block_type == BlockType.PARAGRAPH:
            children = text_to_children(block)
            block_nodes.append(ParentNode("p", children))
        elif block_type == BlockType.HEADING:
            heading_level = len(re.match(r"^(#{1,6}) ", block).group(1))
            content = block[heading_level + 1:]
            children = text_to_children(content)
            block_nodes.append(ParentNode(f"h{heading_level}", children))
        elif block_type == BlockType.QUOTE:
            quote_text = "\n".join([line.lstrip("> ").strip() for line in block.split("\n")])
            children = text_to_children(quote_text)
            block_nodes.append(ParentNode("blockquote", children))
        elif block_type == BlockType.UNORDERED_LIST:
            list_items = []
            for line in block.strip("\n"):
                content = line.lstrip("- ").strip()
                children = text_to_children(content)
                list_items.append(ParentNode("li", children))
            block_nodes.append(ParentNode("ul", list_items))
        elif block_type == BlockType.ORDERED_LIST:
            list_items = []
            for line in block.split("\n"):
                content = re.sub(r"^\d+\. ", "", line).strip()
                children = text_to_children(content)
                list_items.append(ParentNode("li", children))
            block_nodes.append(ParentNode("ol", list_items))
    return ParentNode("div", block_nodes)