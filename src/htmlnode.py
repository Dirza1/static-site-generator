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

    def to_html(LeafNode):
        if LeafNode.value == "":
            raise ValueError
        match LeafNode.tag:
            case None:
                return LeafNode.value
            case "a":
                return f"<a {LeafNode.props.replace(":","=")}>Click me!</a>"
            case _:
                return f"<{LeafNode.tag}>{LeafNode.value}</{LeafNode.tag}>"
