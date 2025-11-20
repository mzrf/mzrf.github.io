# 什么是交换机？

交换机是一种为所连接的IT设备提供网络通信的设备。交换机按不同类型可以分为以太网交换机、三层交换机、园区交换机、数据中心交换机、核心交换机、汇聚交换机、接入交换机、无管理型交换机、Web管理型交换机、全管理型交换机、千兆交换机、多速率交换机盒式交换机和框式交换机等。

目录

-   [交换机是做什么用的](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html#content1)
-   [交换机是如何工作的](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html#content2)
-   [交换机的分类](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html#content3)
-   [交换机 VS 路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html#content4)
-   [交换机 VS 集线器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html#content5)
-   [华为有哪些交换机](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html#content6)

## 交换机是做什么用的

交换机的主要作用是转发传输数据，实现网络设备之间的通信互联。可概括为以下功能：

-   对网络进行分段和隔离，划分多个虚拟网段，提高网络的安全性。
-   识别接收到的数据，精准向目标设备转发，提高网络的性能。
-   对不同端口、用户和应用进行流量控制和管理，优化网络环境，提高网络的可靠性和稳定性。
-   优化数据传输方式，提高传输速率。

交换机除了以上基本作用之外，还具备了一些新的功能，如对[VLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VLAN.html "VLAN")（虚拟局域网）的支持、对链路汇聚的支持，甚至有的还具有[防火墙](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E9%98%B2%E7%81%AB%E5%A2%99.html "防火墙")的功能。

## 交换机是如何工作的

交换机对数据包的转发是建立在物理地址（MAC地址）基础之上的，对于[IP](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")网络协议来说，它是透明的，即交换机在转发数据包时，不知道也无须知道信源机和信宿机的[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")，只需知其目的MAC地址。

交换机在工作过程当中会不断的收集信息去建立一个MAC地址表，这个表相当简单，它说明了某个MAC地址是在哪个端口上被发现的。

当交换机收到一个TCP/IP数据包时，会先确认是否为广播数据包，如果是则将数据包广播到所有端口；如果不是则会在MAC地址表中查询目的MAC，以确认应该从哪个端口把数据包发出去（如果目的MAC地址与源MAC地址相同，会被视为无效数据包并丢弃）。

如果目的MAC地址不能在地址表中找到时，交换机会如同处理广播数据包一样，把该数据包从接收端口除外的所有端口转发出去。对应端口回应后交换机会“学习”新的MAC地址，把新的MAC地址添加到MAC地址表中。

![交换机工作过程示意图](https://download.huawei.com/mdl/image/download?uuid=513781d5081343b4acd77ce365d0a96a "交换机工作过程示意图")  
交换机工作过程示意图

## 交换机的分类

交换机从不同角度可分为多种不同类型的交换机，以下是从应用场景、网络层次和管理类型等角度对交换机进行分类。

表1-1  交换机的分类

分类依据

交换机种类

主要特点

应用场景

园区交换机

面向企业、政府、教育、金融、制造等各行业，打造极简管理、稳定可靠、业务智能的园区网络。

数据中心交换机

面向云[数据中心](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83.html "数据中心")和高端园区，适用于各种场景和网络规模，为规模化、自动化、可编程和实时可见性而打造。

网络层次

接入交换机

指工作在接入层的交换机。直接连接IT设备和网络，成本较低、端口密度较高。

汇聚交换机

指工作在汇聚层的交换机。是多台接入层交换机的汇聚点，相较于接入交换机，需要更高的性能和更高的交换速率。

核心交换机

指工作于核心层的交换机。核心层交换机对可靠性，性能和吞吐量都有较高的要求。

管理类型

无管理型交换机

既不支持Web，也不支持[SNMP](https://info.support.huawei.com/info-finder/encyclopedia/zh/SNMP.html "SNMP")管理的交换机，设备完成安装连线和上电后可[即插即用](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%8D%B3%E6%8F%92%E5%8D%B3%E7%94%A8.html "即插即用")，不涉及设备登录和开局等配置。

Web管理型交换机

通过Web可视化的界面，对交换机的各种功能进行简单可视化管理。

全管理型交换机

支持SNMP、Web管理和命令行等多样化的管理和维护方式，具备友好的人机界面。

OSI网络模型

二层交换机

工作在OSI七层模型的第二层（数据链路层），可识别数据帧中的MAC地址。二层交换机通常也称为以太网交换机。

三层交换机

工作在OSI七层模型的第三层（网络层），具有[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")功能。在校园网等大型局域网中有广泛应用，主要作用是加快内部数据交换转发。

端口速率

百兆交换机

下行端口可以提供全百兆传输速率。

千兆交换机

下行端口可以提供全千兆传输速率。

万兆交换机

下行端口可以提供全万兆传输速率。

多速率交换机

下行端口可以提供100M/1G/2.5G/5G/10G速率传输。

整机结构

盒式交换机

整机采用集中式一体化设计，具有固定数量的端口和功能配置，易于维护和管理。整机尺寸较小，适用于桌面、挂墙和机柜安装。

框式交换机

又称模块化交换机，各个功能模块相对独立，可以添加或更换单板、电源和风扇等模块均可插拔和更换，可拓展性高。整机尺寸较大，只用于机柜安装。

## 交换机 VS 路由器

[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")是一个链接两个或多个网络的设备。接收数据后，路由器会先依据[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")表找出通往目的[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")的最短路径，然后转发到下一地址。

路由器和交换机都可以在网络中传送转发数据，但是两者之间也有一定的区别。

-   交换机主要功能是用于数据交换，路由器主要功能是用于路由转发。
-   交换机根据MAC地址进行数据转发，而路由器是根据IP地址进行数据转发。
-   路由器能在多条路径中选择最佳的路径，提升交换数据的传输速率。

## 交换机 VS 集线器

集线器（Hub）是指将多条[以太网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BB%A5%E5%A4%AA%E7%BD%91.html "以太网")双绞线或光纤集合连接在同一段物理介质下的设备。Hub有多个I/O端口，信号由任一端口进入后，经过再生或放大转发至其他所有端口。

Hub无法储存数据，在接收之后必须立刻转发，所以在转发数据时需要进行冲突检测，防止产生冲突导致数据包丢弃。基于此，Hub只能以半双工模式工作。

在网络早期，Hub的诞生给人们带来了极大的便利，在交换机发明之前一度十分流行。从一定程度上来看，集线器可以说是交换机的前身，现在集线器已经很难满足人们的要求，因此大部分的集线器已经被交换机所取代。同时，交换机也在不断扩展自身的功能，衍生出很多更高级、更强大的交换机以满足不同的需求。

## 华为有哪些交换机

[华为交换机](https://e.huawei.com/cn/products/switches)按应用场景进行分类，包括华为园区交换机和华为数据中心交换机。

### 华为园区交换机

华为园区交换机致力于打造极简管理、稳定可靠、业务智能的园区网络。

华为园区交换机有三大突出特点：

-   更可靠的网络：搭载全新可编程芯片，基于信元交换技术，在高并发、高负载工作环境下，实现无阻塞交换、业务零丢包。
-   更简单的管理：接入到核心全层次[有线无线深度融合](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%9C%89%E7%BA%BF%E6%97%A0%E7%BA%BF%E6%B7%B1%E5%BA%A6%E8%9E%8D%E5%90%88.html "有线无线深度融合")，一台交换机支持高达10240台[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")融合管理，统一用户认证，简化运维。
-   更敏捷的部署：基于[SDN](https://info.support.huawei.com/info-finder/encyclopedia/zh/SDN.html "SDN")和[VxLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VXLAN.html "VXLAN")技术，整网设备[即插即用](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%8D%B3%E6%8F%92%E5%8D%B3%E7%94%A8.html "即插即用")，分钟级网络部署和调整，更敏捷地响应业务的变化。

华为园区交换机产品形态众多，针对不同场景可选用不同的交换机，详情可查看[华为园区交换机全家福](https://e.huawei.com/cn/material/networking/campusswitch/563935e525ae4787a2a80d727a39701f)。以下仅为CloudEngine S8700系列园区交换机示意图。

![CloudEngine S8700系列园区交换机示意图](https://download.huawei.com/mdl/image/download?uuid=c153c59c90284bdf8dad30abd738a9f7 "CloudEngine S8700系列园区交换机示意图")  
CloudEngine S8700系列园区交换机示意图

### 华为数据中心交换机

[数据中心](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83.html "数据中心")正在从云时代向智能时代演进，成为5G、人工智能等新型基础设施的核心。华为推出面向智能时代的CloudEngine数据中心交换机。同时，华为定义了智能时代数据中心交换机的三大特征：400GE超宽、0丢包[以太网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BB%A5%E5%A4%AA%E7%BD%91.html "以太网")、全生命周期自动管理，助力客户加速智能化转型。

华为数据中心交换机具有以下特点：

-   高可扩展性和灵活性：丰富的产品组合，支持从500到50000+服务器规模的灵活组网；基于数据采集的实时分析，满足业务快速创新和[智能运维](https://info.support.huawei.com/info-finder/encyclopedia/zh/AIOps.html "AIOps")。
-   自动化和敏捷性：采用iMaster NCE-Fabric实现Overlay和Underlay的自动化操作；可基于标准开放API与第三方DevOps工具集成实现自动化管理。
-   基于开放架构的平滑演进： 统一的开放架构，支持从传统数据中心网络向SDN和多云时代平滑演进。

如华为园区交换机一样，华为数据中心交换机也有众多产品，可查看[华为数据中心交换机全家福](https://e.huawei.com/cn/material/enterprise/37be0a1a811f451e916f09e90ff27c58)了解详情。

以下为CloudEngine XH16800系列数据中心交换机示意图，CloudEngine XH16800是华为推出的面向AI场景的数据中心核心交换机，具备高算力效率和高算力可用率两大特点。在算力效率方面，CloudEngine XH16800 系列交换机支持[NSLB](https://info.support.huawei.com/info-finder/encyclopedia/zh/NSLB.html "NSLB")（[网络级负载均衡](https://info.support.huawei.com/info-finder/encyclopedia/zh/NSLB.html "NSLB")），实现训练效率提升20%。在算力可用率方面，支持算网CCAE一体化运维等功能，排障效率提升90%。

![CloudEngine XH16800系列数据中心交换机示意图](https://download.huawei.com/mdl/image/download?uuid=75080469e045425f9ff416b4a5aba26b "CloudEngine XH16800系列数据中心交换机示意图")  
CloudEngine XH16800系列数据中心交换机示意图

参考资源

1[华为 S100, S200, S300, S500, S600 交换机](https://support.huawei.com/enterprise/zh/switches/s100-s200-s300-s500-s600-pid-259590357)

2[华为 S1700, S2700 交换机](https://support.huawei.com/enterprise/zh/switches/s1700-s2700-pid-259590359)

3[华为 S3700, S5700, S6700 交换机](https://support.huawei.com/enterprise/zh/switches/s3700-s5700-s6700-pid-259602657)

4[华为 S7700, S8700, S9700, S12700, S16700 交换机](https://support.huawei.com/enterprise/zh/switches/s7700-s8700-s9700-s12700-s16700-pid-259602655)

5[华为 CloudEngine 12800,16800 交换机](https://support.huawei.com/enterprise/zh/switches/cloudengine-12800-16800-pid-252837173)

6[华为 CloudEngine 5800, 6800, 7800, 8800, 9800 交换机](https://support.huawei.com/enterprise/zh/switches/cloudengine-58-68-78-88-98-pid-252837181)

7[华为 CloudEngine XH16800系列交换机](https://support.huawei.com/enterprise/zh/data-communication/xh16800-8-pid-261323714?offeringId=252837173)

8[华为 CloudEngine XH9000, XH8000系列交换机](https://support.huawei.com/enterprise/zh/switches/xh8210-32dq-pid-261327238?offeringId=252837181)

9[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU3NTEwNjEzOF19
-->