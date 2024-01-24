from typing import Dict, List

from html.parser import HTMLParser

SELF_CLOSING_TAGS = {'input', 'br', 'hr', 'img', 'meta', 'link', 'area', 'base', 'col', 'param', 'source'}


class HTMLNode:
    def __init__(self,
                 tag_name: str,
                 attrs: Dict,
                 parent=None):
        self.tag_name = f'{tag_name}_' if tag_name in {'input', 'del', 'map', 'object'} else tag_name
        self.attrs = {
            f'{k}_' if k in {'class', 'for'} else k.replace('-', '_'): v for k, v in attrs.items()
        }
        self.parent = parent
        self.children = []

    def __repr__(self):
        attr_string = ', '.join([f'{k}="{v}"' for k, v in self.attrs.items()]) if self.attrs else ''
        if self.children:
            return f'{self.tag_name}({self.children}, {attr_string})'
        elif attr_string:
            return f'{self.tag_name}({attr_string})'
        else:
            return f'{self.tag_name}()'


class HTMLToClass(HTMLParser):
    def __init__(self):
        super().__init__()
        self.nodes = [HTMLNode('root', {})]

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        node = HTMLNode(tag, attrs, parent=self.nodes[-1])
        self.nodes[-1].children.append(node)
        if tag not in SELF_CLOSING_TAGS:
            self.nodes.append(node)

    def handle_data(self, data):
        if data := data.strip():
            self.nodes[-1].children.append(data)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if self.nodes[-1].tag_name != tag:
            raise ValueError(f'Expected end tag for {self.nodes[-1].tag_name}, got {tag}')
        self.nodes.pop()

    def get_parsed_tree(self):
        return self.nodes[0].children  # drop the root node


def html_to_code(html_string: str) -> str:
    """
    Converts an HTML string to a code representation and returns it.

    This function parses the input HTML string using the HTMLToClass parser,
    then returns the resulting function-based representation of the HTML.

    Parameters
    ----------
    html_string : str
        The HTML string to convert. This should include the full HTML that
        you want to parse, enclosed in quotes.

    Returns
    -------
    a string representation of the HTML

    Examples
    --------
    >>> html_to_code('<div class="example"><p>Some text</p></div>')
    [div([p(['Some text'], )], _class="example")]

    """
    parser = HTMLToClass()
    parser.feed(html_string)
    tree = parser.get_parsed_tree()
    return str(tree)
