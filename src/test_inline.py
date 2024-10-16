import unittest

from inline import *
from textnode import *
from main import extract_title

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

    def test_image_text(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text)
        actual = split_nodes_image([node])
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", text_type_text),
            TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(actual, expected)

    def test_link_text(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
        actual = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(actual, expected)
    
    def test_text_to_textnode(self):
        node = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", text_type_text)
        actual = text_to_textnodes(node.text)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertEqual(actual, expected)
    
    def test_extract_title(self):
        paragraph = "# Hello\nMy name is\nWait for it...\nJeff."
        actual = extract_title(paragraph)
        expected = "Hello"
        self.assertEqual(actual, expected)







    

    



    
