import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TestMarkdownModules(unittest.TestCase):

    def test_delimiter_func(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        code_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(code_nodes, [TextNode("This is text with a ", "text", None), TextNode("code block", "code", None), TextNode(" word", "text", None)])
        
        node2 = TextNode("This is text with a **bolded** word", text_type_text)
        bold_nodes = split_nodes_delimiter([node2], "**", text_type_bold)
        self.assertEqual(bold_nodes, [TextNode("This is text with a ", "text", None), TextNode("bolded", "bold", None), TextNode(" word", "text", None)])
        
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        
        self.assertEqual(extract_markdown_images(text), [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text), [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])
        
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text
        )
        self.assertEqual(split_nodes_link([node]), [TextNode("This is text with a link ", "text", None), TextNode("to boot dev", "link", "https://www.boot.dev"), TextNode(" and ", "text", None), TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev")])

    def test_split_nodes_image(self):
        node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png) too ", text_type_text)
        self.assertEqual(split_nodes_image([node]), [TextNode("This is text with an ", "text", None), TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" and ", "text", None), TextNode("another", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png"), TextNode(" too ", "text", None)])
             
if __name__ == "__main__":
    unittest.main()