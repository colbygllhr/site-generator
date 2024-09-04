import unittest

from htmlnode import HTMLNode

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
        actual = HTMLNode(tag="<a>", value="this is not the value", props={"href": "https://www.google.com", "target": "_blank"})
        expected = HTMLNode(tag="<a>", value="this is the value", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(actual.value, expected.value)
        

        


if __name__ == "__main__":
    unittest.main()