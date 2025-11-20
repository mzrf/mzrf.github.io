# 什么是QAM？

正交幅度调制QAM（Quadrature Amplitude Modulation）是[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")中一种常用的数字信号调制，是相位调制和幅度调制的组合。

目录

-   [为什么要有QAM？](https://info.support.huawei.com/info-finder/encyclopedia/zh/QAM.html#content1)
-   [QAM是如何工作的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/QAM.html#content2)
-   [QAM的星座图](https://info.support.huawei.com/info-finder/encyclopedia/zh/QAM.html#content3)
-   [噪声与干扰对QAM的影响](https://info.support.huawei.com/info-finder/encyclopedia/zh/QAM.html#content4)
-   [QAM如何与Wi-Fi配合使用？](https://info.support.huawei.com/info-finder/encyclopedia/zh/QAM.html#content5)

## 为什么要有QAM？

QAM在用于[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")数字信号调制时，与普通幅度调制和相位调制相比能得到更高的速率。因为幅度调制和相位调制仅有2种符号（symbol）来区分0或1。

-   幅度调制：通过改变载波的振幅来区分0和1。
-   相位调制：通过改变载波的相位来区分0和1。例如我们常见的BPSK，就是使用0°和180°共2个相位表示0和1，即2种符号；QPSK则是使用0°、90°、180°和270°共4个相位，能够表示00、01、10和11共4种符号，传递2 bit的信息。其实QPSK就是一种特殊的QAM，即4-QAM。

而QAM则有更多的符号，每个符号都有相应的相位和幅度值。

以16-QAM为例，通过QAM调制可得到16个不同的波形，分别代表0000，0001....这也意味着一共有16种符号，一个符号可以传递4 bit信息。

![16-QAM示意图](https://download.huawei.com/mdl/image/download?uuid=f5195be143254caf8f4bf836b216e0fb "16-QAM示意图")  
16-QAM示意图

## QAM是如何工作的？

QAM是将信号加载到2个正交的载波上（通常是正弦和余弦），通过对这两个载波幅度调整并叠加，最终得到相位和幅度都调制过的信号。这两个载波通常被称为I信号，另一个被称为Q信号，所以这种调制方式也被称为IQ调制。

![IQ调制](https://download.huawei.com/mdl/image/download?uuid=e5e75c194a024a88b76bb3f6de81e1ac "IQ调制")  
IQ调制

由于QAM最终调制后的信号包含了相位和幅度的变换，因此QAM也被认为相位调制和幅度调制的组合。

## QAM的星座图

在数字信号调制中，星座图通常用于表示QAM调制二维图形。星座图相对于IQ调制而言，将数据调制信息映射到极坐标中，这些信息包含了信号的幅度信息和相位信息。

星座图上的每一个点，都表示一个符号。该点I轴和Q轴的分量分别代表着正交的载波上的幅度调整。该点到原点的距离**A**就是调制后的幅度，夹角**φ**就是调制后的相位。

![QAM的星座图](https://download.huawei.com/mdl/image/download?uuid=4014c806206846f29ec8ab6cb228e782 "QAM的星座图")  
QAM的星座图

而星座图上点的数量，决定了每个符号传输的比特数。例如：

-   256-QAM，256是2的8次方，每个符号能传输8bit的数据。
-   1024-QAM，1024是2的10次方，每个符号能传输10bit的数据。

因此，作为比256-QAM更高阶的1024-QAM，数据传输的峰值速率进一步提高25%。

![WiFi 6 1024-QAM](https://download.huawei.com/mdl/image/download?uuid=ebe968055dd8415da9d58caaaa0df0eb "WiFi 6 1024-QAM")  
WiFi 6 1024-QAM

## 噪声与干扰对QAM的影响

尽管较高阶的调制速率能够为无线电通信系统提供更快的数据速率和更高水平的频谱效率，但这是有代价的。较高阶的调制方案对噪声和干扰的适应性要差得多。

因为发送一个符号所用的载波频宽是固定的，发送时长也是一定的，较高阶意味着两个符号之间差异就越小。这不仅对接收双方的器件要求很高，而且对环境的要求也很高。也就是说，如果环境过于恶劣，终端将无法使用高阶的QAM模式通信，只能使用较低阶次的调制模式。

## QAM如何与Wi-Fi配合使用？

### 不同Wi-Fi标准使用的QAM

在[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")标准中，为了提升速率，各版本协议使用的QAM阶数也在逐步提升。

![不同WiFi标准采用的QAM](https://download.huawei.com/mdl/image/download?uuid=39b0f751955c4c66a093eabbfde7eaae "不同WiFi标准采用的QAM")  
不同WiFi标准采用的QAM

### QAM对Wi-Fi标准速率影响

在Wi-Fi标准中，定义了调制和编码方案MCS（Modulation and Coding Scheme）。MCS对应一组调制和编码方式。以[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")为例，MCS索引有12个。

![Wi-Fi 6中MCS索引对应的调制方式以及编码率](https://download.huawei.com/mdl/image/download?uuid=db3923f2bb764bbdaa6ca1d6d67ef20e "Wi-Fi 6中MCS索引对应的调制方式以及编码率")  
Wi-Fi 6中MCS索引对应的调制方式以及编码率

如果MCS为1，则使用的是QPSK的调制方式；如果MCS为11，则使用的是1024的调制方式。

对于每个MCS的索引值，根据信道带宽、空间流数和保护间隔（Guard Interval，GI）可以计算出不同的速率。

计算公式如下：

![Wi-Fi标准的速率计算公式](https://download.huawei.com/mdl/image/download?uuid=c7ffbd462d664e5b9a175d8c705019ad "Wi-Fi标准的速率计算公式")  
Wi-Fi标准的速率计算公式

由此可见，提升调制方式，可以明显提升速率。

参考资源

1[阅读eBook：Wi-Fi 6](https://support.huawei.com/enterprise/zh/doc/EDOC1100195173)

2[华为Wi-Fi 6(802.11ax)技术白皮书](https://e.huawei.com/cn/material/networking/wlan/b3f46485597c4d72b43a6a27c6480646)

3[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/QAM.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MjM0NTk0NTFdfQ==
-->