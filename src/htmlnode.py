from textnode import TextNode
from textnode import TextType


class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:      #if props is None, we return a empty string
            return ""
        to_return = ""
        for x in self.props:        #if props has a value we return a string made up of that value
            to_return = to_return + " " + x +"=\""+self.props[x]+"\""
        return to_return
    
    def __repr__(self):
        return f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None or self.value == " ":
            raise ValueError("LeafNode must have a value")
        
        if self.tag is None or self.tag == " ":
            return self.value
        
        if not isinstance(self.tag, str) and self.tag is not None:
            raise TypeError("Tag must be a string or None")
        
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag=tag,children=children, props= props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        to_return = ""
        for child in self.children:
            to_return = to_return + child.to_html()
        
        props_html = self.props_to_html()  # Or whatever the method is called
        return f"<{self.tag}{props_html}>{to_return}</{self.tag}>"
    

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
            raise TypeError("Text node must be a TextNode object")
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text)
        case TextType.CODE:
            return LeafNode("code",text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid TextType")