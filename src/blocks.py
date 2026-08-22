def markdown_to_blocks(markdown: str) -> list[str]:

    if not markdown:
        return []

    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks]
