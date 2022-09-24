__version__ = '1.0.0'

indent = False


from typing import Iterator, List, Optional, Union
import re

Tag = Iterator[str]
Inner = Union[str, Tag, Iterator['Inner']]

_tab = "  "
_cr = "\n"

def indent_it(value):
    global indent
    indent = value

def render(gen: Tag) -> str:
    return ''.join(gen)


def solo_tag(tag_name: str, ** kwargs) -> Tag:
    """returns a tag without innerHTML, e.g. `<br id="1">`

    Args:
        tag_name : name of the tag
        kwargs (Dict[str, Optional[Union[str, bool]]]): attributes of the tag
            The `i` attributes, if present, is actually the innerHtml of the tag

    Yields:
        Tag: a string iterator to be rendered
    """

    kwargs = { re.sub("_$", "", k).replace("_", "-"): v
               for k, v in kwargs.items()
               if v is not None and (type(v) != bool or v)}

    attrs = ""
    for k,v in kwargs.items():
        if type(v) == bool:
                attrs += f' {k}'
        else:
                attrs += f' {k}="{v}"'

    yield f"<{tag_name}{attrs}>{_cr if indent else ''}"


def _inner(inner: Inner):
    """ unfold the inner iterators """
    if type(inner) == str:  # inner is a str
        yield (f"{_tab}{inner}" if indent else inner)
    else:
        for i in inner:
            yield from _inner(i)


def tag(tag_name: str,
        inner: Inner = None,
        **kwargs
        ) -> Tag:
    """returns a generator of strings, to be rendered as a HTML tag of type `name`

    Args:
        tag_name : name of the tag
        inner : innerHTML of the tag, or None
        kwargs (Dict[str, Optional[Union[str, bool]]]): attributes of the tag
            The `i` attributes, if present, is actually the innerHtml of the tag

    Yields:
        Tag: a string iterator to be rendered
    """
    if 'i' in kwargs:
        inner = kwargs['i']
        del kwargs['i']

    yield from solo_tag(tag_name, **kwargs)

    if inner is not None:
        if type(inner) == str:  # inner is a str
            yield (f"{_tab}{inner}{_cr}" if indent else inner)
        else:
            for i in inner:
                if type(i) == str:  # inner is a Tag
                    yield (f"{_tab}{i}{_cr}" if indent else i)
                else:
                    for i1 in i:
                        yield from _inner(i1)

    yield f"</{tag_name}>{_cr if indent else ''}"


# in alphabetic order

def a(inner=None, **kwargs):
    yield from tag("a", inner, **kwargs)


def abbr(**kwargs):
    yield from tag("abbr", **kwargs)


def address(**kwargs):
    yield from tag("address", **kwargs)


def area(**kwargs):
    yield from solo_tag("area", **kwargs)


def article(**kwargs):
    yield from tag("article", **kwargs)


def aside(**kwargs):
    yield from tag("aside", **kwargs)


def audio(**kwargs):
    yield from tag("audio", **kwargs)


def b(**kwargs):
    yield from tag("b", **kwargs)


def base(**kwargs):
    yield from solo_tag("base", **kwargs)


def bdi(**kwargs):
    yield from tag("bdi", **kwargs)


def bdo(**kwargs):
    yield from tag("bdo", **kwargs)


def blockquote(**kwargs):
    yield from tag("blockquote", **kwargs)


def body(inner=None, **kwargs):
    yield from tag("body", inner, **kwargs)


def br(**kwargs):
    yield from solo_tag("br", **kwargs)


def button(inner=None, **kwargs):
    yield from tag("button", inner, **kwargs)


def canvas(**kwargs):
    yield from tag("canvas", **kwargs)


def caption(**kwargs):
    yield from tag("caption", **kwargs)


def cite(**kwargs):
    yield from tag("cite", **kwargs)


def code(**kwargs):
    yield from tag("code", **kwargs)


def col(**kwargs):
    yield from tag("col", **kwargs)


def colgroup(**kwargs):
    yield from tag("colgroup", **kwargs)


def data(**kwargs):
    yield from tag("data", **kwargs)


def datalist(**kwargs):
    yield from tag("datalist", **kwargs)


def dd(**kwargs):
    yield from tag("dd", **kwargs)


def del_(**kwargs):
    yield from tag("del", **kwargs)


def details(**kwargs):
    yield from tag("details", **kwargs)


def dfn(**kwargs):
    yield from tag("dfn", **kwargs)


def dialog(**kwargs):
    yield from tag("dialog", **kwargs)


def div(inner=None, **kwargs):
    yield from tag("div", inner, **kwargs)


def dl(**kwargs):
    yield from tag("dl", **kwargs)


def dt(**kwargs):
    yield from tag("dt", **kwargs)


def em(**kwargs):
    yield from tag("em", **kwargs)


def embed(**kwargs):
    yield from tag("embed", **kwargs)


def fieldset(**kwargs):
    yield from tag("fieldset", **kwargs)


def figcaption(**kwargs):
    yield from tag("figcaption", **kwargs)


def figure(**kwargs):
    yield from tag("figure", **kwargs)


def footer(**kwargs):
    yield from tag("footer", **kwargs)


