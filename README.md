# Smart Text Decorator <sup>v1.0.0</sup>

Smart text decorator. A library for decorating strings and displaying them beautifully in the console.

- Generates and displays lines to the full width of the console with the specified text and a placeholder character.
- Generates and displays a line with the specified text, decorated at the top and bottom with filler characters along the length of the line.

> Use for beautiful design of console applications.

---

Author and developer: [___Alexander Suvorov___](https://github.com/smartlegionlab)

---

[![PyPI Downloads](https://static.pepy.tech/badge/smarttextdecorator)](https://pepy.tech/projects/smarttextdecorator)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smarttextdecorator)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smarttextdecorator?label=pypi%20downloads)](https://pypi.org/project/smarttextdecorator/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smarttextdecorator)](https://github.com/smartlegionlab/smarttextdecorator/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smarttextdecorator)](https://github.com/smartlegionlab/smarttextdecorator/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/smarttextdecorator)](https://pypi.org/project/smarttextdecorator)
[![PyPI - Format](https://img.shields.io/pypi/format/smarttextdecorator)](https://pypi.org/project/smarttextdecorator)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smarttextdecorator?style=social)](https://github.com/smartlegionlab/smarttextdecorator/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smarttextdecorator?style=social)](https://github.com/smartlegionlab/smarttextdecorator/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smarttextdecorator?style=social)](https://github.com/smartlegionlab/smarttextdecorator/)


---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](https://github.com/smartlegionlab/smarttextdecorator/blob/master/DISCLAIMER.md)

---

## Help

- `pip install smarttextdecorator`

```python
from smarttextdecorator import SmartPrinter

SmartPrinter.print_framed(symbol='-')
SmartPrinter.print_center(text='Smart Legion Lab')

```

### Example

```python
from smarttextdecorator import SmartPrinter


def main():
    SmartPrinter.show_head(text='Smart Legion Lab')
    print()
    SmartPrinter.print_framed(text='Hello World!!!')
    print()
    SmartPrinter.show_footer(url='https://github.com/smartlegionlab/', copyright_='Copyright © 2024, Alexander Suvorov. All rights reserved.')


if __name__ == '__main__':
    main()

```

![logo](https://github.com/smartlegionlab/smarttextdecorator/raw/master/data/images/smarttextdecorator.png)

---

## License

**[BSD 3-Clause License](https://github.com/smartlegionlab/smarttextdecorator/blob/master/LICENSE)**

Copyright (©) 2026, [Alexander Suvorov](https://github.com/smartlegionlab)

---
