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
        print(result)
    
        # Since dictionary order is not guaranteed, we need to check for both possibilities
        possible_outputs = [
        ' href="https://www.google.com" target="_blank"',
        ' target="_blank" href="https://www.google.com"'
        ]
        self.assertIn(result, possible_outputs)
    
    def test_repr(self):
        test_case = HTMLNode("p","this is a test", None,None)
        expected_result = "HTMLNode: p, this is a test, None None"
        result = test_case.__repr__()
        self.assertEqual(result,expected_result)

if __name__ == "__main__":
    unittest.main()