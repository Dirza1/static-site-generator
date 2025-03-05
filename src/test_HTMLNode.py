import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        # Test without properties
        note = HTMLNode("p","this is a test",None,None)
        test_case = note.props_to_html()
        self.assertEqual(test_case,"")

    def test_props_to_html_full(self):
        # Test with properties
        props = {
        "href": "https://www.google.com",
        "target": "_blank"
         }
        node = HTMLNode("a", "Google", None, props)
        result = node.props_to_html()
    
        # Since dictionary order is not guaranteed, we need to check for both possibilities
        possible_outputs = [
        ' href="https://www.google.com" target="_blank"',
        ' target="_blank" href="https://www.google.com"'
        ]
        self.assertIn(result, possible_outputs)
    
    def test_repr_simp(self):
        test_case = HTMLNode("p","this is a test", None,None)       #testing the __repr__ function
        expected_result = "HTMLNode: p, this is a test, None, None"
        result = test_case.__repr__()
        self.assertEqual(result,expected_result)
    
    def test_repr_comp(self):
        child1 = HTMLNode(None, None, None, None)
        child2 = HTMLNode("i", "test", None, None)
        
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
        test = HTMLNode("i", "test", None, None)
        with self.assertRaises(NotImplementedError):
            test.to_html()

    def test_constructor(self):
        test = HTMLNode()
        expected_restult = "HTMLNode: None, None, None, None"
        result = test.__repr__()
        self.assertEqual(result,expected_restult)

if __name__ == "__main__":
    unittest.main()