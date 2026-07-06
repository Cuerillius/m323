from __future__ import annotations
from dataclasses import dataclass
from functools import reduce
import requests
import re


@dataclass(frozen=True)
class Page:
    main: str
    links: tuple[Page, ...] = ()

def parse_urls(html: str) -> tuple[str, ...]:
    found = re.findall(
        r"https?://[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&//=]*",
        html,
    )
    return tuple(set(found))


def to_string(page: Page, indent: int = 0) -> str:
    prefix = "   " * indent
    children = [to_string(p, indent + 1) for p in page.links]
    return prefix + page.main + "\n" + "".join(children)


def pipeline(*fns):
    return reduce(lambda v, f: f(v), fns)


def fetch_html(url: str) -> str:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
        timeout=5,
    )
    return response.text if response.status_code == 200 else ""


def find_links(url: str, depth: int) -> Page:
    if depth <= 0:
        return Page(url)
    urls = pipeline(url, fetch_html, parse_urls)
    child_urls = filter(lambda u: u != url, urls)
    return Page(url, tuple(find_links(u, depth - 1) for u in child_urls))


def main():
    output = pipeline("https://www.restaurantlemon.ch", lambda url: find_links(url, 2), to_string)
    print(output)
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(output)


import unittest
from unittest.mock import patch


class TestCrawler(unittest.TestCase):
    def test_parse_urls_finds_links(self):
        html = 'See <a href="https://example.com">here</a> and <a href="https://test.org/page">there</a>'
        result = parse_urls(html)
        self.assertIn("https://example.com", result)
        self.assertIn("https://test.org/page", result)

    def test_parse_urls_empty(self):
        self.assertEqual(parse_urls("no urls here"), ())

    def test_to_string_single(self):
        self.assertEqual(to_string(Page("https://example.com")), "https://example.com\n")

    def test_to_string_nested(self):
        parent = Page("https://parent.com", (Page("https://child.com"),))
        result = to_string(parent)
        self.assertIn("https://parent.com\n", result)
        self.assertIn("   https://child.com\n", result)

    @patch("crawler.fetch_html", return_value='<a href="https://linked.com">link</a>')
    def test_find_links(self, _mock):
        page = find_links("https://root.com", 1)
        self.assertEqual(page.main, "https://root.com")
        self.assertTrue(any(p.main == "https://linked.com" for p in page.links))

    def test_find_links_depth_zero(self):
        page = find_links("https://root.com", 0)
        self.assertEqual(page.links, ())


if __name__ == "__main__":
    main()
