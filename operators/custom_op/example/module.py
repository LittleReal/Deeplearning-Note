import torch
from torch.autograd import Function
from torch.nn import Module
import example_op_api


class ExampleOpFunction(Function):
    @staticmethod
    def forward(ctx, x, y):
        #如果有一些信息，需要在梯度反向传播时用到，
        #可以使用ctx.save_for_backward()进行保存
        return example_op_api.forward(x, y)

    @staticmethod
    def backward(ctx, gradOutput):
        #如果在forward中保存了信息，可以使用ctx.saved_tensors取回
        grad_x, grad_y = example_op_api.backward(gradOutput)
        return grad_x, grad_y

class ExampleOpModule(Module):
    def __init__(self):
        super(ExampleOpModule, self).__init__()

    #只需要定义forward的函数就可以了
    def forward(self, input_x, input_y):
        return ExampleOpFunction.apply(input_x, input_y)