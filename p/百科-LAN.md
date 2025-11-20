# 什么是局域网？

LAN（Local Area Network，局域网）指有限区域内由计算机和其它网络设备互联组成的计算机网络。网络内的设备能够互相通信、共享资源。局域网可大可小，大到办公室或学校中拥有数千个用户和设备的企业网络，小到只有一个用户的家庭网络。

目录

-   [局域网由什么组成？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B1%80%E5%9F%9F%E7%BD%91.html#content1)
-   [局域网的分类](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B1%80%E5%9F%9F%E7%BD%91.html#content2)
-   [局域网有哪些优点？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B1%80%E5%9F%9F%E7%BD%91.html#content3)
-   [局域网、城域网和广域网有什么区别](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B1%80%E5%9F%9F%E7%BD%91.html#content4)

## 局域网由什么组成？

局域网是一个有限地理区域内的网络，通常由连接线路（电缆、[以太网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BB%A5%E5%A4%AA%E7%BD%91.html "以太网")线、光纤、无线信道等）、网络连接设备（HUB、[交换机](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html "交换机")、[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")等）、其他相关网络设备（例如[防火墙](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E9%98%B2%E7%81%AB%E5%A2%99.html "防火墙")等安全设备）等组成。其中路由器、交换机是局域网中常见的网络设备，路由器设备通常作为[网关](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")，用于连接局域网到Internet。交换机设备通常用于连接局域网内的终端设备（笔记本电脑、打印机、台式计算机、手机等），能使设备间快速传输数据，一般应用于较大空间的企业局域网。

![企业局域网](https://download.huawei.com/mdl/image/download?uuid=c34ae357c918433588a30ddc77b96018 "企业局域网")  
企业局域网

局域网在加速设备传输数据的同时，也产生了广播泛滥，通信冲突的问题。为解决该问题，在局域网的基础上，出现了[VLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VLAN.html "VLAN")（Virtual Local Area Network），将局域网从逻辑上分为多个独立的广播域，VLAN内的主机间通信就和在一个LAN内一样，而VLAN间则不能直接互通，广播报文就被限制在一个VLAN内。

![VLAN划分](https://download.huawei.com/mdl/image/download?uuid=50c12da910114c9d951c7891f7b27064 "VLAN划分")  
VLAN划分

## 局域网的分类

### 按拓扑结构分类

在实际局域网组网中，网络节点可以根据需要连接成多种拓扑结构，典型的拓扑结构有总线型结构、环型结构、星型结构、树型结构、网状结构、全连接结构等。

-   总线型结构
    
    总线结构通常采用广播信道，即网上的一个节点（主机）发送数据时，其他所有节点都能接收总线上的数据，这种结构容易产生通信冲突，通信效率一般比较低。
    
    图1-4  总线型结构
    
    ![](https://download.huawei.com/mdl/image/download?uuid=bf6a60cb008d435b97e23996b7df65cc)
    
-   环型结构
    
    环型结构一般采用点对点通信模式，即一个网络节点将数据沿一定方向传送到下一个网络节点，数据在环内依次高速传输，为了提升可靠性，也常使用双环结构。
    
    图1-5  环型结构
    
    ![](https://download.huawei.com/mdl/image/download?uuid=e84f2180b1af4647ba399a24f16b329b)
    
-   星型结构
    
    星型结构有一个中心节点，该节点执行数据交换网络控制功能。这种结构易于实现故障的隔离和定位，但是它存在瓶颈问题，一旦中心节点出现故障，将导致网络失效。因此为了增强网络可靠性，一般会采用备份系统，设置热备的中心节点。
    
    图1-6  星型结构
    
    ![](https://download.huawei.com/mdl/image/download?uuid=d72c99f7ba6c4ccba1bc23847d1d18fe)
    
-   树型结构
    
    树型结构的连接方法像一棵树一样，从顶部开始向下逐步分层、分叉。这种结构中执行网络控制功能的节点通常位于树的顶点，在树枝上很容易增加节点，扩大网络的规模。但是，由于数据流量层层收敛，最终会收敛至树的顶点，因此容易出现流量的瓶颈问题。
    
    图1-7  树型结构
    
    ![](https://download.huawei.com/mdl/image/download?uuid=5afb992f45764bf6af90ed76566484ce)
    
-   网状结构
    
    网状结构的特点是节点的用户数据可以选择多条[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")通过网络，网络的可靠性高，但是网络的结构和协议比较复杂。目前大多数复杂的的数据通信网络都采用了这种结构。
    
    图1-8  网状结构
    
    ![](https://download.huawei.com/mdl/image/download?uuid=e366f8624e594526abadd00f4e739007)
    
-   全连接结构
    
    全连接结构适用于对可靠性和有效性要求比较高的网络，通常将交换节点互连成全连接的结构，多个（或者多级）节点可以继续全互连，这种结构容易实现无阻塞的高速数据交换，可扩展性强，相应的这种网络的构造成本也比较高。
    
    图1-9  全连接结构
    
    ![](https://download.huawei.com/mdl/image/download?uuid=7a2da55a116a4ac391268ebf768e8f5a)
    

### 按照工作模式分类

根据局域网内设备间数据交换和资源共享方式的不同，分为两种局域网类型：客户端/服务器（Client/Server）和点对点（Peer-to-Peer）。

-   客户端/服务器局域网
    
    客户端/服务器局域网由连接到服务器的多个设备（称为客户端）组成。服务器除了控制文件存储和共享以及打印机访问之外，还控制网络流量。此类网络中的客户端可以是笔记本电脑、台式计算机、平板电脑和智能手机等。客户端设备可以通过[以太网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BB%A5%E5%A4%AA%E7%BD%91.html "以太网")电缆（局域网电缆）或[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")连接（[无线局域网](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html "WLAN")）连接到服务器。
    
    客户端/服务器局域网提供了大量的网络控制，特别适合大型网络。但是，建立和维护这些局域网可能会带来更多的挑战。服务器是一个关键依赖项，它的故障可能会触发整个网络的故障。
    
    一般应用在数据安全、集中管理和可扩展性至关重要的商业、公司和企业环境。
    
    图1-10  客户端/服务器局域网
    
    ![](https://download.huawei.com/mdl/image/download?uuid=1e3c3470458b467b80794debee13fb9d)
    
-   点对点局域网
    
    点对点局域网没有服务器，无法像客户端/服务器局域网那样处理繁重的工作负载，因此他们通常较小。对于这种局域网类型，每个设备通过到[交换机](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html "交换机")或[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")的有线或无线连接，平等地共享资源和数据。
    
    局域网中的每个设备都可以同时充当客户端和服务器，设置简单。不需要任何特殊的网络软件。此外，如果一台计算机出现故障，它不会导致整个网络的故障。
    
    与客户端/服务器架构相比，缺点是缺乏集中控制和高级安全功能。一般应用在小基础设施的地方，例如家庭网络、小型办公室、临时网络。
    
    图1-11  点对点局域网
    
    ![](https://download.huawei.com/mdl/image/download?uuid=b4b7448fe2d44b92a0e57d71e49f8273)
    

### 按照传输介质分类

局域网内的数据交换是依赖传输介质把数据从源传送到目的地，根据传输介质一般可分为Ethernet（以太网）、[WLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html "WLAN")（[Wireless Local Area Network](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html "WLAN")，无线局域网），Token Ring（令牌环），FDDI（Fiber Distributed Data Interface，光纤分布数据接口），ATM（Asynchronous Transfer Mode，异步传输模式）。

-   Ethernet
    
    以太网的传输介质是物理层的基础，决定了信号的传输方式和质量。常见的以太网传输介质包括双绞线、同轴电缆和光纤。以太网作为迄今为止使用最广泛的局域网技术，使用简单的用户界面连接交换机、路由器和计算机等设备，通过 MAC（Media Access Control） 地址唯一标识主机，实现局域网互联。
    
-   WLAN
    
    WLAN是一种无线计算机网络，使用无线信道代替有线传输介质连接两个或多个设备形成一个局域网，网络部署灵活，使用自由，不受限于线缆和端口位置。目前是最热门的一种局域网。
    

-   Token Ring
    
    令牌环网中所有设备连接在一起形成一个逻辑环，数据通过一个称为令牌的特殊消息在网络中传输，设备按顺序相互传递，直到到达其起点。传输速率相对较低。目前这种网络比较少见。
    

-   FDDI
    
    FDDI采用双环结构，使用光纤作为传输介质，也是利用令牌来传递对环网的控制权。在性能和效率上都较Token Ring有很大提高，适用于对可靠性要求较高的环境。由于成本比较昂贵，市场占有率逐年缩减。
    

-   ATM
    
    ATM网络中使用了一种分组交换和复用技术，将数据编码为固定大小的信元，以信元为基本单位进行信息传输、复用和交换。如语音、视频和数据等各种服务类型的信息都是以固定长度的信元为单位来传输的，降低了网络[时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")，提高了交换速度。技术比较复杂，成本高。
    

## 局域网有哪些优点？

局域网最早产生在二十世纪60年代末，在大学和研究实验室主要用于将计算机连接到其他计算机。二十世纪80年代，随着[以太网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BB%A5%E5%A4%AA%E7%BD%91.html "以太网")技术的商业化和标准化，局域网才开始被广泛使用。随着[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")技术的广泛部署，局域网几乎在所有类型的环境中普遍使用。如今不仅家庭、学校和企业使用局域网，餐馆、咖啡店、商店也使用局域网。从PC、打印机和手机到物联网 (Internet of Things) 等越来越多的终端设备连接到局域网中。局域网带来的好处主要有以下几点。

-   资源共享
    
    局域网可以使多台计算机之间资源共享。用户可以共享文件、打印机、扫描仪和其它设备，无需为每个用户配备单独的设备，提高工作效率和资源利用率。
    
-   高效沟通
    
    局域网提供了设备之间的有效通信，使用户可以方便地发送和接收消息和数据。存储在服务器上的数据可以被局域网用户随时访问，促进无缝协作。
    
-   互联网连接
    
    局域网中的多个设备可以共享单个Internet连接。
    
-   数据保护
    
    局域网中可以很容易地配置安全协议和工具来设置不同用户的访问权限，从而形成一个安全的网络系统。此外，局域网容易控制和维护整个网络，确保数据共享和通信安全。
    

## 局域网、城域网和广域网有什么区别

现代的数据通信网络，根据网络的物理覆盖范围，主要可分为局域网、城域网（Metropolitan Area Network，MAN）、[广域网](https://info.support.huawei.com/info-finder/encyclopedia/zh/WAN.html "WAN")（Wide Area Network，[WAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/WAN.html "WAN")）。

-   局域网是计算机通信网络的末端，负责把一个较小区域（如家庭、学校、企业写字楼）内的各种终端设备连接在一起，接入网络。
-   城域网是计算机通信网络的分支，负责把一个城市或直辖市不同建筑中的局域网连接在一起。构建成一个城域网络内的互联网络。城域网比局域网大，但比广域网小。
-   广域网是一种大型计算机通信网络，负责把更大范围（省级、国家级、世界级）中的城域网络再连接成一个统一的互联网络。

![LAN，MAN，WAN关系图](https://download.huawei.com/mdl/image/download?uuid=71db19b895404e58b874ea0910fa948f "LAN，MAN，WAN关系图")  
LAN，MAN，WAN关系图

表1-1  LAN vs MAN vs WAN

特性

LAN

MAN

WAN

地理范围

通常限于较小的物理区域，如家庭、学校或者办公楼。

通常覆盖整个城市或特定地理区域。

跨越广泛地理区域，通常是城市、国家甚至是国家与国家之间。

传输速度

局域网的速度更快，因为它们覆盖的距离更短，因此发生拥塞的可能性也更小。

城域网通常使用高速光纤技术，有较高的传输速度，但比局域网慢。比广域网快

由于带宽可获得性，广域网的速度可能稍慢，但用户可能无法察觉到这一差异。

设备

局域网的数据传输主要依赖于物理层和数据链路层，通常使用的设备包括[交换机](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html "交换机")、HUB和  [AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")  等。

城域网的数据传输主要依赖物理层、数据链路层和网络层，通常使用的设备包括交换机、[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")。

广域网的数据传输主要依赖物理层、数据链路层和网络层，通常需要使用复杂的网络设备，如路由器。

成本

成本较低，建设和维护相对简单。

涉及多个局域网的管理，复杂性和成本比局域网有所增加。

由于距离较远以及技术的复杂性，通常成本较高。

安全性

由于是封闭系统，通常具有较高的安全性，但仍需防范内部威胁。

由于实现了不同地点之间的通信和资源共享，需要使用一些安全措施抵御外部威胁，如[防火墙](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E9%98%B2%E7%81%AB%E5%A2%99.html "防火墙")、加密、入侵检测系统等。

由于通过公共网络传输，需要更多的安全措施，如加密、隧道技术等。

网络[延迟](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")

由于数据传输距离短，因此延迟较低。

由于数据传输距离较长，延迟比局域网高。

由于数据包需要穿越更长的距离，因此延迟较高。

使用场景

局域网支持办公、学习、娱乐等日常计算任务的需求。

城域网连接城市内的政府机构、企业、学校、医院、居民住宅，为城市数字化建设提供基础支撑。

广域网连接了远程办公室、[数据中心](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83.html "数据中心")，并提供了互联网和  [VPN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VPN.html "VPN")  服务等。

参考资源

1[以太网交换配置指南（园区交换机）](https://support.huawei.com/enterprise/zh/doc/EDOC1100410518/8dd2ae9?idPath=24030814|21782164|21782167|259602657)

2[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B1%80%E5%9F%9F%E7%BD%91.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNjA4MTAxNjldfQ==
-->