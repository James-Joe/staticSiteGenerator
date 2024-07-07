import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TestTextNode(unittest.TestCase):

    def test_delimiter_func(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        code_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(code_nodes, [TextNode("This is text with a ", "text", None), TextNode("code block", "code", None), TextNode(" word", "text", None)])
        
        node2 = TextNode("This is text with a **bolded** word", text_type_text)
        bold_nodes = split_nodes_delimiter([node2], "**", text_type_bold)
        self.assertEqual(bold_nodes, [TextNode("This is text with a ", "text", None), TextNode("bolded", "bold", None), TextNode(" word", "text", None)])
               
if __name__ == "__main__":
    unittest.main()