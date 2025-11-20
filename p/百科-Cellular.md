# 什么是Cellular？

Cellular网络，又称为蜂窝网络，是一种无线通信技术。它将整个地理区域划分为很多个小区域，每个小区域中有一个基站用于提供该区域内移动设备的无线网络信号，这种基于一个个小区域的无线通信网络被称为Cellular网络。Cellular网络在全球范围内广泛使用，使得人们可以在任何时间任何地点进行通信，不受地理位置的限制。目前，全球最流行的Cellular网络有3G、4G和5G网络。  
对于支持Cellular功能的华为[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")等网络设备，在设备上插入SIM卡即可实现该设备通过无线的方式接入运营商网络，就像手机可以随时随地无线接入3G/4G/5G网络，使用户网络部署更灵活。

目录

-   [Cellular和WiFi的区别是什么？](https://info.support.huawei.com/info-finder/encyclopedia/zh/Cellular.html#content1)
-   [Cellular有哪些应用？](https://info.support.huawei.com/info-finder/encyclopedia/zh/Cellular.html#content2)
-   [Cellular是如何工作的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/Cellular.html#content3)

## Cellular和WiFi的区别是什么？

Cellular和[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")均为无线通信技术，能够在无需物理连接的情况下传输数据和信息。Cellular依赖于基站来发射和接收无线电波，而Wi-Fi则通过AP/WAC等[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")交换设备进行信号传输。两者虽然都利用无线电波进行数据传输，但使用的频段有所不同。蜂窝网络主要使用较低的频段，例如800MHz至2.7GHz，适合广域覆盖和移动通信。Wi-Fi则主要使用较高的频段，如2.4GHz、5GHz和6GHz，适合高速数据传输及室内使用。更多关于Cellular和Wi-Fi的区别可参见下面表格。

表1-1  Cellular和Wi-Fi的区别

项目

Cellular网络

Wi-Fi网络

覆盖范围

由运营商的基站覆盖，适用于广泛区域，适合移动和广域覆盖，如户外活动。

覆盖范围有限，适合固定场所，如家庭和办公室，提供稳定连接。

传输速度

速度受信号质量和用户数量影响。

通常更快，特别是采用[Wi-Fi 7](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+7.html "WiFi 7")时。

信号稳定性

可能受地形和基站负载影响。

在固定范围内通常更稳定，除非受到干扰。

## Cellular有哪些应用？

在连接分布在不同地点的网络时，通常会使用有线网络，通过物理链路将不同地点的设备连接起来。但在某些情况下，因为物理链路的架设成本和难度，人们希望采用无线的方式进行接入。例如：

-   当部分网络设备部署在地理位置特殊的地方（如企业的偏远分支机构或海上油田）时，有线接入的成本过高。
-   在网络需要临时架设且频繁变更的场景下，比如在灾区现场需要进行快速建立网络，有线接入不仅成本高，而且移动性较差。
-   对于一些分布广泛的业务，如加油站或ATM机，站点过于分散，有线接入难以全面覆盖。

在这些场景下，网络设备可以通过无线接入Cellular网络的方式开展业务，提供所需的网络服务。

如下图所示，为了实现企业分支与总部间便捷、快速的的通信，免于布设有线网络，企业分支出口[网关](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")可以接入BSS（Base Station Subsystem，基站子系统），用无线广域接入代替有线广域接入，实现分支与总部间的网络互通。Cellular网络由三个部分构成：

-   用户设备：指用户接入Cellular网络的设备，如出口网关。
-   BSS：负责与用户设备进行无线通信，例如运营商的固定基站、移动基站等。可以将BSS看作无线网络与有线网络之间的转换器。
-   承载网与核心网：承载网负责承载与汇聚数据，核心网负责数据处理与[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")。

![Cellular网络基础架构](https://download.huawei.com/mdl/image/download?uuid=3c27559e21fc49d0ae54b4fc5f05b1bd "Cellular网络基础架构")  
Cellular网络基础架构

## Cellular是如何工作的？

[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")等设备通过Cellular款型或Cellular单板、SIM卡实现Cellular功能。

将SIM卡插入Cellular款型或Cellular单板上的SIM卡槽中，并将Cellular单板插入路由器后，路由器设备即可通过拨号连接的方式与运营商网络进行连接。在开启拨号功能后，设备无需数据报文触发，会自动尝试与运营商网络建立拨号连接。若拨号失败，设备将每隔一段时间自动重试与运营商网络的拨号连接。拨号连接过程如下图所示。

![拨号连接过程](https://download.huawei.com/mdl/image/download?uuid=3c0a62261b3a42c3b54da1c3dae425db "拨号连接过程")  
拨号连接过程

详细过程如下：

1.  Cellular通道接口向Cellular模组发送连接建立请求。
2.  Cellular模组向运营商网络发送连接建立请求，该请求中包含用户的身份认证信息。
3.  运营商网络对接入的用户进行认证，认证成功后，核心网与Cellular模组建立连接，并分配[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")给Cellular模组。
4.  Cellular模组通知Cellular通道接口物理Up。
5.  Cellular通道接口与Cellular模组进行IP地址协商，并获取Cellular模组为通道接口分配的IP地址。
6.  Cellular通道接口成功与运营商网络建立链路，进行数据业务转发。

参考资源

1[了解如何配置Cellular（NetEngine AR路由器）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100458332&id=ZH-CN_CONCEPT_0000001771231365)

2[了解如何配置Cellular（HiSecEngine USG系列防火墙）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100435565&id=ZH-CN_CONCEPT_0000001771231365)

3[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/Cellular.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgyNDk5NzgyNF19
-->