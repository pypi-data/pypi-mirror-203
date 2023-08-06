# fonticon-materialdesignicons6

[![License](https://img.shields.io/pypi/l/fonticon-materialdesignicons6.svg?color=green)](https://github.com/pyapp-kit/fonticon-materialdesignicons6/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/fonticon-materialdesignicons6.svg?color=green)](https://pypi.org/project/fonticon-materialdesignicons6)
[![Python Version](https://img.shields.io/pypi/pyversions/fonticon-materialdesignicons6.svg?color=green)](https://python.org)

[Material Design Icons](https://github.com/Templarian/MaterialDesign-Webfont) extension for [superqt font icons](https://pyapp-kit.github.io/superqt/utilities/fonticon/)

<https://github.com/templarian/MaterialDesign>

```sh
pip install superqt fonticon-materialdesignicons6
```

```python
from fonticon_mdi6 import MDI6
from qtpy.QtCore import QSize
from qtpy.QtWidgets import QApplication, QPushButton
from superqt.fonticon import icon, pulse

app = QApplication([])

btn2 = QPushButton()
btn2.setIcon(icon(MDI6.fan, animation=pulse(btn2)))
btn2.setIconSize(QSize(225, 225))
btn2.show()

app.exec_()
```

### Dev note

To update this package for new fonticon releases, update the `VERSION = ...` string
in `scripts/bundle.py`, and rerun `python scripts/bundle.py`.
