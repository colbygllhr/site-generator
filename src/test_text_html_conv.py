import unittest

from textnode import TextNode
from htmlnode import LeafNode
from htmlnode import text_node_to_html_node



class TestTextHTMLConv(unittest.TestCase):

    def test_node_conv(self):
        text_node = TextNode(text_type="bold", text="Bold Text")
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
    
    def test_text_type_image(self):
        text_node = TextNode(text="some text", text_type="image", url="http://example.com/image.png", alt="An image")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")

    def test_text_type_bold(self):
        text_node = TextNode(text_type="bold", text="Bold Text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "Bold Text")
    