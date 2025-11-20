# 什么是网关？

[网关](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")是从一个网络连接到另一个网络的“关口”，是网络设备用于与本地网络之外的其他网络进行通信的关键关卡，当用户访问一个不在本地网络中的资源时，用户的设备会将数据包发给网关，由网关处理数据解析、转换和转发工作。简而言之，网关是连接本地网络和外部网络的重要桥梁，确保不同网络间的数据信息可以准确传输，从而实现两个网络之间顺利通信。

目录

-   [为什么需要网关？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E7%BD%91%E5%85%B3.html#content1)
-   [网关是如何工作的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E7%BD%91%E5%85%B3.html#content2)
-   [网关和路由器的区别？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E7%BD%91%E5%85%B3.html#content3)
-   [网关的应用场景有哪些？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E7%BD%91%E5%85%B3.html#content4)

## 为什么需要网关？

[网关](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")在不同网络之间的连接和数据交换中起到了至关重要的作用，是本地网络与外部网络之间通信的桥梁，实现不同网络之间的数据转换，使得网络间能够互相通信。网关是网络互通中不可缺少的网络节点，它的主要功能有：

-   实现网络互联互通：网关既可以用于[广域网](https://info.support.huawei.com/info-finder/encyclopedia/zh/WAN.html "WAN")互连，也可以用于[局域网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B1%80%E5%9F%9F%E7%BD%91.html "局域网")互连。不同网络使用不同的协议和通信方式，无法实现直接通信，通过网关，可以实现数据的转换，将不同网络连接起来。

-   提供安全性：网关通过设置访问控制和[安全策略](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%AE%89%E5%85%A8%E7%AD%96%E7%95%A5.html "安全策略")，可以限制非法报文攻击，保护数据的安全，从而提高网络安全性。

-   实现网络管理：网关可以将不同网络的数据进行整合和处理，从而对连接的设备进行管理，具有检测设备的运行状态、配置管理和故障诊断等功能。

## 网关是如何工作的？

如下图所示，[网关](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")部署在网络边缘侧，并管理该网络内部或者外部的所有数据。当一个网络需要和另一个网络通信时，数据包被传输到网关，然后再通过最优的[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")路径传递到目的网络。以物流网络类比，网关就如同小区的快递驿站，如果要寄一个包裹，只需要把要寄的目的地址告诉快递驿站，无需关心它是如何运输的，中间需要经过多少次物流中转。

![网关工作原理图](https://download.huawei.com/mdl/image/download?uuid=b4b990d576d04e128fcb9b7a473b83d0 "网关工作原理图")  
网关工作原理图

具体来讲，网关主要通过以下步骤实现一次数据传输：

-   接收源数据：网关接收来自于源网络PC的请求报文。
-   发送源数据：网关对接收到PC的请求报文转换成目的网络可以解析的数据格式，并发送给目的网络。
-   接收目的数据：网关接收来自于目的网络的响应报文。
-   发送目的数据：网关对接收到的响应报文转换成源网络PC可以解析的数据格式，并发送给源网络。

总的来说，网关的工作原理就是接收、解析、转换和转发数据，使得不同网络中的设备可以相互通信和交换数据，从而实现不同网络之间的通信。

## 网关和路由器的区别？

[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")主要用于数据包的转发，而[网关](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")则用于不同网络之间的协议转换和连接。从以下三点了解两者的不同：

1.  网络传输位置
    -   网关：通常工作在应用层（第七层），通常位于网络的边缘，能够连接不同协议的网络，处理协议转换、数据格式转换等。
    -   路由器：通常工作在网络层（第三层），通常位于网络内部，确定设备所在的网络位置，以包为单位进行数据的发送。
2.  功能应用
    -   网关：通常能够连接使用不同协议的网络，它可以在不同的网络之间进行数据转换，例如将[局域网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B1%80%E5%9F%9F%E7%BD%91.html "局域网")和互联网连接起来。
    -   路由器：主要用于数据包的转发，路由器能够根据目标[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")转发数据包，并且能够选择最优路径来传输数据包。
3.  部署范围
    -   网关：一个网络通常只有一个网关，用于连接本地网络与外部网络之间的通信。
    -   路由器：一个网络可以有多个路由器，用于实现网络内部的数据传输和[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")转发。

## 网关的应用场景有哪些？

[网关](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")是一种网络设备，通常部署在网络的边界，它在不同网络之间进行连接和数据转发，在许多应用场景中起到关键作用。当前AR[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")也有一些典型应用场景：

1.  **互联网接入网关**：如下图所示，RouterA、RouterB和RouterC分别作为企业内部网络的出口网关，支持无线（3G/LTE/5G）和有线方式（GE/FE）接入Internet，为企业提供高性价比、高可靠的网络互联方案。
    
    针对企业不同的网络需求，AR路由器支持配置以下功能：
    
    -   企业分支机构支持通过GE/FE链路等有线方式接入Internet，也支持通过3G/LTE/5G等无线方式接入Internet。通过有线接入时，AR路由器支持通过配置静态[IP](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")、作为[DHCP](https://info.support.huawei.com/info-finder/encyclopedia/zh/DHCP.html "DHCP")  Client通过DHCP方式获取IP或作为[PPPoE](https://info.support.huawei.com/info-finder/encyclopedia/zh/PPPoE.html "PPPoE")  Client通过PPPoE拨号等方式上网。
    -   由于企业分支机构外网地址资源有限，AR路由器支持配置网络地址转换[NAT](https://info.support.huawei.com/info-finder/encyclopedia/zh/NAT.html "NAT")（[Network Address Translation](https://info.support.huawei.com/info-finder/encyclopedia/zh/NAT.html "NAT")）功能实现内网用户（使用私有[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")）访问外部资源。
    -   为了企业用户能过通过域名访问网络资源，AR路由器支持作为[DNS](https://info.support.huawei.com/info-finder/encyclopedia/zh/DNS.html "DNS")客户端，使用DNS协议从DNS Server动态获得域名对应的IP地址，使得企业内网有用户可以通过域名访问网络服务器资源。
    
    ![AR路由器作为企业出口网关访问Internet](https://download.huawei.com/mdl/image/download?uuid=a48a20401e5a4d51b31b1d228b3c2a40 "AR路由器作为企业出口网关访问Internet")  
    AR路由器作为企业出口网关访问Internet
    
2.  **物联网关**：物联网网关（IoT Gateway）在智能家居、智慧城市、工业领域，充当连接物联网设备、云网络的管道，让具有独立功能的普通物体实现互联互通。主要通过[边缘计算](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%BE%B9%E7%BC%98%E8%AE%A1%E7%AE%97.html "边缘计算")网关支持的各种物联接口（IP 化 PLC/RF/RS485/RS232 等）连接各种传感器和终端，实现终端设备接入。
    
    如下图所示，物联场景由平台及应用层、网络层和感知层三部分组成：
    
    -   平台及应用层：包括行业 IoT 平台及 控制器。行业 IoT 平台根据接收到的物联网数据进行分析计算、策略生成与结果呈现。控制器完成对海量终端、网络、数据的统一管理，使能上层行业IoT 应用。
    -   网络层：主要功能包括网络连接建立与维护、数据收集和前端处理，按需进行本地分析和决策，并将筛选后的数据按需回传云端。
    -   感知层：物联接入层，负责接入海量的各类传感器和智能终端。
    
    ![AR路由器作为边缘计算网关应用在物联场景](https://download.huawei.com/mdl/image/download?uuid=742f6a2c4b1f499cbe040b7ca34bec53 "AR路由器作为边缘计算网关应用在物联场景")  
    AR路由器作为边缘计算网关应用在物联场景
    

参考资源

1[NetEngine AR5700, AR6700, AR8000 产品文档](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100409126&tocURL=resources/hedex-homepage.html)

2[SD-WAN解决方案](https://support.huawei.com/enterprise/zh/doc/EDOC1100212003)

3[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E7%BD%91%E5%85%B3.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTA1MjQ3NzAwXX0=
-->