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
        max_execution_time = 0.20
        self.assertLessEqual(execution_time, max_execution_time)


class HtmlToStringTesting(unittest.TestCase):
    def test_html_converter(self):
        self.assertEqual(
            """[div([p(['Some text'], )], class_="example")]""",
            str(html_to_code('<div class="example"><p>Some text</p></div>')),
        )


class EscapedHtmlTesting(unittest.TestCase):
    def setUp(self):
        escape_it(True)


    def tearDown(self):
        escape_it(False)


    def test_bad_script_tag(self):
        actual = render(div([div("<script>alert(1)</script>"), div()]))
        expected = "<div><div>&lt;script&gt;alert(1)&lt;/script&gt;</div><div></div></div>"

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
                        td("Birthday"),
                    ])
                ),
                tbody()
            ])
        )
        expected = "<table><thead><tr><td>Student ID</td><td>Name</td><td>Birthday</td></tr></thead><tbody></tbody></table>"

        self.assertEqual(
            expected,
            actual
        )


if __name__ == '__main__':
    doctest.testfile('README.rst')
    unittest.main()
