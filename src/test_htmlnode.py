import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        actual = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(actual, expected)

    def test_repr(self):
        node = HTMLNode(tag="a", value="this is the value", props={"href": "https://www.google.com", "target": "_blank"})
        actual = repr(node)
        expected = "HTMLNode(a, this is the value, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(actual, expected)

    def test_value(self):
        actual = HTMLNode(tag="a", value="this is not the value", props={"href": "https://www.google.com", "target": "_blank"})
        expected = HTMLNode(tag="a", value="this is the value", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(actual.value, expected.value)

class TestLeafNode(unittest.TestCase):

    def test_value_present(self):
        node = LeafNode(value=None, tag='p')
        with self.assertRaises(ValueError):
            node.to_html()

    def test_valid_html(self):
        node = LeafNode(value="This is an html string converted from a LeafNode.", tag='p')
        html = "<p>This is an html string converted from a LeafNode.</p>"
        self.assertEqual(node.to_html(), html)

class TestParentNode(unittest.TestCase):

    def test_children_present(self):

        node = ParentNode(children=None, tag='p')
        with self.assertRaises(ValueError):
            node.to_html()

    def test_tag_present(self):

        node = ParentNode(children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            tag=None
        )

        with self.assertRaises(ValueError):
            node.to_html()
        
    def test_valid_html(self):

        node = ParentNode(children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            tag="p",
        )
        node.to_html()
        html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), html)


if __name__ == "__main__":
    unittest.main()