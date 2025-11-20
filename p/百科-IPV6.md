# 什么是IPv6？

IPv6（Internet Protocol Version 6）是网络层协议的第二代标准协议，也被称为IPng（[IP](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")  Next Generation），它所在的网络层提供了无连接的数据传输服务。IPv6是IETF设计的一套规范，是[IPv4](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")的升级版本。它解决了目前IPv4存在的许多不足之处，IPv6和IPv4之间最显著的区别就是[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")长度从原来的32位升级为128位。IPv6以其简化的报文头格式、充足的地址空间、层次化的地址结构、灵活的扩展头、增强的邻居发现机制将在未来的市场竞争中充满活力。

目录

-   [为什么会有IPv6?](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv6.html#content1)
-   [什么是IPv6？](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv6.html#content2)
-   [IPv4 vs IPv6](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv6.html#content3)
-   [部署IPv6对现有网络和业务的影响](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv6.html#content4)

## 为什么会有IPv6?

[IP](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")（Internet Protocol）是TCP/IP协议族中的网络层协议（网络层协议主要作用是：在互联网中进行寻址，引导数据包能够正确的到达目的地）。[IPv4](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")协议是目前广泛部署的因特网协议。在Internet发展初期，IPv4以其协议简单、易于实现、互操作性好的优势而得到快速发展。但随着网络的迅猛发展，IPv4协议的各种问题开始显现：

1.  **公有[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")数量不足**
    
    [IPv4地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")由全球5个互联网地址分配机构管理负责，IPv4地址空间约42.9亿，实际可用约36.47亿个，已在2019年全部分配完毕，这意味着没有更多的IPv4地址可以分配给网络服务提供商或企业。作为严重稀缺资源，用户申请固定公有IP地址困难加大，并且费用十分昂贵。
    
2.  **私有地址交流效率低**
    
    在IPv4地址枯竭阶段和IPv6过渡工作未完成之前，通过[NAT](https://info.support.huawei.com/info-finder/encyclopedia/zh/NAT.html "NAT")技术暂时解决了地址匮乏和爆炸式增长的入网需求问题，但NAT技术本身也存在不足，例如，增加了网络的复杂度。由于维护IP地址间及端口号映射关系而增加的网络设备工作负担，使网络整体结构变得脆弱。互联网的本质是提供人与人之间的连接，NAT破坏了这个原则。
    
3.  **设备维护的路由表表项数量过大**
    
    由于IPv4发展初期的分配规划问题，造成许多IPv4地址的分配不连续，不能有效聚合路由。日益庞大的路由表耗用大量内存，对设备成本和转发效率产生影响。
    
4.  **不易进行自动配置和重新编址**
    
    由于IPv4地址只有32 bit，并且地址分配不均衡，导致在网络扩容或重新部署时，经常需要重新分配IP地址，维护工作量较大。
    
5.  **远程访问无法保证业务质量**
    
    在传统的企业组网配置中，对于移动用户（移动办公人员）、远端用户和合作伙伴联网需求，一般会通过[VPN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VPN.html "VPN")（Virtual Private Network，虚拟专用网）技术以专用软件、专用/集成硬件或搭建VPN服务器等方式实现。由此带来了软件开发运维复杂度高、硬件产品方案兼容性差、IT（Information Technology，信息技术）投入成本加大、安全风险提高等问题，并且企业无法预料基于公共互联网传输的可靠性，在面对大流量传输时无法差异化保证业务质量。
    
6.  **安全溯源困难**
    
    IPv4制定时并没有仔细针对安全性进行设计，因此，固有的框架结构并不能支持端到端的安全。企业正在使用的IPv4网络，由于其在设计时几乎没有安全性考虑，随着地址枯竭和分配严重不平衡，NAT方式成为主流选择，即NAT背后的终端用户分配到的一般都是私有地址，网络中一旦有非法信息发布或者[病毒](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%97%85%E6%AF%92.html "计算机病毒")传播，是难以追溯到源地址的，这大大加剧了网络安全问题。
    

IETF曾提出过IPv6、IPv7、IPv8、IPv9等四个草案，并希望其中的一种协议能够替代IPv4。经过充分的讨论，IETF最终选择IPv6并替代IPv4，而IPv7、IPv8、IPv9也就从此销声匿迹。至于IPv5，1990年，IETF曾经提出过IPv5的草案，最初希望IPv5负责承载语音、视频等“流”业务，与负责承载数据业务的IPv4共同在网络运行。但这一草案仅停留在了时延阶段，没有被最终采用。

![IPv6的演进](https://download.huawei.com/mdl/image/download?uuid=194571f9dd2047ee86202f758b170bde "IPv6的演进")  
IPv6的演进

## 什么是IPv6？

### IPv6地址的书写格式

IPv6的128位[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")有以下两种表示形式。

-   X:X:X:X:X:X:X:X
    
    -   在这种形式中，128位的IPv6地址被分为8组，每组的16位用4个十六进制字符（0～9，A～F）来表示，组和组之间用冒号（:）隔开。其中每个“X”代表一组十六进制数值。比如下面这个IPv6地址：
        
        2001:db8:130F:0000:0000:09C0:876A:130B
        
        为了书写方便，每组中的前导“0”都可以省略，所以上述地址可写为：
        
        2001:db8:130F:0:0:9C0:876A:130B。
        
    -   另外，地址中包含的连续两个或多个均为0的组，可以用双冒号“::”来代替，这样可以压缩IPv6地址书写时的长度，所以上述地址又可以进一步简写为：
        
        2001:db8:130F::9C0:876A:130B。
        
        在一个IPv6地址中只能使用一次双冒号“::”，否则当计算机将压缩后的地址恢复成128位时，无法确定每段中0的个数。
        
-   X:X:X:X:X:X:d.d.d.d
    
    [IPv4](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")映射IPv6地址。地址格式为：0:0:0:0:0:FFFF:IPv4-address。该地址用来将IPv4节点的地址表示为IPv6地址。
    
    其中“X”代表高阶的六组数字，用十六进制数来表示每组的16比特。“d”代表低阶的四组数字，用十进制数表示每组的8比特。后边的部分（d.d.d.d）其实就是一个标准的[IPv4地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")。
    

### IPv6地址结构

一个IPv6地址可以分为如下两部分：

-   网络前缀：n比特，相当于IPv4地址中的网络ID
    
-   接口标识：128-n比特，相当于IPv4地址中的主机ID
    

地址2001:DB8:6101:1::E0:F726:4E58 /64的构成如下图所示。

![地址2001:DB8:6101:1::E0:F726:4E58 /64的构成示意图](https://download.huawei.com/mdl/image/download?uuid=a7d046f85b3f463d8b61590f65718885 "地址2001:DB8:6101:1::E0:F726:4E58 /64的构成示意图")  
地址2001:DB8:6101:1::E0:F726:4E58 /64的构成示意图

### IPv6的地址分类

IPv6主要有三种地址：

-   单播地址（Unicast）：唯一标识一个接口，类似于IPv4的单播地址。发送到单播地址的数据包将被传输到此地址所标识的唯一接口。
    
    配置的全球单播地址不能与该地址对应的网络前缀相同，因为该类型的地址是设备预留的子网[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")任播地址。对于前缀长度是127位的IPv6地址，不受该规则限制。
    
-   任播地址（Anycast）：用来标识一组接口（通常这组接口属于不同的节点）。发送到任播地址的数据包被传输给此地址所标识的一组接口中距离源节点最近的一个接口（最“近”的一个，是指根据路由协议的距离度量）。
    
    应用场景：当移动主机需要与它的“home”子网上的移动代理之一通信时，它将用该子网路由设备的任播地址。
    
    具体地址规定：任播地址没有独立的地址空间，它们可使用任何单播地址的格式。因此，需要一种语法来区别任播地址和单播地址。
    
    对于接口标识全为0的IPv6地址，标准协议中定义为子网路由器任播地址（Subnet-Router anycast address）。如下图所示，subnet prefix是单播IPv6地址前缀，由用户配置单播IPv6地址时指定。
    
    ![子网路由器任播地址格式](https://download.huawei.com/mdl/image/download?uuid=a6bf537a49cf4dcca027ebb13e55cbe3 "子网路由器任播地址格式")  
      
    子网路由器任播地址格式
    
    ![](https://download.huawei.com/mdl/image/download?uuid=b7de2d93be78429499cedf4f5a9a7ec0)
    
    任播地址不局限于子网路由器任播地址，全球单播地址也可以配置为任播地址。
    
-   [组播](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E7%BB%84%E6%92%AD.html "组播")地址（Multicast）：用来标识属于不同节点的一组接口，类似IPv4的组播地址。发送到组播地址的数据包被传输给此地址所标识的所有接口。
    
    IPv6不包括广播地址，广播地址的功能均由组播地址来提供。
    

单播地址还可以分为以下几种，如下表所示。

表1-1  IPv6单播地址类型

地址类型

二进制前缀

IPv6前缀标识

链路本地单播地址

1111111010

FE80::/10

唯一本地地址

1111110

FC00::/7

环回地址

00...1 (128 bits)

::1/128

未指定地址

00...0 (128 bits)

::/128

全球单播地址

其他

-

表中各类地址的意义如下：

-   链路本地单播地址：用于邻居发现协议和无状态自动配置进程中链路本地上节点之间的通信。使用链路本地地址作为源或目的地址的数据包不会被转发到其他链路上。使用链路本地前缀FE80::/10(1111 1110 10)和IEEE EUI-64格式的接口标识符（EUI-64可来源于EUI-48）可在以太接口对其进行自动配置。
    
-   唯一本地地址，仅用于同一个站点的地址。具有全球唯一的前缀，可以进行网络之间的私有连接，而不必担心地址冲突等问题。如果出现路由泄漏，不会造成Internet路由冲突。在应用中，上层应用程序将这些地址看作全球单播地址。
    
-   环回地址0:0:0:0:0:0:0:1或::1，不会被分配给任何接口。它的作用与在IPv4中的127.0.0.1相同，即节点将IPv6报文发送给自己。
    
-   未指定地址（::），不能被分配给任何节点，也不能作为目的地址。在主机初始化且没有取得自己的地址时，未指定地址可以用在IPv6报文的源地址字段，例如重复地址探测时，NS报文的源地址就是未指定地址。
    
-   全球单播地址等同于IPv4公网地址。用于可以聚合的链路，最后提供给网络服务提供商。这种地址类型的结构允许路由前缀的聚合，从而满足全球路由表项的数量限制。地址包括运营商管理的48位路由前缀和本地站点管理的16位子网ID，以及64位接口ID。如无特殊说明，全球单播地址包括站点本地单播地址。
    

## IPv4 vs IPv6

由于网络迅速发展，[IPv4](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")的设计不足也日益明显，IPv6相比IPv4提供了一些新特性和改善措施：

表1-2  IPv6、IPv4对比表

问题

IPv4的缺陷

IPv6的优势

地址空间

[IPv4地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")采用32比特标识，理论上能够提供的地址数量是43亿（由于地址分配的原因，实际可使用的数量不到43亿）。另外，IPv4地址的分配也很不均衡：美国占全球地址空间的一半左右，而欧洲则相对较少；亚太地区则更加匮乏。与此同时，移动[IP](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")和宽带技术的发展需要更多的[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")。目前IPv4地址已经消耗殆尽。

针对IPv4的地址短缺问题，也曾先后出现过几种解决方案。比较有代表性的是无类别域间路由CIDR（Classless Inter-Domain Routing）和网络地址转换[NAT](https://info.support.huawei.com/info-finder/encyclopedia/zh/NAT.html "NAT")（Network Address Translator）。但是CIDR和NAT都有各自的弊端和不能解决的问题，由此推动了IPv6的发展。

IPv6地址采用128比特标识。128位的地址结构使IPv6理论上可以拥有（43亿×43亿×43亿×43亿）个地址。近乎无限的地址空间是IPv6的最大优势。

报文格式

IPv4报头包含可选字段Options，内容涉及Security、Timestamp、Record route等，这些Options可以将IPv4报头长度从20字节扩充到60字节。携带这些Options的IPv4报文在转发过程中往往需要中间路由转发设备进行软件处理，对于性能是个很大的消耗，因此实际中也很少使用。

IPv6和IPv4相比，去除了IHL、Identification、Flags、Fragment Offset、Header Checksum、Options、Padding域，只增加了流标签域，因此IPv6报文头的处理较IPv4更为简化，提高了处理效率。另外，IPv6为了更好支持各种选项处理，提出了扩展头的概念，新增选项时不必修改现有结构，理论上可以无限扩展，体现了优异的灵活性。

自动配置和重新编址

由于IPv4地址只有32比特，并且地址分配不均衡，导致在网络扩容或重新部署时，经常需要重新分配IP地址，因此需要能够进行自动配置和重新编址，以减少维护工作量。目前IPv4的自动配置和重新编址机制主要依靠[DHCP](https://info.support.huawei.com/info-finder/encyclopedia/zh/DHCP.html "DHCP")协议。

IPv6协议内置支持通过地址自动配置方式使主机自动发现网络并获取IPv6地址，大大提高了内部网络的可管理性。

路由聚合

由于IPv4发展初期的分配规划问题，造成许多IPv4地址分配不连续，不能有效聚合路由。日益庞大的路由表耗用大量内存，对设备成本和转发效率产生影响，这一问题促使设备制造商不断升级其产品，以提高路由寻址和转发性能。

巨大的地址空间使得IPv6可以方便的进行层次化网络部署。层次化的网络结构可以方便的进行路由聚合，提高了路由转发效率。

对端到端的安全的支持

IPv4协议制定时并没有仔细针对安全性进行设计，因此固有的框架结构并不能支持端到端的安全。

IPv6中，网络层支持[IPSec](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPsec.html "IPsec")的认证和加密，支持端到端的安全。

对[QoS](https://info.support.huawei.com/info-finder/encyclopedia/zh/QoS.html "QoS")（Quality of Service）的支持

随着网络会议、网络电话、网络电视迅速普及与使用，客户要求有更好的QoS来保障这些音视频实时转发。IPv4并没有专门的手段对QoS进行支持。

IPv6新增了流标记域，提供QoS保证。

对移动特性的支持

随着Internet的发展，移动IPv4出现了一些问题，比如：三角路由，源地址过滤等。

IPv6协议规定必须支持移动特性。和移动IPv4相比，移动IPv6使用邻居发现功能可直接实现外地网络的发现并得到转交地址，而不必使用外地代理。同时，利用路由扩展头和目的地址扩展头移动节点和对等节点之间可以直接通信，解决了移动IPv4的三角路由、源地址过滤问题，移动通信处理效率更高且对应用层透明。

## 部署IPv6对现有网络和业务的影响

-   **IPv6对网络性能的影响**
    
    在[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")上开启IPv6技术对高性能的路由器影响非常小；一般情况下，部署IPv6对网络传输[时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")丢包率没有影响；在某个路由器出现故障的情况下，IPv6对更新信息，计算最佳的路径的效率影响很小。
    
-   **IPv6对网络维护的影响**
    
    在使用IPv6的协议过程中，增加了工程师的维护工作量和技能要求，但IPv6对网络维护的冲击比较小，具备维护[IPv4](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")能力的工程师可以在较短时间内掌握IPv6。
    
-   **IPv6对业务和应用的影响**
    
    在IPv6网络的现有网络业务和应用没有影响，您可以额外获得访问IPv6资源的能力。部署IPv6往往需要调整域名系统等业务系统，不正确的配置或有缺陷的软件将影响您的用户体验。
    
    这里，向您简单介绍一下IPv6与域名系统的关联：
    
    IPv6网络中，每一台网络设备都是由IPv6地址来标识的，只有获得了目的地网络设备的IPv6地址，才能成功进行访问。因为记住128位的IPv6地址是相当困难的，所以为IPv6网络建立了一套IPv6域名系统。这样，在对网络设备进行访问操作时，您可以直接使用便于记忆的域名，由网络中的服务器来将域名解析为IPv6地址。
    
    例如，Google提供给大众的公共域名解析服务器可以将您所输入的域名映射为IPv6地址，其自身的IPv6地址如下：
    
    -   2001:4860:4860::8888
    -   2001:4860:4860::8844
    

参考资源

1[IPv6基础配置（CloudEngine S系列交换机）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100318314&id=ZH-CN_TASK_0000001130622158&lang=zh)

2[IPv6基础配置 （HUAWEI NetEngine40E 产品文档](https://support.huawei.com/hedex/hdx.do?docid=DOC1100733075&id=ZH-CN_TASK_0139427895&lang=zh)

3[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv6.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI0MTc5MDg0Ml19
-->