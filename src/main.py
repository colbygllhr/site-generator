from textnode import TextNode
from htmlnode import HTMLNode
from inline import *

def main():

    my_textnode = TextNode("This is text with a **bold block** word", "bold")
    
    my_htmlnode = HTMLNode("a", {"href": "https://www.google.com"})
