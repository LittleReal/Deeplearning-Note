# 虚拟环境创建

虚拟环境创建有两种方式 virtualenv 和 virtualenvwrapper

## virtualenv

安装 virtualenv
`pip install virtualenv`
或者换用国内源安装
`pip install -i https://pypi.douban.com/simple virtualenv`

如下命令表示在当前目录下创建一个名叫 env 的目录（虚拟环境），该目录下包含了独立的 Python 运行程序,以及 pip副本用于安装其他的 packge
`virtualenv env`

创建虚拟环境时也可以选择 python 解释器，如
`virtualenv -p /usr/local/bin/python3 venv`

默认情况下，虚拟环境会依赖系统环境中的 site packages，就是说系统中已经安装好的第三方 package 也会安装在虚拟环境中，如果不想依赖这些 package，那么可以加上参数 --no-site-packages 建立虚拟环境
`virtualenv --no-site-packages`

启动虚拟环境
`source env/bin/activate`

退出虚拟环境
`deactivate`

删除虚拟环境，直接将相应虚拟环境文件夹删掉即可
`rm env -rf`

## virtualenvwrapper

在非虚拟机环境下安装virtualenvwrapper
`pip install virtualenvwrapper`

创建虚拟机
`mkvirtualenv env`
或
`mkvirtualenv env -p C:\python27\python.exe`
创建完虚拟机之后会自动进入相应的虚拟环境中

列出虚拟环境列表
`workon` 或者 `lsvirtualenv`

切换虚拟环境
`workon [虚拟环境名称]`

删除虚拟环境
`rmvirtualenv [虚拟环境名称]`

离开虚拟环境
`deactivate`
