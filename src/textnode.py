import re
from enum import Enum
from typing import override

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    text: str
    text_type: TextType
    url: str | None

    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return False

        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    @override
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise ValueError("invalid URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise ValueError("invalid URL")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimeter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        splitted_node_texts = node.text.split(delimeter)
        if len(splitted_node_texts) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")

        split_nodes: list[TextNode] = []

        for i, n in enumerate(splitted_node_texts):
            if n == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(n, TextType.TEXT))
            else:
                split_nodes.append(TextNode(n, text_type))

        new_nodes.extend(split_nodes)

    return new_nodes


def extract_markdown_images(text: str):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images


def extract_markdown_links(text: str):
    links = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links
