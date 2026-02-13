from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None):
        super().__init__(
            tag=tag, 
            children=children, 
            props=props
        )
    
    def to_html(self) -> str | None: # pyright: ignore[reportIncompatibleMethodOverride]
        if self.tag == None or self.tag == "":
            raise ValueError("ParentNode has no tag")
        if self.children == None:
            raise ValueError("ParentNode has no children")

        output = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            output += child.to_html()
        output += f"</{self.tag}>"

        return output