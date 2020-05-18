#include <torch/extension.h> //这一句是无论要实现任何op都必须添加的
#include <vector>

//forward
torch::Tensor example_op_forward(const torch::Tensor& x, const torch::Tensor& y);

//backward
std::vector<torch::Tensor> example_op_backward(const torch::Tensor& gradOutput);