from textnode import TextNode, TextType


def main() -> None:
    anchorNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(anchorNode)


main()
