# 什么是IPv4？

IPv4（Internet Protocol version 4）是互联网协议（Internet Protocol， IP）的第四版，是当前广泛使用的互联网协议之一，奠定了互联网通信的基础。  
IPv4通过32位的IPv4地址唯一标识和定位设备，使数据包能够正确地从一个设备转发到另一个设备，为设备提供了IP基本的网络连接和通信能力。由于IPv4地址空间有限，随着互联网的发展，IPv4地址用尽的问题日益严重，推动了[IPv6](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv6.html "IPv6")的产生和发展。

目录

-   [IPv4是如何产生的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html#content1)
-   [IPv4有哪些核心技术？](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html#content2)
-   [IPv4有什么局限性？](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html#content3)

## IPv4是如何产生的？

IP协议是TCP/IP协议族中最为核心的协议，它是随着计算机网络的发展逐渐产生并发展起来的。IPv4的第一个正式定义出现在1981年的 RFC 791中，详细描述了IP地址的分配规则和网络的分组交换机制。并在之后发布了多个更新协议，包括RFC 1349、RFC 2474、RFC 6864等，为IPv4的差分服务及分片重组等提供了指导和规范。随着互联网的迅速发展和商业化，IPv4逐渐成为全球化的标准协议。

![IPv4的发展历史](https://download.huawei.com/mdl/image/download?uuid=25b6d7d671724d488ea4f249199dd723 "IPv4的发展历史")  
IPv4的发展历史

## IPv4有哪些核心技术？

IPv4的核心技术包括IPv4地址分配规则、IP数据报文格式 、网络的分组[交换机](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html "交换机")制及[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")选择等。这些技术共同构成了IPv4的基本功能，使得它可以在全球范围内有效地管理和分配网络地址，并实现数据包的路由和传输。

### IPv4地址

在IP网络中通信，每个主机都需要拥有一个IP地址，用于标识主机在网络中的位置。IP地址并不是一种物理地址，而是逻辑地址，即地址是可以被分配、非固定、可修改的。

-   对于一台主机，作为数据的终端，拥有1个IP地址就可以参与到网络中与其他节点进行通讯。
-   对于一个网络设备，作为数据的中转站，每个接口都拥有1个或多个IP地址，用于指导主机数据在网络中的转发。

**IPv4地址格式**

IPv4使用32位的二进制数来表示IP地址，理论上整个IPv4地址空间最多有约42亿个地址。

IPv4地址可以被写作任何表示一个32位整数值的形式。但为了方便阅读和使用，通常表示为点分格式。下面IPv4地址举例展示了点分十进制和点分十六进制的表达方式。

![IPv4地址格式举例](https://download.huawei.com/mdl/image/download?uuid=a1883887f59a49ad9b5f4faddca74c9c "IPv4地址格式举例")  
IPv4地址格式举例

在点分格式中，也支持零的省略写法。例如，对于上面点分十进制的192.168.000.001，可以写为192.168.0.1，也可以写为192.168..1。点分十六进制的0xc0.0xa8.0x00.0x1可以写作0xc0.0xa8.0x0.0x1，也可以写作0xc0.0xa8..0x1。

**IPv4地址分类**

IPv4地址被划分为网络位和主机位。网络位表示所在的逻辑网络区域，主机位表示该主机在网段中的具体逻辑位置。同一网络区域中所有主机的网络位是同一个。不同的网络位长度表示的网络规模不同。

如果把IP地址和电话号码做类比：电话号码(001)907-1234567中，(001)907是区号，代表美国阿拉斯加州，类似于IP地址中的网络位；1234567是阿拉斯加州内某一个电话机的确切号码，类似于IP地址中的主机位。

当IP数据包在网络中传递时，[路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")只关心目的IP地址的网络位，通过识别IP地址的网络位为IP数据包进行路由操作。而只有当数据包达到了目的的网段以后，才通过IP地址的主机位查找具体的接收主机。

IPv4地址根据网络规模的不同，将地址划分为A、B、C三类，称为主类网。同时还定义了用于组播寻址的D类地址，以及被保留用于未来使用的E类地址。这五类地址类由IPv4地址的第一个字节的高位决定。

![IPv4地址分类](https://download.huawei.com/mdl/image/download?uuid=54715396e38d4a339ef112dd9ad952cc "IPv4地址分类")  
IPv4地址分类

在主类网地址中，有一部分被用做了私有地址。私有地址是不可以在互联网上使用的，是在企业或组织内部局域网上使用的IP地址。这样，可以不为局域网中的主机分配互联网可用的地址，从而节约有限的IP地址资源。私有地址又称为私网地址或假地址，除此之外，其他可以在互联网上使用的IP地址称为公网地址或真地址。

![IPv4五类地址范围](https://download.huawei.com/mdl/image/download?uuid=abb04f83a45441488d16c677ccf8cf61 "IPv4五类地址范围")  
IPv4五类地址范围

这些地址分类基于早期的IPv4设计，在实际应用中，由于地址空间的有限性和地址耗尽问题，IPv4地址的分配方式已经被广泛调整和优化，例如使用子网掩码进行更精细的网络划分和地址分配。

**子网掩码**

子网掩码（Subnet Mask）是IPv4地址中用来划分网络和主机部分的32位二进制数，它与IP地址一起使用，形成一个IP网络地址，表示为IP地址/子网掩码（例如，192.168.1.1/255.255.255.192）。

![子网划分示例](https://download.huawei.com/mdl/image/download?uuid=5faf400f2fc3467e9ac78384f7133b49 "子网划分示例")  
子网划分示例

通过灵活使用子网掩码，可以将一个大的网络划分成多个子网，以便更有效地管理和控制网络流量和安全性。CIDR（Classless Inter-Domain Routing，无类别域间路由）就是一种灵活的IP地址分配和路由选择方法，它允许根据需要动态分配子网掩码位数，以更有效地利用IP地址空间。CIDR表示法可以用来表示一个IP地址范围及其对应的子网掩码位数，例如192.168.1.1/26表示IP地址范围为192.168.1.0到192.168.1.63，子网掩码为255.255.255.192。

### IPv4报文格式

IP层提供的服务是通过IP层对报文的封装与拆封来实现的。IPv4报文的格式分为报头区和数据区两大部分。

IPv4报文的转发控制是由IP头决定的，IP头由两部分组成，前一部分是固定长度，共20字节，是所有IP报文必须具有的；后一部分是一些可选字段，其长度是可变的。下面详细介绍IP头中的各字段信息。

![IP头格式](https://download.huawei.com/mdl/image/download?uuid=19d277737b78401fa516da7fd8aca356 "IP头格式")  
IP头格式

表1-1  IP头字段解释

字段

长度

含义

Version

4比特

-   4：表示为IPv4；
-   6：表示为[IPv6](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv6.html "IPv6")。

IHL

4比特

首部长度，如果不带Option字段，则为20，最长为60，该值限制了记录路由选项。以4字节为一个单位。

Type of Service

8比特

服务类型。只有在有[QoS](https://info.support.huawei.com/info-finder/encyclopedia/zh/QoS.html "QoS")差分服务要求时这个字段才起作用。

Total Length

16比特

总长度，整个IP数据报的长度，包括首部和数据之和，单位为字节，最长65535，总长度必须不超过最大传输单元[MTU](https://info.support.huawei.com/info-finder/encyclopedia/zh/MTU.html "MTU")。

Identification

16比特

标识，主机每发一个报文，加1，分片重组时会用到该字段。

Flags

3比特

标志位。字段格式如下：

![Flags标记位字段格式](https://download.huawei.com/mdl/image/download?uuid=c4992a7b3dd14194a559516a2666a3f1 "Flags标记位字段格式")  
Flags标记位字段格式

-   Bit 0: 保留位，必须为0。
-   Bit 1: DF（Don't Fragment），能否分片位，0表示可以分片，1表示不能分片。
-   Bit 2: MF（More Fragment），表示是否该报文为最后一片，0表示最后一片，1代表后面还有。

Fragment Offset

13比特

片偏移：分片重组时会用到该字段。表示较长的分组在分片后，某片在原分组中的相对位置。以8个字节为偏移单位。

Time to Live

8比特

生存时间：数据包在网络中的最大生存时间。

Protocol

8比特

协议：下一层协议。指出此数据包携带的数据使用何种协议，以便目的主机的IP层将数据部分上交给哪个进程处理。

Header Checksum

16比特

首部检验和，只检验数据包的首部，不检验数据部分。这里不采用[CRC](https://info.support.huawei.com/info-finder/encyclopedia/zh/CRC.html "CRC")检验码，而采用简单的计算方法。

Source Address

32比特

源IP地址。

Destination Address

32比特

目的IP地址。

Options

可变

选项字段，用来支持排错，测量以及安全等措施，内容丰富。选项字段长度可变，从1字节到40字节不等，取决于所选项的功能。

Padding

可变

填充字段，全填0。

### 报文分片和重组

IP协议位于TCP/IP模型的网络层，IP报文的发送和接收依赖链路层提供的服务。当IP报文的长度大于链路层MTU（Maximum Transmission Unit，最大传输单元）时，需要对报文进行分片，以使他们可以在网络上传输。当分片报文通过网络传输到接收端时，接收端将收到的分片报文重组成原始的数据包。IPv4报文分片和重组过程如下：

-   分片
    1.  发送端根据目标主机的MTU，检查将要发送的报文大小。
    2.  如果报文长度超过了MTU，发送端就会将数据包分割成更小的片段，每个片段大小不能超过MTU。
    3.  每个片段都是一个独立的IP报文，但它们共享相同的IP头部信息（除了片偏移和分片标志段不同）。
-   重组
    
    1.  接收端收到这些分片后，根据每个IP数据包的标识符、片偏移和分片标志来确定它们应该如何组装。
    2.  接收端将所有分片组合成原始IP报文。
    3.  重组后的完整报文被传递给上层协议处理。
    

例如，一个总长度为4020字节的IP报文，其中IP头长度为20字节，数据区为4000字节，要通过MTU为1500的链路层发送，就需要把报文进行分片。因IP头长度为20字节，分片的数据区长度不能超过1480字节，原始IP报文可以分为3个分片报文，数据区长度分别为1480、1480和1040字节。除标志和片偏移字段外，分片的IP头信息与原始IP报文的IP头信息完全一致。

![IPv4报文分片举例](https://download.huawei.com/mdl/image/download?uuid=16925e1c34aa4a63a796cbaeeec1dd66 "IPv4报文分片举例")  
IPv4报文分片举例

## IPv4有什么局限性？

以IPv4为核心技术的因特网获得巨大成功，促使IP技术得到广泛应用。但是，随着因特网的迅猛发展，IPv4设计的不足也日益明显，主要有以下几点。

-   IPv4地址空间不足
    
    IPv4地址空间共有32位，理论上能够提供的地址数量是43亿。但由于地址分配的原因，实际可使用的数量不到43亿。另外，IPv4地址的分配也很不均衡：美国占全球地址空间的一半左右，而欧洲则相对匮乏；亚太地区则更加匮乏。与此同时，移动IP和宽带技术的发展需要更多的IP地址。IPv4地址资源紧张直接限制了IP技术应用的进一步发展。
    
-   设备维护的[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")表表项数量过大
    
    由于IPv4发展初期的分配规划问题，造成许多IPv4地址的分配不连续，不能有效聚合路由。日益庞大的路由表耗用大量内存，对设备成本和转发效率产生影响，这一问题促使设备制造商不断提升其产品的路由寻址和转发性能。
    
-   不易进行自动配置和重新编址
    
    由于IPv4地址只有32比特，并且地址分配不均衡，导致在网络扩容或重新部署时，经常需要重新分配IP地址。维护工作量较大。
    
-   不能解决日益突出的安全问题
    
    随着因特网的发展，安全问题越来越突出。IPv4协议制定时并没有仔细针对安全性进行设计，因此固有的框架结构并不能保障端到端的安全。
    

IPv4的这些局限性促使了[IPv6](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv6.html "IPv6")的开发和推广，以解决IPv4所面临的各种问题，并为未来互联网的增长和创新提供更为广阔和可持续的基础。

更多IPv6相关介绍请参见：[什么是IPv6](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv6.html)。

参考资源

1[IPv4基础配置指南（NetEngine 8000 X 产品文档）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100363842&id=ZH-CN_TOPIC_0000001155784207)

2[观看视频：IP基础快速入门 - TCP/IP参考模型 （1:01:30）](https://info.support.huawei.com/info-finder/vue/#/zh/enterprise/onlinecourses/detail?video=%28%E5%A4%9A%E5%AA%92%E4%BD%93%29%20IP%E5%9F%BA%E7%A1%80%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8%20-%20%E6%95%B0%E9%80%9A%E5%9F%BA%E7%A1%80%20-%20TCP%2FIP%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%2002)

3[观看视频：IP基础快速入门 - IP子网划分（40:46）](https://support.huawei.com/enterprise/zh/doc/EDOC1000122545)

4[IP报文格式](https://support.huawei.com/enterprise/zh/doc/EDOC1100174722/fc60e39)

5[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTk0NDM0NDQ5XX0=
-->