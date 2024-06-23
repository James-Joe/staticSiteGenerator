import unittest

from htmlnode import HTMLNode, LeafNode #type:ignore


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"" )
        
    def test_to_html(self):
        node1 = LeafNode(value="Hello world!")
        node2 = LeafNode(tag="p", value="This is a paragraph of text.")
        node3 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        
        self.assertEqual(node1.to_html(), "Hello world!")
        self.assertEqual(node2.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node3.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        
        
        
# <p>This is a paragraph of text.</p>
# <a href="https://www.google.com">Click me!</a>