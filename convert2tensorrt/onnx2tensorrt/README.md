# Onnx Convert to Tensorrt

这个过程要借助于 [onnx-tensorrt](https://github.com/onnx/onnx-tensorrt)。onnx2trt 的编译安装依赖于 Tensorrt 的版本和安装路径，因此两者的版本要保持一致。
需要注意的是 main.cpp 中的 **max_batch_size** 设置，如果过大会导致转化过程很慢，因为转化的过程中实际进行了模型推理，建议根据实际需要修改之后再编译。另外，**max_batch_size** 要和源模型转化为 onnx 时的输入数据的 batch_size 保持一致，否则有可能没有加速效果，甚至会降速。