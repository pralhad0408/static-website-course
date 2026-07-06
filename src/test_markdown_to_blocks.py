import unittest

from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_remove_empty_blocks(self):
        md = """
First block



Second block



Third block
"""
        self.assertEqual(
            markdown_to_blocks(md),
            [
                "First block",
                "Second block",
                "Third block",
            ],
        )
    
    def test_empty_markdown(self):
        self.assertEqual(markdown_to_blocks(""), [])

if __name__ == "__main__":
    unittest.main()