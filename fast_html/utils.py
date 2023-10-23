from html.parser import HTMLParser

SELF_CLOSING_TAGS = {'input', 'br', 'hr', 'img', 'meta', 'link', 'area', 'base', 'col', 'param', 'source'}


class HTMLNode:
    def __init__(self, tag_name, attrs, parent=None):
        self.tag_name = f'{tag_name}_' if tag_name in {'input', 'del'} else tag_name
        self.attrs = {
            f'_{k.replace("-", "_")}' if k in {'class', 'for'} else k.replace('-', '_'): v for k, v in attrs.items()
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
            return f'{self.tag_name}'


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

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if self.nodes[-1].tag_name != tag:
            raise ValueError(f'Expected end tag for {self.nodes[-1].tag_name}, got {tag}')
        self.nodes.pop()

    def get_parsed_tree(self):
        return self.nodes[0]


def print_html_to_class(html_string: str) -> None:
    """
    Converts an HTML string to a class representation and prints it.

    This function parses the input HTML string using the HTMLToClass parser,
    then prints the resulting class-based representation of the HTML.

    Parameters
    ----------
    html_string : str
        The HTML string to convert and print. This should include the full HTML that
        you want to parse, enclosed in quotes.

    Returns
    -------
    None

    Examples
    --------
    >>> print_html_to_class('<div class="example"><p>Some text</p></div>')
    div([p(['Some Text'], )], _class="example")

    Notes
    -----
    - The function calls the feed method of the HTMLToClass parser with the input string.
    - It then obtains a class-based tree representation of the HTML using the parse tree from the parser.
    - The class-based tree representation of the HTML string is printed to standard output.
    - The function does not return a value.
    """
    parser = HTMLToClass()
    parser.feed(html_string)
    print(parser.get_parsed_tree())
