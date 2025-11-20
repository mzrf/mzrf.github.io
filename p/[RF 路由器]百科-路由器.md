# 什么是路由器？

路由器是用来连接两个或多个网络的硬件设备，工作在网络层，在网络间起到网关的作用。路由器可以通过查询[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")表为接收到的报文寻找一条最佳的传输路径，然后从对应的接口转发出去，最终将报文送达到对应的目的地址。

目录

-   [为什么需要路由器？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html#content1)
-   [路由器是怎么工作的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html#content2)
-   [路由器分类有哪些？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html#content3)

## 为什么需要路由器？

路由器是网络中必不可少的网络设备之一，路由器的主要功能有：

-   实现网络互联互通：路由器支持多种互联接口及协议，可实现[局域网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B1%80%E5%9F%9F%E7%BD%91.html "局域网")与[广域网](https://info.support.huawei.com/info-finder/encyclopedia/zh/WAN.html "WAN")的互联，实现不同网络间的通信。

-   实现数据高性能转发：路由器可以为经过路由器的报文寻找一条最佳的传输通道，从而提高通信速率，节省网络资源。

-   实现网络管理：路由器提供包括配置管理、性能管理、容错管理和流量控制等功能。

## 路由器是怎么工作的？

如下图所示，路由器最主要的功能转发数据包，就如同快递公司来发送包裹，包裹并不是瞬间到达最终目的地，而是通过不同分站的分拣，不断地接近最终地址，从而实现包裹的投递。由于路由器处在不同网络之间，但并不一定是数据包的最终接收者。所以在路由器中，通常存在着一张[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")表。路由器根据数据包携带的目的地址信息寻找下一个转发地址，应该是哪个网络，我们把这个过程称之为寻址过程。了解寻址过程前我们需要了解下路由表和路由协议。

![路由器工作的网络结构图](https://download.huawei.com/mdl/image/download?uuid=6b23e5e45ade472580ca183d9079b351 "路由器工作的网络结构图")  
路由器工作的网络结构图

### 路由表

路由表（Routing table）是存储在路由器中的数据表，就如一张地图，其中存储了指向特定目的网络地址的路径信息。路由表中有许多条目，每个条目可以被称为一条路由，每条路由都对应一个网络中的目的地。示意图如下。

![](https://download.huawei.com/mdl/image/download?uuid=b0fbfe8508db496098702375c0557a2d "点击放大")

当路由设备收到一个[IP](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")数据包时，会先查看数据包包头的目的地址，并在自己的路由表中进行查找。如果查找结果中有匹配的表项，那么便依据此表项所指示的出接口和下一跳进行转发；如果没有匹配的表项，就去检查是否存在默认路由；如果默认路由也不存在，这个IP数据包会被丢弃，同时路由设备会向数据包的源端设备发送[ICMP](https://info.support.huawei.com/info-finder/encyclopedia/zh/ICMP.html)（Internet Control Message Protocol，因特网控制消息协议）报错消息，报告该目的地址或网络不可达。

每台路由器中都保存着一张**本地核心路由表**，用来保存各种路由协议发现的路由并决策优选路由。路由条目的来源主要有：

-   直连路由（Direct Route）：路由器本地接口所在的网段，由路由器自行发现并写入路由表中；
-   静态路由（Static Route）：网络管理员手工配置的路由；
-   动态路由（Dynamic Route）：路由器通过动态路由协议发现的路由。动态路由协议包括[BGP](https://info.support.huawei.com/info-finder/encyclopedia/zh/BGP.html "BGP")（Border Gateway Protocol，边界网关协议）、[IS-IS](https://info.support.huawei.com/info-finder/encyclopedia/zh/IS-IS.html "IS-IS")（Intermediate System to Intermediate System，中间系统到中间系统）、[OSPF](https://info.support.huawei.com/info-finder/encyclopedia/zh/OSPF.html "OSPF")（Open Shortest Path First，开放式最短路径优先）、RIP（Routing Information Protocol，路由信息协议）等。

除了按来源划分，依据目的地（目的地址范围）的不同，路由可以划分为：

-   主机路由：目的地为单一主机，数据包发送至唯一目的地主机；
-   网段路由：目的地为一个网段，数据包发送至一个网络段中的所有主机。

对于NetEngine系列路由器，可以通过**display ip routing-table**命令查看路由器的路由表信息，如：

```
<HUAWEI> **display ip routing-table**
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table: Public
         Destinations : 8        Routes : 8

Destination/Mask     Proto  Pre  Cost   Flags  NextHop        Interface

       0.0.0.0/0      Static 60   0      D     10.1.4.2       GigabitEthernet1/0/0
       10.1.4.0/30    OSPF   10   0      D     10.1.4.1       GigabitEthernet1/0/0
       10.1.4.1/32    Direct 0    0      D     127.0.0.1      InLoopBack0
       10.1.4.2/32    OSPF   10   0      D     10.1.4.2       GigabitEthernet1/0/0
     127.0.0.0/8      Direct 0    0      D     127.0.0.1      InLoopBack0
     127.0.0.1/32     Direct 0    0      D     127.0.0.1      InLoopBack0
127.255.255.255/32    Direct 0    0      D     127.0.0.1      InLoopBack0
255.255.255.255/32    Direct 0    0      D     127.0.0.1      InLoopBack0
```
路由表中包含了下列关键概念：

-   Destination：目的地址。用来标识路由的目的地址或目的网络。
-   Mask：网络掩码。与目的地址一起来标识目的主机或路由器所在的网段的地址。将目的地址和网络掩码“逻辑与”后可得到目的主机或路由器所在网段的地址。例如：目的地址为1.1.1.1，掩码为255.255.255.0的主机或路由器所在网段的地址为1.1.1.0。
-   Proto：路由协议名称，代表这条路由是通过什么路由协议获取到的，如Direct代表直连路由、Static代表静态路由等。
-   Pre：本条路由加入[IP路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")表的优先级。针对同一目的地，可能存在不同下一跳/出接口等的若干条路由，这些不同的路由可能是由不同的路由协议发现的，也可以是手工配置的静态路由。优先级高（数值小）者将成为当前的最优路由。
-   Cost：路由开销。当到达同一目的地的多条路由具有相同的优先级（Pre相同）时，开销最小的将成为当前的最优路由。路由开销是用来评估路由路径优劣的一个数值，也被称为路由度量（Route Metric），它表示从源节点到目的节点所经过的路由路径的代价，代价的大小取决于网络拓扑、带宽、[延迟](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")、可靠性、安全性等多种因素。
-   Flags：路由标记。一种路由器在转发数据包时使用的标记，用于标识数据包的来源和目的地，以及路由器对数据包的处理方式等。
-   NextHop：下一跳[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")。
-   Interface：输出接口。说明IP包将从该路由器哪个接口转发。

### 路由协议

路由协议是路由设备之间维护路由表的规则，用于发现路由，生成路由表，并指导报文转发。

路由器不仅支持静态路由，也支持动态路由。动态路由协议有自己的路由算法，能够自动适应网络拓扑的变化，适用于具有一定数量三层设备的网络，具体可以划分为：

-   IGP（Interior Gateway Protocol，内部网关协议）：即在一个自治系统内部使用的路由选择协议，它与互联网中的其他自治系统选用什么路由选择协议无关，常见的IGP协议包括RIP、**[OSPF](https://info.support.huawei.com/info-finder/encyclopedia/zh/OSPF.html)**和**[IS-IS](https://info.support.huawei.com/info-finder/encyclopedia/zh/IS-IS.html)**。
-   EGP（Exterior Gateway Protocol，外部网关协议）：若源设备和目的设备处在不同自治系统中，当数据包传到一个自治系统的边界时，就需要使用一种协议将数据包传递到另一个自治系统中，这就是EGP，**[BGP](https://info.support.huawei.com/info-finder/encyclopedia/zh/BGP.html)**是目前最常用的EGP协议。

静态路由和动态路由的区别和适用场景如下：

![静态路由和动态路由区别与适用场景](https://download.huawei.com/mdl/image/download?uuid=dfa0178631ac4d6386ecc2c7197b6980 "静态路由和动态路由区别与适用场景")  
静态路由和动态路由区别与适用场景

在实际应用中，路由器可以同时配置静态路由和动态路由；在所有的路由信息中，默认情况下静态路由优先级高于动态路由。即当同时存在到达同一个目的网络的动态路由与静态路由时，最终选用静态路由作为最佳路由。

### 寻址过程

路由器收到数据包时，首先会解析其目的IP地址，接着在路由表中查找通往目的网络的最佳路径，根据查找结果进行不同处理。

例如如下图所示，PC1要转发一个报文至目的主机PC2，中间途经2个路由器，其选址过程如下：

![路由器寻址过程](https://download.huawei.com/mdl/image/download?uuid=fb60ab17b5a3413588711cd31af17ab2 "路由器寻址过程")  
路由器寻址过程

1.  PC1将报文发送至路由器RouterA，RouterA接收到数据包时，会解析报文的目的IP地址。
2.  RouterA根据目的IP地址查找路由表，根据查找结果进行不同处理。
    -   如果在路由表中找到目的IP地址，按照相应的出口将报文转发给RouterB。
    -   如果在路由表中没找到目标网络地址，就看一下有没有默认路由，如果有就按照默认路由的出接口发送给RouterB。
    -   如果在路由表中没找到目标网络地址，就看一下有没有默认路由，如果也没有就给源IP发送一个出错[ICMP](https://info.support.huawei.com/info-finder/encyclopedia/zh/ICMP.html "ICMP")数据包表明没法传递该数据包，同时丢弃该报文。
3.  RouterB接收到报文后，会和RouterA一样针对报文进行处理，最终将报文转发至目的主机PC2。

## 路由器分类有哪些？

1984年，来自斯坦福大学的教师夫妇波萨克和勒娜设计了多协议路由器的联网设备。随着技术的不断演进，各种路由器层出不穷。

-   如果按使用场景划分，路由器可分为以下几类：
    -   适用于企业内网络连接的企业路由器。
    -   适用于[运营商](https://info.support.huawei.com/info-finder/encyclopedia/zh/CSC.html)的运营商路由器
    -   适用于家庭上网的家用路由器。

-   如果从网络层次功能划分，路由器可分为以下几类：
    -   骨干路由器：数据吐量较大且重要，是运营商网络实现互连的关键。骨干路由器要求性能的高速度及高可靠性。例如华为NetEngine 5000E系列核心路由器是面向企业骨干网、城域网核心节点、[数据中心互联](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%E4%BA%92%E8%81%94.html "数据中心互联")节点和国际网关等推出的核心路由器产品，具有大容量、高可靠、绿色、智能等特点，支持单框、背靠背和多框集群模式，实现按需扩展，帮助企业用户轻松应对互联网流量快速增长和未来业务发展。
    -   城域路由器：用于运营商网络边缘，负责连接各个企业网络汇聚到运营商骨干网络。例如华为NetEngine 8000系列路由器是华为公司推出的全场景接入汇聚路由器，高紧凑大容量，整机交换能力强，同时支持丰富的接口，灵活适配不同业务。关键组件冗余备份，保障多业务承载的高可靠性。同时支持[SRv6](https://info.support.huawei.com/info-finder/encyclopedia/zh/SRv6.html "SRv6")、[FlexE](https://info.support.huawei.com/info-finder/encyclopedia/zh/FlexE.html "FlexE")、[IFIT](https://info.support.huawei.com/info-finder/encyclopedia/zh/IFIT.html "IFIT")等新技术，支撑客户网络云化平滑演进。
    -   接入路由器：连接对象为许多终端系统。网络中用于连接企业网络与运营商网络，支持多种有线及无线接口，支持多种业务能力，如[VPN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VPN.html "VPN")、安全、[QoS](https://info.support.huawei.com/info-finder/encyclopedia/zh/QoS.html "QoS")、认证等。例如华为NetEngine AR系列路由器是华为公司推出的集[SD-WAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/SD-WAN.html "SD-WAN")、[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")、交换、VPN、安全等功能于一体的新一代业务路由网关设备，包含AR5700、AR6700、AR8000等系列产品。

参考资源

1[了解华为路由器](https://e.huawei.com/cn/products/routers)

2[了解华为云广域网络解决方案](https://e.huawei.com/cn/solutions/enterprise-network/wide-area-network)

3[了解华为SD-WAN解决方案](https://e.huawei.com/cn/solutions/enterprise-network/campus-network)

4[华为路由器技术支持](https://support.huawei.com/enterprise/zh/category/routers-pid-1482607112869?submodel=doc)

5[华为云广域网络解决方案技术支持](https://info.support.huawei.com/info-finder/solution/zh/enterprise/index.html?sol=cloudwan)

6[华为SD-WAN技术支持](https://info.support.huawei.com/info-finder/solution/zh/enterprise/index.html?sol=sdwan)

7[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA4ODMyMzk5OV19
-->