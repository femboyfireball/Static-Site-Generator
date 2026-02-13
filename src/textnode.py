from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "No Type"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        if (text_type is TextType.LINK or text_type is TextType.IMAGE) and url is None:
            raise ValueError("Specified text type requires a URL")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url # type: ignore

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def to_html_node(self) -> LeafNode:
        if self.text_type not in TextType:
            raise TypeError("Text type is not a recognized text type.")
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(value=self.text, tag=None)
            case TextType.BOLD:
                return LeafNode(value=self.text, tag="b")
            case TextType.ITALIC:
                return LeafNode(value=self.text, tag="i")
            case TextType.CODE:
                return LeafNode(value=self.text, tag="code")
            case TextType.LINK:
                return LeafNode(value=self.text, tag="a", props={"href": self.url}) # pyright: ignore[reportArgumentType]
            case TextType.IMAGE:
                return LeafNode(value="", tag="img", props={"src": self.url, "alt": self.text}) # pyright: ignore[reportArgumentType]