import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_1_child(self):
        expected = "<div><span>I'm just a fish.</span></div>"
        child_node = LeafNode("I'm just a fish.", "span")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), expected)
    
    def test_to_html_2_child(self):
        expected = "<div><span>I'm just a fish.</span><p>I've got some chips.</p></div>"
        child_node_1 = LeafNode("I'm just a fish.", "span")
        child_node_2 = LeafNode("I've got some chips.", "p")
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(parent_node.to_html(), expected)
    
    def test_to_html_5_child(self):
        expected = "<div><div>Aaah. I need a medic bag!</div><div>Chains is a pickle.</div><div>It's a muddaf*ckin bulldozer!</div><div>Got the taser, b*tch.</div><div>I don't think that's supposed to go there.</div></div>"
        child_node_1 = LeafNode("Aaah. I need a medic bag!", "div")
        child_node_2 = LeafNode("Chains is a pickle.", "div")
        child_node_3 = LeafNode("It's a muddaf*ckin bulldozer!", "div")
        child_node_4 = LeafNode("Got the taser, b*tch.", "div")
        child_node_5 = LeafNode("I don't think that's supposed to go there.", "div")
        parent_node = ParentNode("div", [child_node_1, child_node_2, child_node_3, child_node_4, child_node_5])
        self.assertEqual(parent_node.to_html(), expected)
    
    def test_to_html_grandparent(self):
        expected = "<div><div><span>Grandpappy is an unc.</span></div></div>"
        grandchild_node = LeafNode("Grandpappy is an unc.", "span")
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), expected)
    
    def test_to_html_grandparent_with_siblings(self):
        expected = "<div><div><span>I'm the first and only grandchild.</span></div><div>My brother had a kid.</div></div>"
        grandchild_node = LeafNode("I'm the first and only grandchild.", "span")
        child_node_1 = ParentNode("div", [grandchild_node])
        child_node_2 = LeafNode("My brother had a kid.", "div")
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(parent_node.to_html(), expected)

    def test_no_children(self):
        parent_node = ParentNode("div", None) # pyright: ignore[reportArgumentType]
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        exception = cm.exception
        self.assertEqual(exception.args, ("ParentNode has no children", ))
    
    def test_no_tag(self):
        parent_node = ParentNode("", None) # pyright: ignore[reportArgumentType]
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        exception = cm.exception
        self.assertEqual(exception.args, ("ParentNode has no tag", ))