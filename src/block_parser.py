import re
from enum import Enum

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

#def markdown_to_html_node(markdown):
#    markdown_blocks = markdown_to_blocks(markdown)
#    for block in markdown_blocks:
#        block_type = block_to_block_type(block)
#        if block_type == BlockType.CODE: