import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_no_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is also a text node", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_no_eq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node,node2)
    
    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.nl")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.google.nl")
        self.assertEqual(node, node2)
    
    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.googl.nl")
        node2 = TextNode("This is a text node", TextType.ITALIC, "www.googl.nl")
        self.assertNotEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.ITALIC, "www.googl.nl")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()