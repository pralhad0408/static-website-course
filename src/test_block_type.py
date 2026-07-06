import unittest

from block_type import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        md = "# This is a heading"

        self.assertEqual(
            block_to_block_type(md),
            BlockType.HEADING,
        )

    def test_code(self):
        md = """
```
print("Hello, world")
```
""".strip()
        
        self.assertEqual(
            block_to_block_type(md),
            BlockType.CODE,
        )

    def test_quote(self):
        md = "> This is a quote"

        self.assertEqual(
            block_to_block_type(md),
            BlockType.QUOTE,
        )

    def test_unordered_list(self):
        md = """
- This is the first list item in a list block
- This is the second list item
- This is the third list item
""".strip()

        self.assertEqual(
            block_to_block_type(md),
            BlockType.UNORDERED_LIST,
        )

    def test_ordered_list(self):
        md = """
1. This is the first item in a list block
2. This is the second item
3. This is the third item
""".strip()
        
        self.assertEqual(
            block_to_block_type(md),
            BlockType.ORDERED_LIST,
        )

    def test_paragraph(self):
        md = "This is a paragraph text with no headings"
        self.assertEqual(
            block_to_block_type(md), 
            BlockType.PARAGRAPH,
        )

    def test_invalid_heading(self):
        self.assertEqual(
            block_to_block_type("####### Too many hashes"),
            BlockType.PARAGRAPH,
        )
    
    def test_invalid_ordered_list(self):
        self.assertEqual(
            block_to_block_type("2. Second\n3. Third"),
            BlockType.PARAGRAPH,
        )

    def test_invalid_quote(self):
        md = "> First line\nSecond line"

        self.assertEqual(
            block_to_block_type(md),
            BlockType.PARAGRAPH,
        )

    def test_invalid_unordered_list(self):
        md = "- First item\nSecond item"

        self.assertEqual(
            block_to_block_type(md),
            BlockType.PARAGRAPH,
        )

    def test_invalid_ordered_list_skips_number(self):
        md = "1. First\n3. Third"

        self.assertEqual(
            block_to_block_type(md),
            BlockType.PARAGRAPH,
        )

    def test_heading_level_6(self):
        self.assertEqual(
            block_to_block_type("###### Heading"),
            BlockType.HEADING,
        )

if __name__ == "__main__":
    unittest.main()