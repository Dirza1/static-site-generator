from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    
    for old_node in old_nodes:
        # If not a TEXT node, add it unchanged
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
            
        # Process text nodes
        text = old_node.text
        current_position = 0
        
        # Continue until we've processed the entire string
        while current_position < len(text):
            # Find the next opening delimiter
            opening_index = text.find(delimiter, current_position)
            
            if opening_index == -1:
                # No more delimiters, add any remaining text
                if current_position < len(text):
                    result.append(TextNode(text[current_position:], TextType.TEXT))
                break
                
            # Add text before the delimiter if there is any
            if opening_index > current_position:
                result.append(TextNode(text[current_position:opening_index], TextType.TEXT))
                
            # Find the closing delimiter
            closing_index = text.find(delimiter, opening_index + len(delimiter))
            if closing_index == -1:
                raise Exception(f"No closing delimiter '{delimiter}' found")
                
            # Add the delimited content with the special type
            delimited_content = text[opening_index + len(delimiter):closing_index]
            result.append(TextNode(delimited_content, text_type))
            
            # Update current_position to continue after the closing delimiter
            current_position = closing_index + len(delimiter)

    return result