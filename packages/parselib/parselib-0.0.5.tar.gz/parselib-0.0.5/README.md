# parselib - HTML parser for web scraping

[![Downloads](https://static.pepy.tech/personalized-badge/parselib?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/parselib)

**[Open an issue](https://github.com/chemtrails/parselib/issues/new)**

---

`pip install parselib`

```py
from parselib import Parser

html = """
    <div class="class-one class-two">
        <div class="class-two">text</div>
    </div>
"""
parser = Parser(html)
div_one = parser.find("*", attrs={"class": "class-two class-one"})
div_two = parser.find("*", attrs={"class": "class-two"}, exclude_attrs={"class": ["class-one"]})
```
