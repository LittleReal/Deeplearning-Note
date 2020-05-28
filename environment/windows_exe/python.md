# Python Generate exe

## py2exe

创建一个 `setup.py` 文件，包含如下内容，其中 `your.py` 为要生成可执行文件的 `python` 文件。但是这个有局限性，只能用于 python==3.4 下。
`from distutils.core import setup`
`import py2exe`
`setup(console=['your.py'])`

## pyinstaller

`pip install pyinstaller`
`pyinstaller --onefile --console your.py`

在当前目录下的 dist 文件夹下就可以看到 your.exe 的可执行文件。

