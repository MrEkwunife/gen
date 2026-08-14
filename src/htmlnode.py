class HtmlNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: object | None = None,
                 props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if not self.props or self.props == "":
            return ""

        return "".join([f' {key}="{value}"' for key, value in self.props.items()])

    def __repr__(self) -> str:
        return f"HtmlNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HtmlNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props=props)

    def to_html(self) -> str:
        if not self.value or self.value == "":
            raise ValueError("LeafNode value cannot be empty")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"HtmlNode(tag={self.tag}, value={self.value}, props={self.props})"