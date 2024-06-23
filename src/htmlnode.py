class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

        
        
    def to_html(self):
        raise NotImplementedError 
    
    def props_to_html(self) -> str:
        html = ""
        for i in self.props:
            html = html + f' {i}=\"{self.props[i]}\"'
        return html
   
class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None) -> None:
        super().__init__(tag, value, props)
        
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if self.tag is None: return f"{self.value}"
        if self.props is None: return f"<{self.tag}>{self.value}</{self.tag}>"
        else: return f"<{self.props_to_html()}>"
        # if self.props is not None: return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    

        
# <p>This is a paragraph of text.</p>
# <a href="https://www.google.com">Click me!</a>