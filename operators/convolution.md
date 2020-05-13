# Convolution

##  Conv1D
以 pytorch 为例，网络中添加conv算子的定义如下
`import torch`
`torch.nn.Conv1d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros')`
其中，各参数的含义为
`input_chnnels`、`ouput_channels`输入输出的通道数；
`kernel_size` 卷积核的大小；
`stride` 卷积核滑动步长；
`padding` padding的大小；
`dilation` 空洞卷积参数，值为1时表示普通卷积，值大于1时，表示卷积核中每个卷积元素的感受野为 `2*dilation-1`，整体卷积核的感受野为`(kernel_size +1)*dilation-1`，具体可以参考[空洞卷积](https://blog.csdn.net/hao1994121/article/details/88371685)。
`groups` 卷积分组，将输入channel分组进行卷积，可以减小参数量和计算量，同时不影响输入输出shape，参考[分组卷积](https://www.jianshu.com/p/20150e44bde8)。
`bias` 是否有bias。
`padding_mode`
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxMDI3Mzk2Nl19
-->