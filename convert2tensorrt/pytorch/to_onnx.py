import torch

# input_shape = (1, 3, 224, 224) for example
dummy_input = torch.randn(1, 3, 224, 224, device='cuda')

# load model
# torch default alexnet, the "alexnet.pt" is generated by defualt one.
# model = torchvision.models.alexnet(pretrained=True).cuda()
model = torch.load("alexnet.pt")

# inference mode
model.eval()

# 为模型的输入输出重新命名，也可以不做此操作
input_names = ["input0"]
output_names = ["output0"]

torch.onnx.export(
    model = model, 
    args = dummy_input, 
    "alexnet.onnx", 
    verbose=True, 
    input_names=input_names, 
    output_names=output_names)