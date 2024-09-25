import unittest

from inline import *
from textnode import *

class TestInline(unittest.TestCase):

    def test_code_text(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        list_nodes = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
            ]
        self.assertEqual(new_nodes, list_nodes)
    
    def test_bold_text(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        list_nodes = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bolded phrase", text_type_bold),
            TextNode(" in the middle", text_type_text),
            ]
        self.assertEqual(new_nodes, list_nodes)
    
    def test_img_extract(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(actual, expected)
    
    def test_link_extract(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        actual = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(actual, expected)


    

    



    
