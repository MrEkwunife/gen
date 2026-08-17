import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode


class HtmlNodeTest(unittest.TestCase):
    def test_to_html(self):
        node = HtmlNode(tag="p", value="Hello World", children=None, props=None)
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HtmlNode(
            tag="p",
            value="Hello World",
            children=None,
            props={"data-test": "test", "class": "test"},
        )
        self.assertEqual(node.props_to_html(), ' data-test="test" class="test"')

    def test_repr(self):
        node = HtmlNode(tag="p", value="Hello World", children=None, props=None)
        self.assertEqual(
            repr(node), "HtmlNode(tag=p, value=Hello World, children=None, props=None)"
        )


class LeafNodeTest(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


class ParentNodeTest(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
