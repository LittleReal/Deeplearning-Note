# LSTM

## RNN
RNN (Recurrent Neural Network，循环神经网络) 的简图如下，
![RNN结构](./rnn.png)
RNN其中一个单元的细节如下图，
![RNN-Single](./rnn-single.jpg)
为当前状态下数据的输入，  ![[公式]](https://www.zhihu.com/equation?tex=h)  表示接收到的上一个节点的输入。

![[公式]](https://www.zhihu.com/equation?tex=y)  为当前节点状态下的输出，而  ![[公式]](https://www.zhihu.com/equation?tex=h%27)  为传递到下一个节点的输出。

  

通过上图的公式可以看到，输出  **h'**  与  **x**  和  **h**  的值都相关。

而  **y**  则常常使用  **h'** 投入到一个线性层（主要是进行维度映射）然后使用softmax进行分类得到需要的数据。

对这里的**y**如何通过 **h'** 计算得到往往看具体模型的使用方式。

  

通过序列形式的输入，我们能够得到如下形式的RNN。

主要优势是可以处理序列化数据，比如某个单词的意思会因为上文提到的
内容不同而有不同的含义。在过去几年中，应用 RNN 在语音识别，语言建模，翻译，图片描述等问题上已经取得一定成功，并且这个趋势还在增长。


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY5NTIzNTc3NCwzOTk2OTM3ODgsLTM0MD
U4NDUyOCwtMTg0ODI3ODUyNiwxOTYzOTQ5NTI0LDExMjgwMDg5
MTYsLTg2OTUyODk3MV19
-->