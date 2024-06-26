import unittest

from textnode import TextNode, text_node_to_html_node #type:ignore
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_letter_cases(self):
        node = TextNode("This is a text node", "BOLD")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_url(self):
        node = TextNode("This is a text node", "bold", "www.test.com")
        node2 = TextNode("This is a text node", "bold", "www.test.com")
        self.assertEqual(node, node2)
 
 
    def test_txt_to_html(self):
        node1 = TextNode("This is a text node", "text")
        node2 = TextNode("This is a bold text node", "BOLD")
        node3 = TextNode("This is a italic text node", "italic")
        node4 = TextNode("This is a code node", "coDe")
        node5 = TextNode("This is a link text node", "link", "www.webpg.co.uk")
        node6 = TextNode("This is an image node", "image", "www.webpg.co.uk")
        node7 = TextNode("This is an image node", "ipotato", "www.webpg.co.uk")
        
        html_node1 = text_node_to_html_node(node1)
        html_node2 = text_node_to_html_node(node2)
        html_node3 = text_node_to_html_node(node3)
        html_node4 = text_node_to_html_node(node4)
        html_node5 = text_node_to_html_node(node5)
        html_node6 = text_node_to_html_node(node6)
        
        self.assertEqual(html_node1.__repr__(), f"HTMLNode(tag: {html_node1.tag}, value: {html_node1.value}, children: None, props: {html_node1.props})")
        self.assertEqual(html_node2.__repr__(), f"HTMLNode(tag: {html_node2.tag}, value: {html_node2.value}, children: None, props: {html_node2.props})")
        self.assertEqual(html_node3.__repr__(), f"HTMLNode(tag: {html_node3.tag}, value: {html_node3.value}, children: None, props: {html_node3.props})")
        self.assertEqual(html_node4.__repr__(), f"HTMLNode(tag: {html_node4.tag}, value: {html_node4.value}, children: None, props: {html_node4.props})")
        self.assertEqual(html_node5.__repr__(), f"HTMLNode(tag: {html_node5.tag}, value: {html_node5.value}, children: None, props: {html_node5.props})")
        self.assertEqual(html_node6.__repr__(), f"HTMLNode(tag: {html_node6.tag}, value: {html_node6.value}, children: None, props: {html_node6.props})")
        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node7)

        the_exception = cm.exception
        self.assertEqual(the_exception.__repr__(), f"ValueError(\'{node7.text_type} is not a valid text type\')")
               
if __name__ == "__main__":
    unittest.main()
