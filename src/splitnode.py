from src.textnode import TextNode, TextType

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