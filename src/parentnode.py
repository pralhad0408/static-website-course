from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(
            tag=tag,
            value=None,
            children=children,
            props=props
        )

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag argument is required")
        if self.children is None:
            raise ValueError("Children argument is required")
        
        opening = f"<{self.tag}{self.props_to_html()}>"
        html = ""

        for child in self.children:
            html += child.to_html()

        closing = f"</{self.tag}>"

        return f"{opening}{html}{closing}"