class HTMLNode:
    def __init__(self, tag=None: str, value=None: str, children=None: list, props=None: dict) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __rept__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

        
        
    def to_html(self):
        raise NotImplementedError 
    
    def props_to_html(self) -> str:
        html = ""
        for i in self.props:
            html = html + f' {i}=\"{dic[i]}\"'
        return html
        