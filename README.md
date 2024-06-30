# Smart Text Decorator
Smart text decorator.
A library for decorating strings and displaying them beautifully in the console.
***

Author and developer: ___A.A. Suvorov___

***

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smarttextdecorator)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smarttextdecorator?label=pypi%20downloads)](https://pypi.org/project/smarttextdecorator/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smarttextdecorator)](https://github.com/smartlegionlab/smarttextdecorator/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smarttextdecorator)](https://github.com/smartlegionlab/smarttextdecorator/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/smarttextdecorator)](https://pypi.org/project/smarttextdecorator)
[![PyPI - Format](https://img.shields.io/pypi/format/smarttextdecorator)](https://pypi.org/project/smarttextdecorator)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smarttextdecorator?style=social)](https://github.com/smartlegionlab/smarttextdecorator/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smarttextdecorator?style=social)](https://github.com/smartlegionlab/smarttextdecorator/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smarttextdecorator?style=social)](https://github.com/smartlegionlab/smarttextdecorator/)


***

## Help:

- `pip install smarttextdecorator`

```python
from smarttextdecorator.tools import SmartPrinter
smart_printer = SmartPrinter()
SmartPrinter.print_framed(char='-')
smart_printer.print_center(text='Smart Legion Lab')
```

### Exemple:

```python
from smarttextdecorator.tools import SmartPrinter


def main():
    smart_printer = SmartPrinter()
    smart_printer.show_head(text='Smart Legion Lab')
    print()
    smart_printer.print_framed(text='Hello World!!!')
    print()
    smart_printer.show_footer(text='https://github.com/smartlegionlab/')


if __name__ == '__main__':
    main()

```

<img alt="image" src="data/images/smarttextdecorator.png">

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
