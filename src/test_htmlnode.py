import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode #type:ignore


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"" )
        
    def test_leaf_to_html(self):
        node1 = LeafNode(value="Hello world!")
        node2 = LeafNode(tag="p", value="This is a paragraph of text.")
        node3 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        
        self.assertEqual(node1.to_html(), "Hello world!")
        self.assertEqual(node2.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node3.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        
    def test_parent_to_html(self):
        node1 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )   

        nested_parent = ParentNode(
        "div",
        [
            ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode("i", "italic text"),
                ]
            ),
            LeafNode(None, "Normal text"),
        ]
        )
        expected_nested_html = "<div><p><b>Bold text</b><i>italic text</i></p>Normal text</div>"

        double_nested_parent = ParentNode(
        "div",
        [
            ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode("i", "italic text"),
                    ParentNode(
                        "p",
                        [
                            LeafNode("b", "Bold text")
                        ]
                    )
                ]
            ),
            LeafNode(None, "Normal text"),
        ]
        )
        expected_double_nested_html = "<div><p><b>Bold text</b><i>italic text</i><p><b>Bold text</b></p></p>Normal text</div>"
        
        self.assertEqual(node1.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        self.assertEqual(nested_parent.to_html(), expected_nested_html)
        self.assertEqual(double_nested_parent.to_html(), expected_double_nested_html)

   
        
# <p>This is a paragraph of text.</p>
# 
# <a href="https://www.google.com">Click me!</a>