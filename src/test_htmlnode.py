import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_repr_format_1(self):
        expected = "(Tag: None, Value: \"I am some basic text\", Children: None, Props: None)"
        node = HTMLNode(value="I am some basic text")
        self.assertEqual(node.__repr__(), expected, "Test did not match expected value (Either values are not defaulting to None, or the format is wrong)")
    def test_repr_format_2(self):
        expected = "(Tag: p, Value: \"I'm part of a paragraph!\", Children: None, Props: None)"
        node = HTMLNode(tag="p", value="I'm part of a paragraph!")
        self.assertEqual(node.__repr__(), expected, "Test did not match expected value (Either values are not defaulting to None, or the format is wrong)")
    def test_repr_format_3(self):
        expected = "(Tag: None, Value: \"Hello! I'm a parent!\", Children: [(Tag: None, Value: \"I'm the firstborn child!\", Children: None, Props: None), (Tag: None, Value: \"I'm the middle child.\", Children: None, Props: None), (Tag: None, Value: \"I'm the youngest of the three.\", Children: None, Props: None)], Props: None)"
        child1 = HTMLNode(value="I'm the firstborn child!")
        child2 = HTMLNode(value="I'm the middle child.")
        child3 = HTMLNode(value="I'm the youngest of the three.")
        parent = HTMLNode(value="Hello! I'm a parent!", children=[child1, child2, child3])
        self.assertEqual(parent.__repr__(), expected)
    def test_repr_format_4(self):
        expected = "(Tag: p, Value: \"Hello! I'm a fully fledged HTMLNode.\", Children: [(Tag: None, Value: None, Children: None, Props: None)], Props: {'href': 'https://www.boot.dev'})"
        child = HTMLNode()
        node = HTMLNode(tag="p", value="Hello! I'm a fully fledged HTMLNode.", children=[child], props={"href" : "https://www.boot.dev"})
        self.assertEqual(node.__repr__(), expected)
    def test_repr_format_5(self):
        expected = "(Tag: None, Value: None, Children: None, Props: None)"
        node = HTMLNode()
        self.assertEqual(node.__repr__(), expected)
    
    def test_props_to_html_1(self):
        expected = " href=\"https://www.google.com\""
        node = HTMLNode(props={"href" : "https://www.google.com"})
        self.assertEqual(node.props_to_html(), expected)
    def test_props_to_html_2(self):
        expected = " href=\"https://www.youtube.com\" target=\"_blank\""
        node = HTMLNode(props={"href": "https://www.youtube.com", "target" : "_blank"})
        self.assertEqual(node.props_to_html(), expected)
    def test_props_to_html_3(self):
        expected = ""
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), expected)
