# 什么是WAN？

WAN（Wide Area Network，广域网）指的是跨越多个国家、地区或城市的用于企业、组织或个人远距离通信的互联网络，其覆盖范围从几十公里到几千公里，可以实现相当大范围内的信息与资源共享。

目录

-   [LAN vs. WAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/WAN.html#content1)
-   [WAN的示例](https://info.support.huawei.com/info-finder/encyclopedia/zh/WAN.html#content2)
-   [WAN的技术与协议](https://info.support.huawei.com/info-finder/encyclopedia/zh/WAN.html#content3)
-   [WAN的优缺点](https://info.support.huawei.com/info-finder/encyclopedia/zh/WAN.html#content4)
-   [广域优化与SD-WAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/WAN.html#content5)

## LAN vs. WAN

提到WAN，就有一个绕不开的词：LAN。

LAN（Local Area Network，局域网），又称内网。通常指覆盖了一个较小区域（如家庭、小商店、企业写字楼的一层）的计算机网络。

WAN（Wide Area Network，广域网），又称外网。是连接了多个LAN或者其他网络的大型计算机网络，其覆盖范围几十公里到几千公里。其中最著名的一个WAN就是互联网。

![LAN与WAN](https://download.huawei.com/mdl/image/download?uuid=a5059daf58da45eeac4c593067512d86 "LAN与WAN")  
LAN与WAN

LAN通常应用于本地区域，并且多是通过一个中心位置连接到WAN，这个中心位置一般称之为[网关](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")。现在市面上可以作为网关的设备有很多种：家用的以[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")为主，企业用的则有[交换机](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html "交换机")（具有三层路由功能）、路由器、防火墙等。

LAN中的设备可通过有线、无线或者两者同时使用来进行连接与数据传递。举个例子，在家庭网络中，可以通过笔记本的[WIFI](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")功能接入路由器，观看互联网视频。而如果要玩网络游戏，绝大多数人则会选择通过一根网线使得台式电脑与路由器相连，来保证网络游戏的稳定。

![家庭LAN网络](https://download.huawei.com/mdl/image/download?uuid=e7f9584602034cc692932712eb94a463 "家庭LAN网络")  
家庭LAN网络

WAN则是通过连接多个LAN来实现，其连接方式也分为有线和无线。举个例子，在跨地域的企业网络中，不同地域的分支站点通过运营商提供的专线接入企业WAN，有些站点还会接入5G无线网络作为逃生线路，保障业务的平稳运行。 通过WAN，用户可以跨越多个位置连接企业的办公室、数据中心、云网络等。

![企业WAN网络](https://download.huawei.com/mdl/image/download?uuid=31dfa0d7d1374dd6ac44addd86792d35 "企业WAN网络")  
企业WAN网络

## WAN的示例

提到WAN的示例，很多人会想到互联网，甚至觉得WAN就是互联网。实际上互联网作为一个由全球范围的私有、公共、学术、商业、政府网络组成的超大型网络，已经成为了世界上最大、最多样化的WAN。所以我们可以说互联网是WAN，但是WAN不单单只有互联网，它也普遍应用于校园、政企、运营商等领域。根据适用需求与场景的不同，一般可以分为自建和租用两种。

1.  **自建WAN。**这种场景下，需要自建的组织有着极强的网络建设、配置与运维能力，同时由于自建WAN，所以完全自主可控。典型的例子有运营商所建设的骨干网、高校接入的教育网、国有企业的内部网络等。
2.  **租用WAN。**这种场景下，其组织对底层的网络实现并不关注，只需要有安全稳定的WAN即可，所以大多数会选择租用运营商提供的专线，来搭建自己的WAN。典型的例子有大型连锁商超的业务网络、银行证券企业的业务网络。而随着互联网的进一步发展，越来越多的组织也会租用更便宜的互联网服务来搭建自己的WAN。典型的例子有初创小公司的办公网络、大量业务与数据已搬迁到云上的公司业务网络等。

## WAN的技术与协议

WAN的实现即可通过有线技术，也可通过无线技术。

其所用到的技术与协议包括：

-   **分组交换**。分组交换是一种数据传输技术，将大数据包分组成为更小的数据包进行传输。每个分组都会搭载源地址与目标地址等控制信息，在传输过程中会根据网络不同的拥堵程度选择不同的路线。在接收方收到所有分组数据之前，无法重建原数据，这使得这种方式存在网络[延迟](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")和传输不可靠的问题。但由于其设计简单以及资源利用率高的优点，这种技术依然成为了全球计算机网络数据通信的主要基础，现在依然广泛应用于互联网。
-   **ATM（Asynchronous Transfer Mode，异步传输模式）。**ATM是一种较旧的信元交换技术与协议，可以传输语音、视频与数据。其有着传输速率高、延迟小的优点，但是由于其技术复杂、成本高昂，在千兆网络越来越盛行的当下，已逐渐被IP网络取代。
-   **帧中继**。帧中继是一种用于在 LAN 或 WAN 端点之间传输数据的技术与协议，它将数据打包成帧，以便通过共享帧中继网络进行传输。帧中继网络对于用户来说，它通过一条经常改变且对用户不可见的信道来处理和其他用户间的数据传输。随着Cable/DSL modem（俗称宽带猫）、[MPLS](https://info.support.huawei.com/info-finder/encyclopedia/zh/MPLS.html "MPLS")、[VPN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VPN.html "VPN")等技术的出现，帧中继也逐渐变得过时。
-   **POS（Packet over SONET/SDH）**。SONET（同步光网络）和 SDH（同步数字体系）是高速通信协议，旨在支持通过光纤网络进行语音、数据和视频信号的数字传输。POS 则定义了使用光纤和 SONET（同步光网络）或 SDH（同步数字层次结构）通信协议时点对点链路的通信方式。
-   **PPP（Point-to-Point Protocol，点对点协议）**。PPP 是一种数据链路协议，通过拨号或者专线的方式在两个网络节点之间创建直接连接，发送数据。我们家庭中使用最广泛的宽带接入方式是[PPPoE](https://info.support.huawei.com/info-finder/encyclopedia/zh/PPPoE.html "PPPoE")（PPP over Ethernet），在[以太网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BB%A5%E5%A4%AA%E7%BD%91.html "以太网")（Ethernet）上运行PPP完成用户的接入认证，用于ISP（Internet service provider，互联网服务提供商）为用户提供互联网服务。PPPoA（PPP over ATM）也是同理，只不过需运行在ATM网络中。
-   **MPLS（Multi-Protocol Label Switching，多标签协议交换）**。MPLS是一种被广泛应用的广域网技术，可提高网络数据传输的速度和效率。它为网络上传输的每个数据包添加预定义标签，相较于传统上利用网络地址来决定下一个节点，MPLS 则利用标签引导数据包沿着预定的路径发送，有助于更快地传输数据。由于其工作于协议栈中的链路层和网络层之间，所以可以承载许多不同类型的流量，包括：IP数据包、ATM、帧中继、同步光网络、以太网等。
-   **TCP/IP（The Transmission Control Protocol/Internet Protocol，传输控制协议/互联网协议）**。该技术由传输控制协议（TCP）和互联网协议（IP）组成，它们共同构成了互联网的基础。它是一个关键协议，通过指定数据如何封装、寻址、传输、路由和接收来定义端到端通信。
-   **[Overlay网络](https://info.support.huawei.com/info-finder/encyclopedia/zh/Overlay%E7%BD%91%E7%BB%9C.html "Overlay网络")**。Overlay网络作为一种建立在另一种网络之上的计算机网络，并不算特别新鲜。但随着[智能云网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%99%BA%E8%83%BD%E4%BA%91%E7%BD%91.html "智能云网")时代的到来，互联网的质量越来越好，使得在互联网之上建立高质量WAN网络成为可能。基于Overlay VPN的[EVPN](https://info.support.huawei.com/info-finder/encyclopedia/zh/EVPN.html "EVPN")、[VXLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VXLAN.html "VXLAN")、NVGRE等技术，在业务开通敏捷性、组网灵活性以及互联互通性等方面优势突出，目前已经逐渐成为新一代企业WAN的主流技术。
-   **4G/5G/LTE**。除了有线WAN，无线WAN的发展也相当快速。目前主流方案多使用4G、5G、LTE等移动电信蜂窝技术来传输数据，使得用户可在服务范围的任何地方连接上网。

## WAN的优缺点

-   **优点**
    1.  连接范围广：WAN可以连接物理相距遥远的多方用户，实现通信与资源传递。
    2.  资源集中：由于可忽略物理距离满足多方接入的需求，使得资源集中存储、服务器集中部署成为可能，方便后续的访问和管理。
    3.  可扩展性：WAN可以根据需求在原有的基础上增加新的用户、分支，而不是推倒重建。
-   **缺点**
    1.  成本高：虽然WAN可拓展性强，但是要新增一条企业级专线，涉及的租用费用、网络配置与运维费用也是一笔可观的开支。
    2.  网络复杂：目前广域网的建设多为租用运用商提供的专线或公用网络，而这些网络涉及的协议与技术较为复杂，需要专业人士进行设计和管理。
    3.  存在安全隐患：WAN容易发生数据泄露和信息丢失的情况，尤其是使用互联网来做企业WAN的场景。

## 广域优化与SD-WAN

随着越来越多的企业通过WAN链路访问云服务、数据中心和移动办公，流量激增，但是租用专线过于昂贵，且互联网链路的不够可靠，所以需要引入广域优化技术来降低企业带宽费用，并且优化应用的访问体验。

目前主流的广域优化技术包括：

-   **[自适应前向纠错](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%87%AA%E9%80%82%E5%BA%94%E5%89%8D%E5%90%91%E7%BA%A0%E9%94%99.html "自适应前向纠错")（[A-FEC](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%87%AA%E9%80%82%E5%BA%94%E5%89%8D%E5%90%91%E7%BA%A0%E9%94%99.html "自适应前向纠错")）**
-   **[多发选收](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%A4%9A%E5%8F%91%E9%80%89%E6%94%B6.html "多发选收")**
-   **[负载分担](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B4%9F%E8%BD%BD%E5%88%86%E6%8B%85.html "负载分担")**
-   **[广域数据消冗](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B9%BF%E5%9F%9F%E6%95%B0%E6%8D%AE%E6%B6%88%E5%86%97.html "广域数据消冗")**

虽然广域优化解决了一些广域网络痛点，降低了网络带宽费用，提升了用户的关键应用体验。但是显然，企业对于WAN想要的更多，借助[SDN](https://info.support.huawei.com/info-finder/encyclopedia/zh/SDN.html "SDN")的理念与[Overlay网络](https://info.support.huawei.com/info-finder/encyclopedia/zh/Overlay%E7%BD%91%E7%BB%9C.html "Overlay网络")相关的技术，[SD-WAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/SD-WAN.html "SD-WAN")应运而生。

![Huawei SD-WAN](https://download.huawei.com/mdl/image/download?uuid=05fac1c030fc46108cacf79d13249b23 "Huawei SD-WAN")  
Huawei SD-WAN

为了满足企业用户对于WAN的需求，华为SD-WAN如今有着如下四大核心价值。

1.  **强互联：灵活组网构建多云多网按需互联。**SD-WAN 可充分利用混合链路资源，灵活利用光纤、DSL、LTE 等混合链路的接入，快速实现络开通并优化链路成本。同时，SD-WAN 提供Hub-Spoke、Full-Mesh、层次化组网、IaaS/SaaS访问等丰富的组网模型，用于适配企业不同的业务。
2.  **优体验：应用选路和优化保障关键应用体验**。可提供[应用识别](https://info.support.huawei.com/info-finder/encyclopedia/zh/SAC.html "SAC")、[智能选路](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%99%BA%E8%83%BD%E7%AD%96%E7%95%A5%E8%B7%AF%E7%94%B1.html "智能策略路由")、广域优化等功能，保障企业关键应用体验。
3.  **高性能：高性能分支站点设备构筑转发新引擎**。设备处理能力从一层～三层以包转发为核心延伸到三层～七层以应用为核心的全业务处理，支撑企业业务正常运转。
4.  **易运维：业务驱动的极简分支[网络运维](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E7%BD%91%E7%BB%9C%E6%99%BA%E8%83%BD%E8%BF%90%E7%BB%B4.html "网络智能运维")**。SD-WAN继承了SDN集中管控的设计思想，提供了全网的集中监控和可视化，可实时获取全网拓扑、站点间链路状态、流量统计以及关键的设备告警日志等信息。另外，SD-WAN通过[ZTP](https://info.support.huawei.com/info-finder/encyclopedia/zh/ZTP.html "ZTP")等方式，可实现分支的快速部署和上线。这种[即插即用](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%8D%B3%E6%8F%92%E5%8D%B3%E7%94%A8.html "即插即用")的部署方式降低了技术门槛，无须专业网络工程师到现场部署，节省了人力成本。

参考资源

1[阅读eBook：SD-WAN](https://support.huawei.com/enterprise/zh/doc/EDOC1100212003)

2[了解SD-WAN（SD-WAN解决方案）](https://support.huawei.com/enterprise/zh/enterprise-network-solution/sd-wan-pid-22584369?category=product-documentation-sets&subcategory=downloadable-product-documentation-package)

3[了解CloudWAN（云广域解决方案）](https://support.huawei.com/enterprise/zh/enterprise-network-solution/cloudwan-pid-253932239)

4[配置广域网接入（NetEngine路由器](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100366057&id=ZH-CN_TOPIC_0000001610643377)

5[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/WAN.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM1NzA2OTM3OV19
-->