import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_paragraph(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode(
            "a",
            "Click me!",
            {
                "href": "https://www.google.com",
            },
        )

        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )
    
    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Hello!")

        self.assertEqual(node.to_html(), "Hello!")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)

        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_without_props(self):
        node = LeafNode("span", "hello")

        self.assertEqual(
            node.to_html(),
            "<span>hello</span>"
        )

if __name__ == "__main__":
    unittest.main()