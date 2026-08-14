import unittest
from htmlnode import HtmlNode


class HtmlNodeTest(unittest.TestCase):
    def test_to_html(self):
        node = HtmlNode(tag="p", value="Hello World", children=None, props=None)
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HtmlNode(tag="p", value="Hello World", children=None, props={"data-test": "test", "class": "test"})
        self.assertEqual(node.props_to_html(), 'data-test="test" class="test"')

    def test_repr(self):
        node = HtmlNode(tag="p", value="Hello World", children=None, props=None)
        self.assertEqual(repr(node), 'HtmlNode(tag=p, value=Hello World, children=None, props=None)')


if __name__ == "__main__":
    unittest.main()
