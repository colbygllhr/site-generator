from textnode import TextNode
from htmlnode import HTMLNode

def main():

    my_textnode = TextNode("its dark here", "italic", "https://www.cave.com")
    print(repr(my_textnode))
    my_htmlnode = HTMLNode("a", {"href": "https://www.google.com"})


