import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:
        nodes = []
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        strings = node.text.split(delimiter)

        if len(strings) % 2 == 0:
            raise ValueError("Syntax error: unmatched delimiter detected")
        
        for i in range(0, len(strings)):
            string = strings[i]
            if i % 2 == 0:
                text_type_node = TextNode(string, text_type_text)
                nodes.append(text_type_node)
            else:
                other_type_node = TextNode(string, text_type)
                nodes.append(other_type_node)
            
        
        new_nodes.extend(nodes)

    return new_nodes

def extract_markdown_images(text):

    images_matcher = re.findall(r"!\[(.*?)\]\((.*?)\)", text)

    return images_matcher

def extract_markdown_links(text):

    link_matcher = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

    return link_matcher

def split_nodes_image(old_nodes):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        
        remaining_text = node.text
        for alt, url in images:
            delimiter = f"![{alt}]({url})"
            parts = node.text.split(delimiter, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))
            
            new_nodes.append(TextNode(alt, text_type_image, url))
            
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, text_type_text))

    return new_nodes
            
def split_nodes_link(old_nodes):
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)
            continue
        
        remaining_text = node.text

        for desc, url in links:
            delimiter = f"[{desc}]({url})"
            parts = node.text.split(delimiter, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))
            
            new_nodes.append(TextNode(desc, text_type_link, url))
            
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, text_type_text))

    return new_nodes

    



 
    

  




        



