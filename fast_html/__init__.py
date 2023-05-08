__version__ = '1.0.3'

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
    if type(gen) == list:
        return ''.join(render(t) for t in gen)
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
                    yield (f"{_tab}{i}" if indent else i)
                else:
                    for i1 in i:
                        yield from _inner(i1)

    yield f"</{tag_name}>{_cr if indent else ''}"


# in alphabetic order

def a(inner=None, **kwargs):
    yield from tag("a", inner, **kwargs)


def abbr(inner=None, **kwargs):
    yield from tag("abbr", inner, **kwargs)


def address(inner=None, **kwargs):
    yield from tag("address", inner, **kwargs)


def area(**kwargs):
    yield from solo_tag("area", **kwargs)


def article(inner=None, **kwargs):
    yield from tag("article", inner, **kwargs)


def aside(inner=None, **kwargs):
    yield from tag("aside", inner, **kwargs)


def audio(inner=None, **kwargs):
    yield from tag("audio", inner, **kwargs)


def b(inner=None, **kwargs):
    yield from tag("b", inner, **kwargs)


def base(**kwargs):
    yield from solo_tag("base", **kwargs)


def bdi(inner=None, **kwargs):
    yield from tag("bdi", inner, **kwargs)


def bdo(inner=None, **kwargs):
    yield from tag("bdo", inner, **kwargs)


def blockquote(inner=None, **kwargs):
    yield from tag("blockquote", inner, **kwargs)


def body(inner=None, **kwargs):
    yield from tag("body", inner, **kwargs)


def br(**kwargs):
    yield from solo_tag("br", **kwargs)


def button(inner=None, **kwargs):
    yield from tag("button", inner, **kwargs)


def canvas(inner=None, **kwargs):
    yield from tag("canvas", inner, **kwargs)


def caption(inner=None, **kwargs):
    yield from tag("caption", inner, **kwargs)


def cite(inner=None, **kwargs):
    yield from tag("cite", inner, **kwargs)


def code(inner=None, **kwargs):
    yield from tag("code", inner, **kwargs)


def col(inner=None, **kwargs):
    yield from tag("col", inner, **kwargs)


def colgroup(inner=None, **kwargs):
    yield from tag("colgroup", inner, **kwargs)


def data(inner=None, **kwargs):
    yield from tag("data", inner, **kwargs)


def datalist(inner=None, **kwargs):
    yield from tag("datalist", inner, **kwargs)


def dd(inner=None, **kwargs):
    yield from tag("dd", inner, **kwargs)


def del_(inner=None, **kwargs):
    yield from tag("del", inner, **kwargs)


def details(inner=None, **kwargs):
    yield from tag("details", inner, **kwargs)


def dfn(inner=None, **kwargs):
    yield from tag("dfn", inner, **kwargs)


def dialog(inner=None, **kwargs):
    yield from tag("dialog", inner, **kwargs)


def div(inner=None, **kwargs):
    yield from tag("div", inner, **kwargs)


def dl(inner=None, **kwargs):
    yield from tag("dl", inner, **kwargs)


def dt(inner=None, **kwargs):
    yield from tag("dt", inner, **kwargs)


def em(inner=None, **kwargs):
    yield from tag("em", inner, **kwargs)


def embed(inner=None, **kwargs):
    yield from tag("embed", inner, **kwargs)


def fieldset(inner=None, **kwargs):
    yield from tag("fieldset", inner, **kwargs)


def figcaption(inner=None, **kwargs):
    yield from tag("figcaption", inner, **kwargs)


def figure(inner=None, **kwargs):
    yield from tag("figure", inner, **kwargs)


def footer(inner=None, **kwargs):
    yield from tag("footer", inner, **kwargs)


def form(inner=None, **kwargs):
    yield from tag("form", inner, **kwargs)

def h1(inner=None, **kwargs):
    yield from tag("h1", inner, **kwargs)


def h2(inner=None, **kwargs):
    yield from tag("h2", inner, **kwargs)


def h3(inner=None, **kwargs):
    yield from tag("h3", inner, **kwargs)


def h4(inner=None, **kwargs):
    yield from tag("h4", inner, **kwargs)


def h5(inner=None, **kwargs):
    yield from tag("h5", inner, **kwargs)


def h6(inner=None, **kwargs):
    yield from tag("h6", inner, **kwargs)


def head(inner=None, **kwargs):
    yield from tag("head", inner, **kwargs)


def header(inner=None, **kwargs):
    yield from tag("header", inner, **kwargs)


def hr(**kwargs):
    yield from solo_tag("hr", **kwargs)


def html(inner=None, **kwargs):
    yield from tag("html", inner, **kwargs)


def i(inner=None, **kwargs):
    yield from tag("i", inner, **kwargs)

def iframe(inner=None, **kwargs):
    yield from tag("iframe", inner, **kwargs)


def img(**kwargs):
    yield from solo_tag("img", **kwargs)


def input_( **kwargs):
    yield from solo_tag("input", **kwargs)

