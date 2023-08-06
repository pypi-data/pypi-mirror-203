<div align="center">

# QtPy-Frameless-Window

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![Downloads](https://static.pepy.tech/badge/qtpy-frameless-window)](https://pepy.tech/project/qtpy-frameless-window)
![GitHub](https://img.shields.io/github/license/TaoChenyue/Qtpy-Frameless-Window?style=plastic)

A cross-platform frameless window based on QtPy.

</div>

## Introduce 
A QWidget/QMainWindow/QDialog is wrapped in another QWidget to realize frameless effect. 
![structure](assets/structure.png)
Only qtpy library is required.

## Install
To install use pip:
```shell
pip install QtPy-Frameless-Window
```
Or clone the repo:
```shell
git clone https://github.com/TaoChenyue/QtPy-Frameless-Window.git
pip install -e .
```

## Demo
QtPy use PyQt5 as default Qt API, so you can run demo with PyQt5 like this.
```sh
python examples/dark_demo.py
python examples/light_demo.py
```
Or you can specify your Qt API like this.
```sh
python examples/dark_demo.py --api pyside6
python examples/light_demo.py --api pyqt6
...
```
It is realized by an easy function.
```python 
import argparse
import os
def set_qt_api(api:str="pyqt5",parse:bool=False):
    if parse:
        parser = argparse.ArgumentParser(description='Set Qt API')
        parser.add_argument('--api', type=str)
        args = parser.parse_args()
        if args.api is not None:
            api=args.api
    os.environ["QT_API"]=api
```

![light_demo](assets/light_demo.png)

![dark_demo](assets/dark_demo.png)

## Reference
1. [PyQt-Frameless-Window](https://github.com/zhiyiYo/PyQt-Frameless-Window)
2. [draw window shadow](https://blog.csdn.net/goforwardtostep/article/details/99549750)
