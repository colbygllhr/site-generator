from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:
        nodes = []
        if node.text_type != "text":
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

        



