from textnode import *
from htmlnode import *

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

def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "code":
            code_node = HTMLNode("code", block)
            pre_node = HTMLNode("pre", block, code_node)
            


    





    
