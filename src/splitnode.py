from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    old_nodes = old_nodes.text.split(delimiter)
    node_one = TextNode(old_nodes[0], TextType.TEXT)
    node_two = TextNode(old_nodes[1], text_type)
    node_three = TextNode(old_nodes[2], TextType.TEXT)
    return [node_one, node_two, node_three]