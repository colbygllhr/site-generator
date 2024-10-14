from textnode import *
from htmlnode import *
from inline import *

def markdown_to_blocks(markdown):
    lines = markdown.split('\n\n') # Double newline to specify paragraph

    stripped = [line.strip() for line in lines if line.strip()]

    return stripped

def block_to_block_type(block):
    lines = block.splitlines()  # assuming `markdown` is a single block

    #checking for code blocks
    if lines[0].startswith('```') and lines[-1].endswith('```'):
        return "code"

    # Checking for headings
    # Checking for headings
    if lines[0].startswith("#"):
        i = 0
        while i < len(lines[0]) and lines[0][i] == "#":
            i += 1
        if i <= 6 and i < len(lines[0]) and lines[0][i] == ' ':
            return "heading"

    # Checking for quote blocks
    for line in lines:
        if not line.startswith('>'):
            break  # If any line doesn't start with '>', it's not a quote block
    else:
        return "quote"

# Checking for unordered list
    for line in lines:
        if not (line.startswith('* ') or line.startswith('- ')):
            break  # If any line doesn't start with a list marker, it's not an unordered list
    else:
        return "unordered_list"

# Checking for ordered list
    counter = 1
    for line in lines:
        if not line.startswith(f"{counter}. "):
            break  # If any line isn't a correct ordered list number, it's not ordered
        counter += 1
    else:
        return "ordered_list"
    
    return "paragraph"

def text_to_children(type):
    text_nodes = text_to_textnodes(type)
    children = []

    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)

    return children


def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    nodes = [] 

    def process_ordered_list(content):
        lines = content.split("\n")
        list_items = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line[0].isdigit() and ". " in line:
                _, content = line.split(". ", 1)
                item = HTMLNode("li", None, text_to_children(content))
                list_items.append(item)
    
        ol_node = HTMLNode("ol", None, list_items)
        return ol_node
    
    def process_unordered_list(content):
        lines = content.split("\n")
        list_items = []
        for line in lines:
            line.strip()
            if not line:
                continue
            if line.startswith('* ') or line.startswith('- '):
                content = line[2:]  # Remove the '* ' or '- '
                item = HTMLNode("li", None, text_to_children(content))
                list_items.append(item)

        ul_node = HTMLNode("ul", None, text_to_children(content))
        return ul_node
       
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == "quote": 
            quote_node = HTMLNode("blockquote", block)
            nodes.append(quote_node)

        if block_type == "code":
            code_node = HTMLNode("code", block)
            pre_node = HTMLNode("pre", block, code_node)
            nodes.append(pre_node)
        
        if block_type == "ordered_list":
            node = process_ordered_list(block)
            nodes.append(node)
        
        if block_type == "unordered_list":
            node = process_unordered_list(block)
            nodes.append(node)

        if block_type == "heading":
            level = block.count('#')
            content = block.lstrip('#').strip()
            heading_node = HTMLNode(f"h{level}", None, text_to_children(content))
            nodes.append(heading_node)  

        if block_type == "paragraph":
            children = text_to_children(block)
            para_node = HTMLNode("p", None, children)
            nodes.append(para_node)
        
    parent_node = HTMLNode("div", children=nodes)

    return parent_node