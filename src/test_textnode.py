import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_eq_url(self):
        node = TextNode("I link to boot.dev!", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("I link to boot.dev!", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)
    def test_link_no_url(self):
        with self.assertRaises(ValueError) as cm:
            TextNode("I should link to something, but my developer forgot to give me a link.", TextType.LINK)
        exception = cm.exception
        self.assertEqual(exception.args, ("Specified text type requires a URL", ))
    
    def test_text_to_html(self):
        t_node = TextNode("I'm just some basic text.", TextType.TEXT)
        h_node = LeafNode(value="I'm just some basic text.", tag=None)
        self.assertEqual(t_node.to_html_node(), h_node)
    def test_bold_to_html(self):
        t_node = TextNode("I'm quite important.", TextType.BOLD)
        h_node = LeafNode(value="I'm quite important.", tag="b")
        self.assertEqual(t_node.to_html_node(), h_node)
    def test_italic_to_html(self):
        t_node = TextNode("I'm spoken with emphasis.", TextType.ITALIC)
        h_node = LeafNode(value="I'm spoken with emphasis.", tag="i")
        self.assertEqual(t_node.to_html_node(), h_node)
    def test_code_to_html(self):
        t_node = TextNode("function pythonSucks() {\nconsole.log(\"Python sucks so much\")\n}", TextType.CODE)
        h_node = LeafNode(value="function pythonSucks() {\nconsole.log(\"Python sucks so much\")\n}", tag="code")
        self.assertEqual(t_node.to_html_node(), h_node)
    def test_link_to_html(self):
        t_node = TextNode("I like to watch youtube. It just has so much content!", TextType.LINK, "https://www.youtube.com")
        h_node = LeafNode(value="I like to watch youtube. It just has so much content!", tag="a", props={"href": "https://www.youtube.com"})
        self.assertEqual(t_node.to_html_node(), h_node)
    def test_image_to_html(self):
        t_node = TextNode("I've got a cat. Haha. Thank you for looking at this cat.", TextType.IMAGE, "https://images.pexels.com/photos/31440959/pexels-photo-31440959.jpeg")
        h_node = LeafNode(value="", tag="img", props={"src": "https://images.pexels.com/photos/31440959/pexels-photo-31440959.jpeg", "alt": "I've got a cat. Haha. Thank you for looking at this cat."})
        self.assertEqual(t_node.to_html_node(), h_node)
    

if __name__ == "__main__":
    unittest.main()