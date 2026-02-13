import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_no_tag_1(self):
        expected = "(Tag: None, Value: \"I'm a leaf node!\", Props: None)"
        node = LeafNode("I'm a leaf node!", None)
        self.assertEqual(node.__repr__(), expected)
    def test_leaf_node_no_tag_2(self):
        expected = "I'm a leaf node!"
        node = LeafNode("I'm a leaf node!", None)
        self.assertEqual(node.to_html(), expected)

    def test_leaf_with_tag_1(self):
        expected = "(Tag: p, Value: \"I'm in a paragraph. I can go on and on and on, but I do have to end at some point.\", Props: None)"
        node = LeafNode("I'm in a paragraph. I can go on and on and on, but I do have to end at some point.", "p")
        self.assertEqual(node.__repr__(), expected)
    def test_leaf_with_tag_2(self):
        expected = "<p>I'm in a paragraph. I can go on and on and on, but I do have to end at some point.</p>"
        node = LeafNode("I'm in a paragraph. I can go on and on and on, but I do have to end at some point.", "p")
        self.assertEqual(node.to_html(), expected)

    def test_leaf_with_props_1(self):
        expected = "(Tag: h1, Value: \"Ooh look at me, I'm a big, bad, red hyperlink to youtube!\", Props: {'style': 'color: red;', 'href': 'https://www.youtube.com'})"
        node = LeafNode("Ooh look at me, I'm a big, bad, red hyperlink to youtube!", "h1", {"style" : "color: red;", "href" : "https://www.youtube.com"})
        self.assertEqual(node.__repr__(), expected)
    def test_leaf_with_props_2(self):
        expected = "<h1 style=\"color: red;\" href=\"https://www.youtube.com\">Ooh look at me, I'm a big, bad, red hyperlink to youtube!</h1>"
        node = LeafNode("Ooh look at me, I'm a big, bad, red hyperlink to youtube!", "h1", {"style" : "color: red;", "href" : "https://www.youtube.com"})
        self.assertEqual(node.to_html(), expected)
    
    def test_leaf_with_no_value(self):
        self.assertRaises(ValueError, LeafNode, None, None) # pyright: ignore[reportArgumentType], We purposefully pass in a None type for the test