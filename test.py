import doctest
import unittest
from time import time as timeobj

from fast_html import *


class PerformanceTesting(unittest.TestCase):
    def test_large_structure_generation_performance(self):
        num_divs = 100000
        start_time = timeobj()
        for _ in range(num_divs):
            ''.join(div('Content'))
        end_time = timeobj()
        execution_time = end_time - start_time
        max_execution_time = 0.3
        self.assertLessEqual(execution_time, max_execution_time)


class HtmlToStringTesting(unittest.TestCase):
    def test_html_converter(self):
        self.assertEqual(
            """[div([p(['Some text'], )], class_="example")]""",
            str(html_to_code('<div class="example"><p>Some text</p></div>')),
        )

    def test_underscore(self):
        self.assertEqual(
            """[div([p(['Some text'], )], _="example", hidden=True)]""",
            str(html_to_code('<div _="example" hidden><p>Some text</p></div>')),
        )


class EscapedHtmlTesting(unittest.TestCase):
    def setUp(self):
        escape_it(True)
        indent_it(False)


    def tearDown(self):
        escape_it(False)
        indent_it(True)


    def test_bad_script_tag(self):
        actual = render(div([div("<script>alert(1)</script>"), div()]))
        expected = "<div><div>&lt;script&gt;alert(1)&lt;/script&gt;</div><div></div></div>"

        self.assertEqual(
            expected,
            actual
        )


    def test_bad_script_tag_with_sibling(self):
        actual = render(div([div(["<script>alert(1)</script>", div()]), div()]))
        expected = "<div><div>&lt;script&gt;alert(1)&lt;/script&gt;<div></div></div><div></div></div>"

        self.assertEqual(
            expected,
            actual
        )


    def test_bad_script_tag_with_nested_lists(self):
        actual = render(div([div([["<script>alert(1)</script>"], div()]), div()]))
        expected = "<div><div>&lt;script&gt;alert(1)&lt;/script&gt;<div></div></div><div></div></div>"

        self.assertEqual(
            expected,
            actual
        )


    def test_deeper_nesting(self):
        actual = render(
            table([
                thead(
                    tr([
                        td("Student ID"),
                        td("Name"),
                        td("<bold>Birthday</bold>"),
                    ])
                ),
                tbody()
            ])
        )
        expected = "<table><thead><tr><td>Student ID</td><td>Name</td><td>&lt;bold&gt;Birthday&lt;/bold&gt;</td></tr></thead><tbody></tbody></table>"

        self.assertEqual(
            expected,
            actual
        )


if __name__ == '__main__':
    doctest.testfile('README.md')
    unittest.main()
