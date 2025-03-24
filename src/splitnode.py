from src.textnode import TextNode, TextType
from src.inline_parser import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("Unmatched delimiter in input text")
            for i, segment in enumerate(split_text):
                if i % 2 == 0:
                    new_nodes.append(TextNode(segment, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(segment, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            if len(images) == 0:
                new_nodes.append(node)
                continue
            text = node.text
            for alt, url in images:
                markdown = f"![{alt}]({url})"
                before, after = text.split(markdown, 1)
                if before: #check for before text and append it (avoids appending empty strings)
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                text = after

            if text:   #if anything left, append it
                new_nodes.append(TextNode(text, TextType.TEXT))


    return new_nodes