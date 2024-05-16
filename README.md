**fast_html** is a fast, minimalist HTML generator.


It is an alternative to templating engines, like Jinja,
for use with, e.g., [htmx](https://htmx.org/).

**Pros:**

- use familiar python syntax

- use efficient concatenation techniques

- optional automatic indentation

Unlike other HTML generators (e.g. [Dominate](https://pypi.org/project/dominate/)) that use python objects to represent HTML snippets,
fast_html represents HTML snippets using string [generators](https://docs.python.org/3/glossary.html#term-generator)
that can be rendered extremely fast using `join`.
(see [here](https://python.plainenglish.io/concatenating-strings-efficiently-in-python-9bfc8e8d6f6e))

**Like other HTML generators, one needs to remember:**

- the name of some tags and attributes is changed (e.g., `class_` instead of `class`, due to Python parser)

- there may be conflicts of function names with your code base


Installation
============
`pip install fast_html` or copy the (single) source file in your project.

Don't forget to `add a star on GitHub <https://github.com/pcarbonn/fast_html>`_ ! Thanks.


Tutorial:
=========

    >>> from fast_html import *

A tag is created by calling a function of the corresponding name,
and rendered using `render`:

    >>> print(render(p("text")))
    <p>text</p>

Tag attributes are specified using named arguments:

    >>> print(render(br(id=1)))
    <br id="1">

    >>> print(render(br(id=None)))
    <br>

    >>> print(render(ul(li("text", selected=True))))
    <ul><li selected>text</li></ul>

    >>> print(render(ul(li("text", selected=False))))
    <ul><li>text</li></ul>

The python parser introduces some constraints:

- The following tags require a trailing underscore: `del_`, `input_`, `map_`, `object_`.

- The following tag attributes require a trailing underscore: `class_`, `for_`.

In fact, the trailing underscore in attribute names is always removed by fast_html,
and other underscores are replaced by `-`.
For example, the htmx attribute `hx-get` is set using `hx_get="url"`.

    >>> print(render(object_("text", class_="s12", hx_get="url")))
    <object class="s12" hx-get="url">text</object>

    >>> print(render(button("Click me", hx_post="/clicked", hx_swap="outerHTML")))
    <button hx-post="/clicked" hx-swap="outerHTML">Click me</button>

The innerHTML can be a list:

    >>> print(render(div(["text", span("item 1"), span("item 2")])))
    <div>text<span>item 1</span><span>item 2</span></div>

The innerHTML can also be a list of lists:

    >>> print(render(div(["text", [span(f"item {i}") for i in [1,2]]])))
    <div>text<span>item 1</span><span>item 2</span></div>

    >>> print(render([br(), br()]))
    <br><br>

The innerHTML can also be specified using the `i` parameter,
after the other attributes, to match the order of rendering:

    >>> print(render(ul(class_="s12", i=[
    ...                 li("item 1"),
    ...                 li("item 2")]
    ...      )))
    <ul class="s12"><li>item 1</li><li>item 2</li></ul>

You can create your own tag using the `tag` function:

    >>> def my_tag(inner=None, **kwargs):
    ...     yield from tag("my_tag", inner, **kwargs)
    >>> print(render(my_tag("text")))
    <my_tag>text</my_tag>


Options:
========

By default, the inner string of a tag is not escaped:
characters `&`, `<` and `>` in it are not converted to HTML-safe sequences.


    >>> print(render(p("<bold>text</bold>")))
    <p><bold>text</bold></p>

Of course, you can escape strings before calling fast_html:


    >>> from html import escape
    >>> print(render(p(escape("<bold>text</bold>"))))
    <p>&lt;bold&gt;text&lt;/bold&gt;</p>

If your policy is to escape every inner string,
you can activate escaping by setting the variable `escape` to `True`
(or by calling `escape_it(True)`).

    >>> escape_it(True)
    >>> print(render(p("<bold>text</bold>")))
    <p>&lt;bold&gt;text&lt;/bold&gt;</p>

When debugging your code, you can set global variable `indent` to `True`
(or call `indent_it(True)`) to obtain HTML with tag indentation, e.g.,

    >>> indent_it(True)
    >>> print(render(div(class_="s12", i=["text\n", span("item 1"), span("item 2")])))
    <div class="s12">
      text
      <span>
        item 1
      </span>
      <span>
        item 2
      </span>
    </div>
    <BLANKLINE>

You can also convert an HTML string to a function-based code representation:

    >>> print(html_to_code('<div class="example"><p>Some text</p></div>'))
    [div([p(['Some text'], )], class_="example")]

