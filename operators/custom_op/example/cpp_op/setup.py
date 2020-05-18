from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension


# name 要和 PYBIND11_MODULE 里设的模块名保持一致
setup(name='example_op_api',
      version='0.l',
      ext_modules=[CppExtension('example_op_api', sources=['example_op.cpp'], extra_compile_args=['-std=c++11'])],
      cmdclass={'build_ext':BuildExtension})