def form(inner=None, **kwargs):
    yield from tag("form", inner, **kwargs)

def h1(**kwargs):
    yield from tag("h1", **kwargs)


def h2(**kwargs):
    yield from tag("h2", **kwargs)


def h3(**kwargs):
    yield from tag("h3", **kwargs)


def h4(**kwargs):
    yield from tag("h4", **kwargs)


def h5(**kwargs):
    yield from tag("h5", **kwargs)


def h6(**kwargs):
    yield from tag("h6", **kwargs)


def head(**kwargs):
    yield from tag("head", **kwargs)


def header(**kwargs):
    yield from tag("header", **kwargs)


def hr(**kwargs):
    yield from solo_tag("hr", **kwargs)


def html(**kwargs):
    yield from tag("html", **kwargs)


def i(inner=None, **kwargs):
    yield from tag("i", inner, **kwargs)

def iframe(**kwargs):
    yield from tag("iframe", **kwargs)


def img(**kwargs):
    yield from solo_tag("img", **kwargs)


def input(**kwargs):
    yield from solo_tag("input", **kwargs)

def ins(**kwargs):
    yield from tag("ins", **kwargs)


def kbd(**kwargs):
    yield from tag("kbd", **kwargs)


def label(inner=None, **kwargs):
    yield from tag("label", inner, **kwargs)

def legend(**kwargs):
    yield from tag("legend", **kwargs)


def li(inner=None, **kwargs):
    yield from tag("li", inner, **kwargs)

def link(**kwargs):
    yield from solo_tag("link", **kwargs)


def main(**kwargs):
    yield from tag("main", **kwargs)


def map(**kwargs):
    yield from tag("map", **kwargs)


def mark(**kwargs):
    yield from tag("mark", **kwargs)


def meta(**kwargs):
    yield from solo_tag("meta", **kwargs)


def nav(**kwargs):
    yield from tag("nav", **kwargs)


def noscript(**kwargs):
    yield from tag("noscript", **kwargs)


def object_(**kwargs):
    yield from tag("object", **kwargs)


def ol(**kwargs):
    yield from tag("ol", **kwargs)


def optgroup(**kwargs):
    yield from tag("optgroup", **kwargs)


def option(**kwargs):
    yield from tag("option", **kwargs)


def output(**kwargs):
    yield from tag("output", **kwargs)


def p(inner=None, **kwargs):
    yield from tag("p", inner, **kwargs)

def param(**kwargs):
    yield from solo_tag("param", **kwargs)


def picture(**kwargs):
    yield from tag("picture", **kwargs)


def pre(**kwargs):
    yield from tag("pre", **kwargs)


def progress(**kwargs):
    yield from tag("progress", **kwargs)


def q(**kwargs):
    yield from tag("q", **kwargs)


def rp(**kwargs):
    yield from tag("rp", **kwargs)


def rt(**kwargs):
    yield from tag("rt", **kwargs)


def ruby(**kwargs):
    yield from tag("ruby", **kwargs)


def s(**kwargs):
    yield from tag("s", **kwargs)


def samp(**kwargs):
    yield from tag("samp", **kwargs)


def script(**kwargs):
    yield from tag("script", **kwargs)


def section(**kwargs):
    yield from tag("section", **kwargs)


def select(**kwargs):
    yield from tag("select", **kwargs)


def small(**kwargs):
    yield from tag("small", **kwargs)


def source(**kwargs):
    yield from solo_tag("source", **kwargs)


def span(inner=None, **kwargs):
    yield from tag("span", inner, **kwargs)

def strong(**kwargs):
    yield from tag("strong", **kwargs)


def style(**kwargs):
    yield from tag("style", **kwargs)


def sub(**kwargs):
    yield from tag("sub", **kwargs)


def summary(**kwargs):
    yield from tag("summary", **kwargs)


def sup(**kwargs):
    yield from tag("sup", **kwargs)


def svg(**kwargs):
    yield from tag("svg", **kwargs)


def table(inner=None, **kwargs):
    yield from tag("table", inner, **kwargs)


def tbody(**kwargs):
    yield from tag("tbody", **kwargs)


def td(inner=None, **kwargs):
    yield from tag("td", inner, **kwargs)


def template(**kwargs):
    yield from tag("template", **kwargs)


def textarea(**kwargs):
    yield from tag("textarea", **kwargs)


def tfoot(**kwargs):
    yield from tag("tfoot", **kwargs)


def th(inner=None, **kwargs):
    yield from tag("th", inner, **kwargs)


def thead(**kwargs):
    yield from tag("thead", **kwargs)


def time(**kwargs):
    yield from tag("time", **kwargs)


def title(**kwargs):
    yield from tag("title", **kwargs)


def tr(inner=None, **kwargs):
    yield from tag("tr", inner, **kwargs)


def track(**kwargs):
    yield from solo_tag("track", **kwargs)


def u(**kwargs):
    yield from tag("u", **kwargs)


def ul(inner=None, **kwargs):
    yield from tag("ul", inner, **kwargs)

def var(**kwargs):
    yield from tag("var", **kwargs)


def video(**kwargs):
    yield from tag("video", **kwargs)


def wbr(**kwargs):
    yield from solo_tag("wbr", **kwargs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()