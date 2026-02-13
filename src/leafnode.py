from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str | None, props: dict[str, str] | None = None):
        if value is None: # pyright: ignore[reportUnnecessaryComparison]
            raise ValueError("LeafNode requires a value.")
        super().__init__(
            value=value, 
            tag=tag, 
            props=props
        )

    def to_html(self) -> str:
        if self.tag is not None:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        else:
            return self.value # pyright: ignore[reportReturnType], LeafNodes always have a str in self.value
    
    def __repr__(self):
        return f"(Tag: {self.tag}, Value: \"{self.value}\", Props: {self.props})"
