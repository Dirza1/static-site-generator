import unittest
from textnode_creation import *
from htmlnode import *
from textnode import *
'''
class TestTextNideCreation(unittest.TestCase):

    def setUp(self):
        self.text_node_test1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.text_node_test2 = TextNode("This is text with a `code block` word", TextType.TEXT)


    def test_simple(self):
       result = split_nodes_delimiter([self.text_node_test1,],"`", TextType.CODE)

       self.assertEqual(len(result), 3)
       self.assertEqual(result[0].text, "This is text with a ")
       self.assertEqual(result[0].text_type, TextType.TEXT)
        
       self.assertEqual(result[1].text, "code block")
       self.assertEqual(result[1].text_type, TextType.CODE)
        
       self.assertEqual(result[2].text, " word")
       self.assertEqual(result[2].text_type, TextType.TEXT)
    




'''

if __name__ == "__main__":
    unittest.main()