#include "./example_op.h"

torch::Tensor example_op_forward(const torch::Tensor& x, const torch::Tensor& y) {     
     AT_ASSERTM(x.sizes() == y.sizes(), "x must be the same size as y");
     torch::Tensor z = torch::zeros(x.sizes());
     z = 3 * x - y;
     return z; 
}

std::vector<torch::Tensor> example_op_backward(const torch::Tensor& gradOutput) {
     torch::Tensor gradOutputX = 3 * gradOutput * torch::ones(gradOutput.sizes());
     torch::Tensor gradOutputY = -1 * gradOutput * torch::ones(gradOutput.sizes());
     return {gradOutputX, gradOutputY}; 
} 

// pybind11 绑定 
// PYBIND11_MODULE是用来将C++函数绑定到python上的。
// 其中第一个参数my_op_api为要生成的python模块名，
// 以后import my_op_api就可以调用该op了。第二个参数固定为m
// 函数体中的两个语句分别是绑定前向传播与反向传播到实现的两个函数上。
PYBIND11_MODULE(example_op_api, m) {
     m.def("forward", &example_op_forward, "example_op forward");
     m.def("backward", &example_op_backward, "example_op backward"); 
}