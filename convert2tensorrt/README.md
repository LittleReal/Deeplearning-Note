# Model Convert to Tensorrt

目前比较快捷的方法是先将模型转化为 onnx，然后通过 onnx-tensorrt 转化为 tensorrt。如果有自定义 op，需要添加对应 plugin。

## ONNX Install
clone 选定的 onnx release 的版本，添加或修改自定义的 op，目前 Tensorrt 建议的是 onnx==1.6.0
git clone https://github.com/onnx/onnx.git -b release_verssion

cd onnx
git submodule update --init --recursive
python setup.py install

## Tensorrt Inference
Go to [tensorrt inference](./tensorrt)