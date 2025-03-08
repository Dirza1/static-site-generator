import unittest
from htmlnode import *
from textnode import *

class TestHTMLNode(unittest.TestCase):
    
    def setUp(self):
        props = {
        "href": "https://www.google.com",
        "target": "_blank"
         }

        self.note = HTMLNode("p","this is a test",None,None)
        self.note_props = HTMLNode("a", "Google", None, props)
        self.note_empty = HTMLNode(None, None, None, None)
    
        self.leaf_p= LeafNode("p", "Hello, world!")
        self.leaf_a = LeafNode("a", "click me!", {"href": "https://www.google.com"})
        self.leaf_empty = LeafNode(None,None,None)
        self.leaf_tag = LeafNode(None, "raw text")


        self.parent_tag = ParentNode(None,self.leaf_a,None)
        self.parent_child = ParentNode("a", None,None)

    def test_props_to_html_none(self):
        # Test without properties
        test_case = self.note.props_to_html()
        self.assertEqual(test_case,"")

    def test_props_to_html_full(self):
        # Test with properties
        result = self.note_props.props_to_html()
    
        # Since dictionary order is not guaranteed, we need to check for both possibilities
        possible_outputs = [
        ' href="https://www.google.com" target="_blank"',
        ' target="_blank" href="https://www.google.com"'
        ]
        self.assertIn(result, possible_outputs)
    
    def test_repr_simp(self):
        test_case = self.note_props      #testing the __repr__ function
        expected_result = "HTMLNode: a, Google, None, {'href': 'https://www.google.com', 'target': '_blank'}"
        result = test_case.__repr__()
        self.assertEqual(result,expected_result)
    
    def test_repr_comp(self):
        child1 = self.note_empty.props_to_html()
        child2 = self.note.props_to_html()
        
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        children = [child1, child2]
        test_case = HTMLNode("p", "this is a test", children, props)
        result = test_case.__repr__()
        
        # Check that it contains the important parts
        self.assertIn("p", result)
        self.assertIn("this is a test", result)
        self.assertIn("href", result)
        self.assertIn("https://www.google.com", result)
        self.assertIn("target", result)
        self.assertIn("_blank", result)

    def test_to_html(self):
        test = self.note
        with self.assertRaises(NotImplementedError):
            test.to_html()

    def test_constructor(self):
        test = self.note_empty
        expected_result = "HTMLNode: None, None, None, None"
        result = test.__repr__()
        self.assertEqual(result,expected_result)


    def test_leaf_to_html_p(self):
        self.assertEqual(self.leaf_p.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        self.assertEqual(self.leaf_a.to_html(), '<a href="https://www.google.com">click me!</a>')

    def test_leaf_empty_value(self):
        with self.assertRaises(ValueError):
            self.leaf_empty.to_html()
    
    def test_leaf_empty_tag(self):
        self.assertEqual(self.leaf_tag.to_html(), "raw text")


    def test_empty_prop(self):
        node = LeafNode("span", "text", {})
        self.assertEqual(node.to_html(), "<span>text</span>")

    def test_unusual_props(self):
        props = {"data-id": "123", "aria-label": "Special & Value!", "class": ""}
        node = LeafNode("span", "text", props)
        self.assertEqual(node.to_html(),'<span data-id="123" aria-label="Special & Value!" class="">text</span>')

    def test_long_value(self):
        long_value = "a" * 10000
        node = LeafNode("p", long_value)
        self.assertEqual(node.to_html(), f"<p>{long_value}</p>")

    def test_empty_tag(self):
        node = LeafNode(" ", "test",None)
        self.assertEqual(node.to_html(),"test")

    def test_invalid_imput(self):
        node=LeafNode(123,456)
        with self.assertRaises(TypeError):
            node.to_html()

    def test_parent_tag(self):
        with self.assertRaises(ValueError):
            self.parent_tag.to_html()
    
    def test_parent_child(self):
        with self.assertRaises(ValueError):
            self.parent_child.to_html()


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()