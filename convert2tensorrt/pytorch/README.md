# Pytorch Model to Tensorrt

## Pytorch 设置 GPU
`gpu_index = 0`  
1. `device=torch.device('cuda:%d'%gpu_index)`  
2. `device = torch.device('cuda', gpu_index)`  
3. `import os  
os.environ["CUDA_VISIBLE_DEVICES"]='%d'%gpu_index`  
*torch.cuda.current_device() 返回的是从当前设置的 gpu 从 0 开始编号的 current_device* 

## Pytorch 存储和加载模型方式
### 存储和加载整个模型
`torch.save(model_object, "model.pt")`
`model_object = torch.load("model.pt")`

`torch.save(model_object.state_dict(), "params.pt")`
`model_object.load_state_dict("params.pt")`

如果只是进行推理，并且模型中包含 BatchNorm 或者 Dropout，需要 `model.eval()`。因为在训练和预测时，这两个 op forward 时的参数不同。

## By ONNX

### 模型转化为 onnx
[convert to onnx](./to_onnx.py)
代码中 input_shape 中的 **batch_size** 要和 onnx-tensorrt 中的 **max_batch_size** 保持一致。