class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list[HTMLNode] | None = None, props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self) -> None:
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        if self.props == None or len(self.props) == 0:
            return ""
        
        output_str = ""
        for prop in self.props:
            output_str += f" {prop}=\"{self.props[prop]}\""
        return output_str
    
    def __repr__(self):
        if self.value is not None:
            return f"(Tag: {self.tag}, Value: \"{self.value}\", Children: {self.children}, Props: {self.props})"
        else:
            return f"(Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props})"