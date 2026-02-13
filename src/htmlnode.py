class HTMLNode:
    def __init__(self, value: str | None = None, tag: str | None = None, children: list[HTMLNode] | None = None, props: dict[str, str] | None = None):

        """
        A Node with no tag is rendered as plain text
        A Node with no value is *assumed* to have children
        A Node with no children is *assumed* to have a value
        A Node with no props has no styling
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self) -> str:
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