def ins(inner=None, **kwargs):
    yield from tag("ins", inner, **kwargs)


def kbd(inner=None, **kwargs):
    yield from tag("kbd", inner, **kwargs)


def label(inner=None, **kwargs):
    yield from tag("label", inner, **kwargs)

def legend(inner=None, **kwargs):
    yield from tag("legend", inner, **kwargs)


def li(inner=None, **kwargs):
    yield from tag("li", inner, **kwargs)

def link(**kwargs):
    yield from solo_tag("link", **kwargs)


def main(inner=None, **kwargs):
    yield from tag("main", inner, **kwargs)


def map_(inner=None, **kwargs):
    yield from tag("map", inner, **kwargs)


def mark(inner=None, **kwargs):
    yield from tag("mark", inner, **kwargs)


def meta(**kwargs):
    yield from solo_tag("meta", **kwargs)


def nav(inner=None, **kwargs):
    yield from tag("nav", inner, **kwargs)


def noscript(inner=None, **kwargs):
    yield from tag("noscript", inner, **kwargs)


def object_(inner=None, **kwargs):
    yield from tag("object", inner, **kwargs)


def ol(inner=None, **kwargs):
    yield from tag("ol", inner, **kwargs)


def optgroup(inner=None, **kwargs):
    yield from tag("optgroup", inner, **kwargs)


def option(inner=None, **kwargs):
    yield from tag("option", inner, **kwargs)


def output(inner=None, **kwargs):
    yield from tag("output", inner, **kwargs)


def p(inner=None, **kwargs):
    yield from tag("p", inner, **kwargs)

def param(**kwargs):
    yield from solo_tag("param", **kwargs)


def picture(inner=None, **kwargs):
    yield from tag("picture", inner, **kwargs)


def pre(inner=None, **kwargs):
    yield from tag("pre", inner, **kwargs)


def progress(inner=None, **kwargs):
    yield from tag("progress", inner, **kwargs)


def q(inner=None, **kwargs):
    yield from tag("q", inner, **kwargs)


def rp(inner=None, **kwargs):
    yield from tag("rp", inner, **kwargs)


def rt(inner=None, **kwargs):
    yield from tag("rt", inner, **kwargs)


def ruby(inner=None, **kwargs):
    yield from tag("ruby", inner, **kwargs)


def s(inner=None, **kwargs):
    yield from tag("s", inner, **kwargs)


def samp(inner=None, **kwargs):
    yield from tag("samp", inner, **kwargs)


def script(inner=None, **kwargs):
    yield from tag("script", inner, **kwargs)


def section(inner=None, **kwargs):
    yield from tag("section", inner, **kwargs)


def select(inner=None, **kwargs):
    yield from tag("select", inner, **kwargs)


def small(inner=None, **kwargs):
    yield from tag("small", inner, **kwargs)


def source(**kwargs):
    yield from solo_tag("source", **kwargs)


def span(inner=None, **kwargs):
    yield from tag("span", inner, **kwargs)

def strong(inner=None, **kwargs):
    yield from tag("strong", inner, **kwargs)


def style(inner=None, **kwargs):
    yield from tag("style", inner, **kwargs)


def sub(inner=None, **kwargs):
    yield from tag("sub", inner, **kwargs)


def summary(inner=None, **kwargs):
    yield from tag("summary", inner, **kwargs)


def sup(inner=None, **kwargs):
    yield from tag("sup", inner, **kwargs)


def svg(inner=None, **kwargs):
    yield from tag("svg", inner, **kwargs)


def table(inner=None, **kwargs):
    yield from tag("table", inner, **kwargs)


def tbody(inner=None, **kwargs):
    yield from tag("tbody", inner, **kwargs)


def td(inner=None, **kwargs):
    yield from tag("td", inner, **kwargs)


def template(inner=None, **kwargs):
    yield from tag("template", inner, **kwargs)


def textarea(inner=None, **kwargs):
    yield from tag("textarea", inner, **kwargs)


def tfoot(inner=None, **kwargs):
    yield from tag("tfoot", inner, **kwargs)


def th(inner=None, **kwargs):
    yield from tag("th", inner, **kwargs)


def thead(inner=None, **kwargs):
    yield from tag("thead", inner, **kwargs)


def time(inner=None, **kwargs):
    yield from tag("time", inner, **kwargs)


def title(inner=None, **kwargs):
    yield from tag("title", inner, **kwargs)


def tr(inner=None, **kwargs):
    yield from tag("tr", inner, **kwargs)


def track(**kwargs):
    yield from solo_tag("track", **kwargs)


def u(inner=None, **kwargs):
    yield from tag("u", inner, **kwargs)


def ul(inner=None, **kwargs):
    yield from tag("ul", inner, **kwargs)

def var(inner=None, **kwargs):
    yield from tag("var", inner, **kwargs)


def video(inner=None, **kwargs):
    yield from tag("video", inner, **kwargs)


def wbr(**kwargs):
    yield from solo_tag("wbr", **kwargs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()