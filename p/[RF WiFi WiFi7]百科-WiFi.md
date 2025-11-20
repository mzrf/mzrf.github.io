# 什么是WiFi 7？

WiFi 7（Wi-Fi 7）是下一代[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")标准，对应的是IEEE 802.11将发布新的修订标准IEEE 802.11be –极高吞吐量EHT（Extremely High Throughput ）。  
Wi-Fi 7是在[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")的基础上引入了320MHz带宽、4096-QAM、Multi-RU、多链路操作等技术，使得Wi-Fi 7相较于Wi-Fi 6将提供更高的数据传输速率和更低的[时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")。Wi-Fi 7预计能够支持高达23Gbps的吞吐量，大约是Wi-Fi 6的3倍。

目录

-   [为什么要有Wi-Fi 7？](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+7.html#content1)
-   [Wi-Fi 7的发布时间](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+7.html#content2)
-   [Wi-Fi 7 vs Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+7.html#content3)
-   [Wi-Fi 7支持的新特性](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+7.html#content4)
-   [Wi-Fi 7的应用场景](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+7.html#content5)
-   [Wi-Fi 7设备](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+7.html#content6)

## 为什么要有Wi-Fi 7？

随着[WLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html "WLAN")技术的发展，家庭、企业等越来越依赖[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")，并将其作为接入网络的主要手段。近年来出现新型应用对吞吐率和[时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")要求也更高，比如4K和8K视频（传输速率可能会达到20Gbps）、VR/AR、游戏（时延要求低于5ms）、远程办公、在线视频会议和云计算等。虽然最新发布的[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")已经重点关注了高密场景下的用户体验，然而面对上述更高要求的吞吐率和时延依旧无法完全满足需求。

为此，IEEE 802.11标准组织即将发布一个新修订标准IEEE 802.11be EHT，即Wi-Fi 7。

## Wi-Fi 7的发布时间

IEEE 802.11be EHT工作组已于2019年5月成立，802.11be（Wi-Fi 7）的开发工作仍在进行中，整个协议标准将按照两个Release发布，Release1预计在2021年将发布第一版草案Draft1.0，预期在2022年底发布标准；Release2预计在2022年初启动，并且在2024年底完成标准发布。

## Wi-Fi 7 vs Wi-Fi 6

Wi-Fi 7在[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")标准的基础上，引入了许多新的技术，主要体现在：

![WiFi 7 vs WiFi 6](https://download.huawei.com/mdl/image/download?uuid=e7b4e8e139c84731a54ae7e70136ae71 "WiFi 7 vs WiFi 6")  
WiFi 7 vs WiFi 6

## Wi-Fi 7支持的新特性

Wi-Fi 7协议的目标是将[WLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html "WLAN")网络的吞吐率进一步提升，并且提供[低时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")的接入保障。为了满足这个目标，整个协议在PHY层和MAC层都做了相应的改变。相对于[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")协议，Wi-Fi 7协议带来的主要技术变革点如下：

### 支持最大320MHz带宽

2.4GHz和5GHz频段免授权频谱有限且拥挤，现有[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")在运行VR/AR等新兴应用时，不可避免地会遇到[QoS](https://info.support.huawei.com/info-finder/encyclopedia/zh/QoS.html "QoS")低的问题。为了实现最大吞吐量提升的目标，Wi-Fi 7将继续引入6GHz频段，并增加新的带宽模式，包括连续240MHz，非连续160+80MHz，连续320 MHz和非连续160+160MHz。

### 支持Multi-RU机制

在Wi-Fi 6中，每个用户只能在分配到的特定RU上发送或接收帧，大大限制了频谱资源调度的灵活性。为解决该问题，进一步提升频谱效率，Wi-Fi 7中定义了允许将多个RU分配给单用户的机制。当然，为了平衡实现的复杂度和频谱的利用率，协议中对RU的组合做了一定的限制，即：小规格RU（小于242-Tone的RU）只能与小规格RU合并，大规格RU（大于等于242-Tone的RU）只能与大规格RU合并，不允许小规格RU和大规格RU混合使用。

### 引入更高阶的4096-QAM调制技术

Wi-Fi 6的最高调制方式是1024-QAM，其中调制符号承载10bits。为了进一步提升速率，Wi-Fi 7将会引入4096-QAM，使得调制符号承载12bit。在相同的编码下，Wi-Fi 7的4096-QAM比Wi-Fi 6的1024-QAM可以获得20%的速率提升。

### 引入Multi-Link多链路机制

为了实现所有可用频谱资源的高效利用，迫切需要在2.4 GHz、5 GHz和6 GHz上建立新的频谱管理、协调和传输机制。工作组定义了多[链路聚合](https://info.support.huawei.com/info-finder/encyclopedia/zh/LACP.html "LACP")相关的技术，主要包括增强型多链路聚合的MAC架构、多链路信道接入和多链路传输等相关技术。

## Wi-Fi 7的应用场景

Wi-Fi 7引入的新功能将大大提升数据传输速率并提供更低的[时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")，而这些优势将更有助于新兴的应用，如下：

-   视频流
-   视频/语音会议
-   无线游戏
-   实时协作
-   云/[边缘计算](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%BE%B9%E7%BC%98%E8%AE%A1%E7%AE%97.html "边缘计算")
-   [工业物联网](https://info.support.huawei.com/info-finder/encyclopedia/zh/IIoT.html "IIoT")
-   沉浸式AR/VR
-   互动远程医疗

## Wi-Fi 7设备

华为推出的全场景Wi-Fi 7  [AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")产品，在[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")  AP的基础上做了全面升级，具备如下4大优势：

-   带宽升级：秒级下载、秒级阅片，性能2倍于Wi-Fi 6。
-   体验升级：VIP体验“0”受损，关键应用“0”卡顿。
-   并发升级：30路4K课堂不眩晕，并发2倍于Wi-Fi 6。
-   安全升级：独家[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")  [密盾](https://info.support.huawei.com/info-finder/encyclopedia/zh/Wi-Fi%E5%AF%86%E7%9B%BE.html "Wi-Fi密盾")，盾随人动，信道绝缘防偷听。

更多Wi-Fi 7 AP产品信息请参考[华为Wi-Fi 7 AP产品](https://e.huawei.com/cn/topic/enterprise-network/wifi7)。

![华为Wi-Fi 7 AP产品示意图](https://download.huawei.com/mdl/image/download?uuid=8a196098af684231a35a865ed57a20bb "华为Wi-Fi 7 AP产品示意图")  
华为Wi-Fi 7 AP产品示意图

参考资源

1[阅读eBook：Wi-Fi 7](https://support.huawei.com/enterprise/zh/doc/EDOC1100325165)

2[阅读eBook：Wi-Fi 6](https://support.huawei.com/enterprise/zh/doc/EDOC1100195173)

3[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+7.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MDcxNjUxMDZdfQ==
-->