from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type.lower()
        self.url = url

    def __eq__(self, other_node) -> bool:
        if self.text == other_node.text and self.text_type == other_node.text_type and self.url == other_node.url: 
            return True
        return False
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == text_type_text:
        return LeafNode(text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"{text_node.text_type} is not a valid text type")    

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list:
    new_nodes = []
    if text_type == text_type_text: 
        new_nodes.extend(old_nodes)
    for i in old_nodes:
        if i.text_type != text_type_text: 
            new_nodes.append(i)
        delimiter_num = i.text.count(delimiter)
        print(delimiter_num)
        if delimiter_num % 2 > 0:
            raise Exception("Odd number of delimiters")
        in_delimiter = False
        string = ""
        for char in i.text:
            if char != delimiter:
                string += char
            elif char == delimiter and in_delimiter is False:
                in_delimiter = True
                new_nodes.append(TextNode(string, text_type_text))
                string = ""
                continue
            elif char == delimiter and in_delimiter is True:
                in_delimiter = False
                new_nodes.append(TextNode(string, text_type))
                string = ""
                continue
        if in_delimiter is False:
            new_nodes.append(TextNode(string, text_type_text))
        if in_delimiter is True:
            new_nodes.append(TextNode(string, text_type))
    for i in new_nodes:
        if i.text == "" or i.text == " ":
            new_nodes.remove(i)
    return new_nodes


node = TextNode("`This is` text with a `code` `block` word", text_type_text)
new_nodes = split_nodes_delimiter([node], "`", text_type_code)

for i in new_nodes:
    print(i)