import unittest

from textnode import TextNode #type:ignore


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
        
if __name__ == "__main__":
    unittest.main()
