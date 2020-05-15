# Convolution

##  Conv1D
以 pytorch 为例，网络中添加conv算子的定义如下
`import torch`
`torch.nn.Conv1d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros')`

其中，各参数的含义为:
`input_chnnels`、`ouput_channels`输入输出的通道数；

`kernel_size` 卷积核的大小；

`stride` 卷积核滑动步长；

`padding` padding的大小；

`dilation` 空洞卷积参数，值为1时表示普通卷积，值大于1时，表示卷积核中每个卷积元素的感受野为 `2*dilation-1`，整体卷积核的感受野为`(kernel_size +1)*dilation-1`，具体可以参考[空洞卷积](https://blog.csdn.net/hao1994121/article/details/88371685)。

`groups` 卷积分组，将输入channel分组进行卷积，可以减小参数量和计算量，同时不影响输入输出shape，参考[分组卷积](https://www.jianshu.com/p/20150e44bde8)。

`bias` 是否有bias。

`padding_mode` `zeros`，`reflect`，`replicate` 或者 `circular`，一般默认`zeros`，即补0。想了解各模式下的具体操作，可以参考[Padding Layer](https://pytorch.org/docs/master/nn.html#padding-layers)

在`Conv1D`中，输入输出数据均为3维`(n,c,l)`，`n`表示`batch_size`，`c`表示通道数，`l`表示输入数据中一个序列的长度。

在pytorch中，Conv1D是看作Conv2D来处理的。前向反向传播细节参考`Conv2D`

##  Conv2D

在`Conv2D`中，输入输出数据均为4维`(n,c,h,w)`。其中`kernel`可以为`int`也可为`tuple`，为`tuple`时可以设置高宽不同的kenel，比如`kenel=(3,5)`。

##  Conv3D

在`Conv3D`中，输入输出数据均为5维`(n,c,h,w)`。同时`kernel`如果3个维度大小不一，如`(3,4,5)`，则其shape必须为`(3,)`。


假设损失函数 $E=\sum_{i=1}^d\frac{1}{2}(y_i-y_i')^2$，训练 `DNN` 的目的时使 $E$ 最小，反向传播时使用基于梯度下降的 `BP` 来优化。$\delta$
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk3NjYxNTgzNywxNDgxOTMwMjYzLC0xNz
U4MDA1ODUwLC0xNzAxNzc0MDQ1LDEwMTAyNzM5NjZdfQ==
-->