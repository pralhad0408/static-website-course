import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Goodbye", TextType.TEXT)

        self.assertNotEqual(node1, node2)

    def test_not_eq_text_type(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Hello", TextType.BOLD)

        self.assertNotEqual(node1, node2)

    def test_not_eq_url(self):
        node1 = TextNode("BootDev", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("BootDev", TextType.LINK, "https://www.boot.dev/dashboard")

        self.assertNotEqual(node1, node2)
    
    def test_eq_url_none(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Hello", TextType.TEXT)

        self.assertEqual(node1, node2)

    def test_not_eq_none_url(self):
        node1 = TextNode("BootDev", TextType.LINK)
        node2 = TextNode("BootDev", TextType.LINK, "https://www.boot.dev")

        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()