from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    old_nodes_split = old_nodes.text.split(delimiter)
    to_return_list = []
    for node in old_nodes_split:
        if node.startswith(delimiter) and node.endswith(delimiter):
            new_node = TextNode(node,text_type)
            to_return_list.extend(new_node)
        if node.startswith(delimiter) or node.endswith(delimiter):
            raise Exception("invalid markdown text. Not all delimiters have a matching set")
        else:
            new_node = TextNode(node,TextType.TEXT)

    return to_return_list
