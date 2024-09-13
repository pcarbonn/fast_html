__version__ = '1.0.7'

import re
from html import escape as escape_html
from typing import Iterator, Union, Optional, Iterable, Any, List

from .utils import html_to_code

Tag = Iterator[str]
Inner = Union[Tag, Iterator['Inner'], Any]

_tab = '  '
_cr = '\n'

indent: bool = False
escape: bool = False


def indent_it(value: bool):
    global indent
    indent = value


def escape_it(value: bool):
    global escape
    escape = value


def render(gen: Union[Tag, List[Tag]]) -> str:
    return ''.join(map(render, gen)) if isinstance(gen, list) else ''.join(gen)


def solo_tag(tag_name: str, **kwargs) -> Tag:
    """returns a tag without innerHTML, e.g. `<br id="1">`

    Args:
        tag_name : name of the tag
        kwargs (Dict[str, Optional[Union[str, bool]]]): attributes of the tag
            The `i` attributes, if present, is actually the innerHtml of the tag

    Yields:
        Tag: a string iterator to be rendered
    """

    kwargs = {
        re.sub('_$', '', k).replace('_', '-'): v
        for k, v in kwargs.items()
        if v is not None and (not isinstance(v, bool) or v)
    }

    attrs = "".join(
        f" {k}" if isinstance(v, bool) else f' {k}="{v}"'
        for k, v in kwargs.items()
    )
    yield f"<{tag_name}{attrs}>{_cr if indent else ''}"


def _inner(inner: Inner, with_cr = False):
    """unfold the inner iterators"""
    if isinstance(inner, str):
        yield ((f'{_tab}{inner}{_cr}' if indent and with_cr else
                f'{_tab}{inner}' if indent else
                inner))
    else:
        for i in inner:
            yield from _inner(i)


def escape_inner(inner: Inner) -> Inner:
    if isinstance(inner, str):
        return escape_html(inner)

    elif isinstance(inner, list):
        return map(escape_inner, inner)

    else:
        return inner


def tag(tag_name: str, inner: Optional[Inner] = None, **kwargs) -> Tag:
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
        if escape:
            inner = escape_inner(inner)
        yield from _inner(inner, with_cr = True)

    yield f"</{tag_name}>{_cr if indent else ''}"


# in alphabetic order


