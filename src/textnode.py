from enum import Enum

class TextType(Enum):
    Bold_Text = "Bold"
    Italic_Text = "Italic"
    Code_Text = "Code"
    Links = "Links"
    Immages = "Images"

class TextNode():
    def __init__(self, text, text_type,url):
        self.text = text
        self.text_type=text_type
        self.url = url
    
    def __eq__(self,textnode):
        if self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url:
            return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"