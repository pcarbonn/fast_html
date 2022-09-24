This module contains functions to generate HTML conveniently and efficiently.

It is an alternative to templating engines, like Jinja,
for use with, e.g., `htmx <https://htmx.org/>`__.

Pros:

- use familiar python syntax

- use efficient concatenation techniques (`join`, see `here <https://python.plainenglish.io/concatenating-strings-efficiently-in-python-9bfc8e8d6f6e>`__)

- optional automatic indentation

Cons:

- the name of some tag attributes is changed (e.g., ``class_`` instead of ``class``, due to Python parser)

- possible conflicts of function names in your code base


Installation
------------
``pip install htmx_gen`` or copy the (single) source file in your project.

Don't forget to `add a star on GitHub <https://github.com/pcarbonn/htmx_gen>`_ ! Thanks.


Tutorial:
---------

>>> from htmx_gen import *

A tag is created by calling a function of the corresponding name,
and rendered using ``render``:

>>> print(render(p("text")))
<p>text</p>


Tag attributes are specified using named arguments:

>>> print(render(br(id="1")))
<br id="1">

>>> print(render(br(id=None)))
<br>

>>> print(render(ul(li("text", selected=True))))
<ul><li selected>text</li></ul>

>>> print(render(ul(li("text", selected=False))))
<ul><li>text</li></ul>


Some tag attributes are changed: you must add ``_`` to tag (or attribute) names
conflicting with Python reserved names, (e.g. ``class_`` instead of ``class``),
and you must use ``_`` instead of ``-`` in attribute names.

>>> print(render(p("text", class_="s12", hx_get="url")))
<p class="s12" hx-get="url">text</p>

>>> print(render(button("Click me", hx_post="/clicked", hx_swap="outerHTML")))
<button hx-post="/clicked" hx-swap="outerHTML">Click me</button>


The innerHTML can be a list:

>>> print(render(div(["text", span("item 1"), span("item 2")])))
<div>text<span>item 1</span><span>item 2</span></div>

The innerHTML can also be a list of lists:

>>> print(render(div(["text", [span(f"item {i}") for i in [1,2]]])))
<div>text<span>item 1</span><span>item 2</span></div>


The innerHTML can also be specified using the ``i`` parameter,
after the other attributes, to match the order of rendering:

>>> print(render(ul(class_="s12", i=[
...                 li("item 1"),
...                 li("item 2")]
...      )))
<ul class="s12"><li>item 1</li><li>item 2</li></ul>


When debugging your code, you can set global variable ``indent`` to ``True``
(or call ``indent_it(True)``) to obtain HTML with tag indentation, e.g.,

>>> indent_it(True); print(render(div(class_="s12", i=["text", span("item 1"), span("item 2")])))
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