def a(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('a', inner, **kwargs)


def abbr(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('abbr', inner, **kwargs)


def address(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('address', inner, **kwargs)


def area(**kwargs) -> Tag:
    yield from solo_tag('area', **kwargs)


def article(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('article', inner, **kwargs)


def aside(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('aside', inner, **kwargs)


def audio(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('audio', inner, **kwargs)


def b(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('b', inner, **kwargs)


def base(**kwargs) -> Tag:
    yield from solo_tag('base', **kwargs)


def bdi(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('bdi', inner, **kwargs)


def bdo(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('bdo', inner, **kwargs)


def blockquote(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('blockquote', inner, **kwargs)


def body(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('body', inner, **kwargs)


def br(**kwargs) -> Tag:
    yield from solo_tag('br', **kwargs)


def button(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('button', inner, **kwargs)


def canvas(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('canvas', inner, **kwargs)


def caption(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('caption', inner, **kwargs)


def cite(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('cite', inner, **kwargs)


def code(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('code', inner, **kwargs)


def col(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('col', inner, **kwargs)


def colgroup(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('colgroup', inner, **kwargs)


def data(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('data', inner, **kwargs)


def datalist(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('datalist', inner, **kwargs)


def dd(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('dd', inner, **kwargs)


def del_(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('del', inner, **kwargs)


def details(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('details', inner, **kwargs)


def dfn(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('dfn', inner, **kwargs)


def dialog(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('dialog', inner, **kwargs)


def div(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('div', inner, **kwargs)


def dl(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('dl', inner, **kwargs)


def dt(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('dt', inner, **kwargs)


def em(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('em', inner, **kwargs)


def embed(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('embed', inner, **kwargs)


def fieldset(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('fieldset', inner, **kwargs)


def figcaption(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('figcaption', inner, **kwargs)


def figure(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('figure', inner, **kwargs)


def footer(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('footer', inner, **kwargs)


def form(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('form', inner, **kwargs)


def h1(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('h1', inner, **kwargs)


def h2(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('h2', inner, **kwargs)


def h3(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('h3', inner, **kwargs)


def h4(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('h4', inner, **kwargs)


def h5(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('h5', inner, **kwargs)


def h6(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('h6', inner, **kwargs)


def head(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('head', inner, **kwargs)


def header(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('header', inner, **kwargs)


def hr(**kwargs) -> Tag:
    yield from solo_tag('hr', **kwargs)


def html(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('html', inner, **kwargs)


def i(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('i', inner, **kwargs)


def iframe(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('iframe', inner, **kwargs)


def img(**kwargs) -> Tag:
    yield from solo_tag('img', **kwargs)


def input_(**kwargs) -> Tag:
    yield from solo_tag('input', **kwargs)


def ins(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('ins', inner, **kwargs)


def kbd(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('kbd', inner, **kwargs)


def label(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('label', inner, **kwargs)


def legend(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('legend', inner, **kwargs)


def li(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('li', inner, **kwargs)


def link(**kwargs) -> Tag:
    yield from solo_tag('link', **kwargs)


def main(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('main', inner, **kwargs)


def map_(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('map', inner, **kwargs)


def mark(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('mark', inner, **kwargs)


def meta(**kwargs) -> Tag:
    yield from solo_tag('meta', **kwargs)


def nav(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('nav', inner, **kwargs)


def noscript(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('noscript', inner, **kwargs)


def object_(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('object', inner, **kwargs)


def ol(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('ol', inner, **kwargs)


def optgroup(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('optgroup', inner, **kwargs)


def option(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('option', inner, **kwargs)


def output(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('output', inner, **kwargs)


def p(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('p', inner, **kwargs)


def param(**kwargs) -> Tag:
    yield from solo_tag('param', **kwargs)


def picture(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('picture', inner, **kwargs)


def pre(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('pre', inner, **kwargs)


def progress(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('progress', inner, **kwargs)


def q(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('q', inner, **kwargs)


def rp(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('rp', inner, **kwargs)


def rt(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('rt', inner, **kwargs)


def ruby(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('ruby', inner, **kwargs)


def s(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('s', inner, **kwargs)


def samp(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('samp', inner, **kwargs)


def script(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('script', inner, **kwargs)


def section(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('section', inner, **kwargs)


def select(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('select', inner, **kwargs)


def small(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('small', inner, **kwargs)


def source(**kwargs) -> Tag:
    yield from solo_tag('source', **kwargs)


def span(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('span', inner, **kwargs)


def strong(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('strong', inner, **kwargs)


def style(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('style', inner, **kwargs)


def sub(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('sub', inner, **kwargs)


def summary(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('summary', inner, **kwargs)


def sup(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('sup', inner, **kwargs)


def svg(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('svg', inner, **kwargs)


def table(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('table', inner, **kwargs)


def tbody(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('tbody', inner, **kwargs)


def td(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('td', inner, **kwargs)


def template(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('template', inner, **kwargs)


def textarea(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('textarea', inner, **kwargs)


def tfoot(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('tfoot', inner, **kwargs)


def th(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('th', inner, **kwargs)


def thead(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('thead', inner, **kwargs)


def time(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('time', inner, **kwargs)


def title(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('title', inner, **kwargs)


def tr(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('tr', inner, **kwargs)


def track(**kwargs) -> Tag:
    yield from solo_tag('track', **kwargs)


def u(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('u', inner, **kwargs)


def ul(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('ul', inner, **kwargs)


def var(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('var', inner, **kwargs)


def video(inner: Optional[Inner] = None, **kwargs) -> Tag:
    yield from tag('video', inner, **kwargs)


def wbr(**kwargs) -> Tag:
    yield from solo_tag('wbr', **kwargs)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
