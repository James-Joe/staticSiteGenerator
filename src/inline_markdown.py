from textnode import TextNode
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text: str) -> list:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> list:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        text = extract_markdown_images(node.text)
        if len(text) == 0: new_nodes.append(node)
  
  
def split_nodes_link(old_nodes: list) -> list:
    new_nodes= []
    for node in old_nodes:
        node_txt = node.text
        txt_lst = extract_markdown_links(node.text)
        if len(txt_lst) == 0: new_nodes.append(node) 
        for i in range(len(txt_lst)):
            new_txt = node_txt.split(f"[{txt_lst[i][0]}]({txt_lst[i][1]})", 1)
            new_nodes.append(TextNode(new_txt[0], text_type_text))
            new_nodes.append(TextNode(txt_lst[i][0], text_type_link, txt_lst[i][-1]))
            node_txt = new_txt[-1] 
        print(len(node_txt))
        if not node_txt.isspace() and len(node_txt) != 0:
            new_nodes.append(TextNode(node_txt, text_type_text))
    return new_nodes      
  
def split_nodes_image(old_nodes: list) -> list:
    new_nodes= []
    for node in old_nodes:
        node_txt = node.text
        txt_lst = extract_markdown_links(node.text)
        if len(txt_lst) == 0: new_nodes.append(node) 
        for i in range(len(txt_lst)):
            new_txt = node_txt.split(f"![{txt_lst[i][0]}]({txt_lst[i][1]})", 1)
            new_nodes.append(TextNode(new_txt[0], text_type_text))
            new_nodes.append(TextNode(txt_lst[i][0], text_type_image, txt_lst[i][-1]))
            node_txt = new_txt[-1] 
        if not node_txt.isspace() and len(node_txt) != 0:
            new_nodes.append(TextNode(node_txt, text_type_text))            
            node_txt = new_txt[-1] 
    return new_nodes      


# node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     text_type_text
# )

# new_nodes = split_nodes_link([node])

# print(new_nodes)     

# node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png) too ", text_type_text)

# new_nodes = split_nodes_image([node])

# print(new_nodes)  