from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown: str) -> BlockType:
    
    for i in range(1, 7):
        prefix = "#" * i + " "
        if markdown.startswith(prefix):
            return BlockType.HEADING
    
    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE
    
    lines = markdown.split("\n")

    is_quote = True
    
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break

    if is_quote:
        return BlockType.QUOTE
    
    is_unordered_list = True
    
    for line in lines:
        if not line.startswith("- "):
            is_unordered_list = False
            break

    if is_unordered_list:
        return BlockType.UNORDERED_LIST
    
    is_ordered_list = True

    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            is_ordered_list = False
            break

    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH