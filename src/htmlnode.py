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
        to_return = " "
        for x in self.props:        #if props has a value we return a string made up of that value
            to_return = to_return + " " + self.props[x]
        return to_return
    
    def __repr__(self):
        return f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}"