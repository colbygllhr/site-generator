import unittest

from blocks import *
from textnode import *

class TestBlock(unittest.TestCase):

    def test_split_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        actual = markdown_to_blocks(markdown)
        expected = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(actual, expected)
    
    def test_block_type_heading(self):
        block = "## This is a heading block"
        actual = block_to_block_type(block)
        expected = "heading"
        self.assertEqual(actual, expected)

    def test_block_type_code(self):
        block = "```\nThis is a code block\n```"
        actual = block_to_block_type(block)
        expected = "code"
        self.assertEqual(actual, expected)
    
    def test_block_type_quote(self):
        block = "> This is a\n> multi-line\n> block of quote text"
        actual = block_to_block_type(block)
        expected = "quote"
        self.assertEqual(actual, expected)
    
    def test_block_type_unordered(self):
        block = "* This is a\n- multi-line block\n* of unordered list text"
        actual = block_to_block_type(block)
        expected = "unordered_list"
        self.assertEqual(actual, expected)
    
    def test_block_type_unordered(self):
        block = "1. This is a\n2. multi-line block\n3. of ordered list text"
        actual = block_to_block_type(block)
        expected = "ordered_list"
        self.assertEqual(actual, expected)
    



