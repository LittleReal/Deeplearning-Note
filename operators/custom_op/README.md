# 添加自定义op

对于如何添加自定义 op，官网也给出了相应的文档 [Extending PyTorch](https://pytorch.org/docs/stable/notes/extending.html#extending-torch-autograd)。

example 中提供了一个添加自定义 [op(z=3x-y)](http://www.shijinglei.com/2019/12/21/pytorch-%E6%B7%BB%E5%8A%A0c%E5%AE%9E%E7%8E%B0%E7%9A%84%E8%87%AA%E5%AE%9A%E4%B9%89op/) 的例子。要想使用 example_op，需要对源码进行安装，运行python setup.py install，如果没有问题的话，就生成了所需的python模块。可以从输出的信息看到该模块在所在python环境下的site-packages文件夹下，以.egg结尾。另外，在当前目录下会有3个文件夹生成，build、dist、example_op_api.egg-info，其中dist下也有.egg文件，可以发布到其它python环境。需要注意的是，在用该自定义 op 之前需要先 import torch。另外，example_module 对 example_op 进行了进一步标准化封装，这样就可以向调用其它标准 op 一样调用自定义的 op。我们还可以参考 [custom_op](https://github.com/huangtinglin/PyTorch-extension-Convolution)，该代码库 pytorch 对卷积算子进行了自定义封装。