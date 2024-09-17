import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url(self):
        actual = TextNode("text node", "bold", " ")
        expected = TextNode("text node", "bold", None)
        self.assertNotEqual(actual, expected)
    
    def test_text_type(self):
        actual = TextNode("text node", "bold", " ")
        expected = TextNode("text node", "italic", " ")
        self.assertNotEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

    