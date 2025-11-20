# 什么是DNS？

TCP/IP提供了通过[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")来连接到设备的功能，但对用户来讲，记住某台设备的IP地址是相当困难的，因此专门设计了一种字符串形式的主机命名机制，这些主机名与IP地址相对应。在IP地址与主机名之间需要有一种转换和查询机制，提供这种机制的系统就是域名系统DNS（Domain Name System）。

目录

-   [为什么要有DNS？](https://info.support.huawei.com/info-finder/encyclopedia/zh/DNS.html#content1)
-   [域名的构成](https://info.support.huawei.com/info-finder/encyclopedia/zh/DNS.html#content2)
-   [DNS服务器、DNS客户端和DNS中继](https://info.support.huawei.com/info-finder/encyclopedia/zh/DNS.html#content3)
-   [DNS域名解析过程](https://info.support.huawei.com/info-finder/encyclopedia/zh/DNS.html#content4)
-   [DDNS客户端](https://info.support.huawei.com/info-finder/encyclopedia/zh/DNS.html#content5)

## 为什么要有DNS？

互联网中，一台计算机与其他计算机通信时，通过[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")唯一的标志自己。此时的IP地址就类似于我们日常生活中的电话号码。但是，这种纯数字的标识是比较难记忆的，而且数量也比较庞大。例如，每个[IPv4地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")是一个32位长的二进制数字，或者采用点分十进制展示成192.168.1.1这种格式，有接近43亿个的IPv4地址。DNS的作用就是将人类可读的名称转换为机器识别的IP地址，供计算机相互连接。DNS的工作原理和电话簿相似，都是管理名称和数字之间的映射关系。就像我们日常打电话，一般使用人名查找，很少直接输入电话号码一样。当我们上网打开某个网页、视频时，也很少直接使用IP地址，而是在浏览器里输入的URL地址，例如：https://www.huawei.com，这其实使用的就是计算机的名字，一般称为域名。

## 域名的构成

最初设备的域名由字符序列组成、所有设备的域名组成一个未分级的域名结构。未分级的域名结构存在命名冲突、管理维护复杂的缺点。因此，TCP/IP把DNS的域名设计成了分级的树状结构。每个申请加入Internet的国家都要向NIC注册一个顶级域名，顶级域采用组织模式和地理模式的划分模式，如cn代表中国、us代表美国等。常见的顶级域名如下表所示。NIC将顶级域的管理权分派给由其指定的管理机构，由这些管理机构再对被授权管理的域继续进行划分，从而形成了二级域。负责划分二级域的管理机构可以授权其下属的管理结构，由它们继续划分域。由此下去，便形成了层次型的Internet域名体系结构。

表1-1  顶级Internet域名及其含义

顶级Internet域名

含义

com

商业组织

edu

教育机构

gov

政府机构

mil

军事部门

net

主要网络支持中心

int

国际组织

org

其他组织

国家代码

国家（按照地理模式划分）

从语法上讲，每一个域名都是有标号序列组成，而各标号之间用点（小数点）隔开。以www.huawei.com域名为例，从右到左依次是：

-   com：顶级域名。代表商业组织。
-   huawei：二级域名，归属于某个公司自己的域名。
-   www：三级域名，表明某个公司提供的是什么服务，www代表普通网页。

## DNS服务器、DNS客户端和DNS中继

网络中与DNS相关的设备角色包括DNS服务器、DNS客户端和DNS中继。

### DNS服务器

DNS服务器是将域名指向对应[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")的服务器。DNS服务器中保存了一张域名和与之相对应的IP地址的表，以解析消息的域名。由于互联网连通的是全球资源，单一的域名服务器不足以支撑全部的地址转换操作，因此全球有多套域名服务器相互配合使用。

域名是分层结构，域名DNS服务器也是对应的层级结构。通过根域名服务器，依次请求顶级域名服务器和权威域名服务器，最终获取对应IP地址，并将该结果保存在本地域名服务器，以待下次DNS请求使用。当用户再次对同一域名发起访问时，可以直接从本地域名服务器获得结果，无需再次发起全球递归查询。

表1-2  DNS服务器的分类

分类

作用

根DNS服务器

根DNS服务器是最高层次的域名服务器，它知道所有顶级服务器的域名和IP地址，当本地域名服务器无法对域名进行解析时，首先对根域名服务器发起请求。

顶级域名服务器

顶级域名服务器负责管理该服务器下的所有二级域名，当收到DNS查询请求时，就会给权威域名服务器相应的回答。

权威域名服务器

负责某一个区域的域名服务器。当一个顶级域名服务器还不能给出最后查询回答时，就会告知下一步应当请求的权威域名服务器。

本地域名服务器

当一个主机发出DNS查询请求时，这个查询请求报文就发送给本地域名服务器。每一个互联网服务提供者ISP都可以拥有一个本地域名服务器。当本地域名服务器无法给出应答时，就会请求最高级的根域名服务器。

### DNS客户端

DNS客户端的作用是接收用户程序（User Program）的DNS请求，并对其作出回应。作为DNS客户端的设备上一般具备以下能力：

1.  启动DNS解析
    
    要使用DNS客户端功能，需要在设备上打开DNS解析的开关。
    
2.  指定服务器的IP地址
    
    要进行DNS域名解析，需要在设备上指定DNS服务器的IP地址。这样才能把查询请求发动到正确的DNS服务器上进行解析。
    
3.  指定DNS域后缀搜索列表
    
    DNS客户端所访问的一些服务器或主机的域名后缀往往都是相同的。用户可以预先设置一些域名后缀，在域名解析的时候，用户只需要输入域名的部分字段，系统会自动将输入域名加上不同的后缀进行解析。例如，用户想查询域名“huawei.com”，那么可以在后缀列表中配置com，然后输入“huawei”，系统会自动将输入域名与后缀连接成“huawei.com”进行查询。
    

### DNS中继

当DNS服务器的IP地址发生变化时，用户网络中每个DNS客户端上的配置都需要改变，这样工作量极大并且容易出错。此时，可以通过部署DNS中继解决该问题。DNS客户端上配置DNS中继的IP地址，DNS服务器的IP地址在DNS中继上配置。之后，DNS客户端会将DNS请求报文直接发送给DNS中继，由DNS中继将收到的DNS请求报文转发至DNS服务器。由此，当DNS服务器的IP地址发生变化时，仅需改变DNS中继上的配置即可，简化了网络管理。

DNS中继的工作原理如下图所示。

![DNS中继的工作原理](https://download.huawei.com/mdl/image/download?uuid=617c63daf80e4341ab725a8e52331006 "DNS中继的工作原理")  
DNS中继的工作原理

1.  DNS客户端将DNS请求报文发送给DNS中继，即请求报文的目的地址为DNS中继的IP地址。
2.  DNS中继收到请求报文后，将报文转发给DNS服务器，通过DNS服务器进行域名解析。

## DNS域名解析过程

通过域名获取对应[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")的过程称为域名解析。DNS域名解析分为以下两种方式：

-   静态域名解析
    
    静态域名解析是通过静态域名解析表进行的，即手动建立域名和IP地址之间的对应关系表，该表的作用可以将一些常用的域名放入表中。当DNS客户端需要域名所对应的IP地址时，即到静态域名解析表中去查找指定的域名，从而获得所对应的IP地址，提高域名解析的效率
    
-   动态域名解析
    
    动态域名解析需要专用的域名解析服务器（DNS服务器）运行域名解析服务器程序，提供从域名到IP地址的映射关系，负责接收客户提出的域名解析请求。
    

为提高查询速度，在解析域名时，首先采用静态域名解析的方法，如果静态解析不成功，再采用动态域名解析的方法。

![动态域名解析原理图](https://download.huawei.com/mdl/image/download?uuid=4a8ce32c6fa54412b276a3c40227c260 "动态域名解析原理图")  
动态域名解析原理图

如上图所示，DNS的工作过程如下：

1.  用户程序（如ping、telnet等）使用域名访问网络时，首先向DNS客户端的地址解析器发出DNS请求。
    
2.  地址解析器收到DNS请求后，首先查询本地域名缓存。
    
    -   如果本地域名缓存中存在该域名对应的映射表项，地址解析器就直接将域名对应的IP地址返回给用户程序。
    -   如果本地域名缓存中不存在所要查找的映射表项，地址解析器就向DNS服务器发送查询请求报文。
    
3.  DNS服务器收到查询报文后，首先判断请求的域名是否处于自己被授权管理的子域里，再根据不同的判断结果，向DNS客户端发送相应的响应报文。
    
    -   如果请求的域名在自己被授权管理的子域范围之内，该DNS服务器首先从自己的数据库中查找域名对应的IP地址。
    -   如果请求的域名不在自己被授权管理的子域范围之内，该DNS服务器就将请求交给上一级的DNS服务器处理。DNS服务器完成解析后，将解析的结果返回给DNS客户端。
    
4.  DNS客户端的地址解析器接收并解析DNS服务器发回来的响应报文，将解析结果返回给用户程序。
    

每次动态解析成功的域名与IP地址的映射均存放在动态域名缓存区中，当下一次查询相同域名的时候，就可以直接从缓存区中读取，不用再向域名服务器进行请求。缓存区中的映射在一段时间后会被老化删除，以保证及时从域名服务器得到最新的内容。

## DDNS客户端

利用DNS可以将域名解析为[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")，从而实现使用域名来访问网络中的节点。但是，DNS仅提供了域名和IP地址之间的静态对应关系，当节点的IP地址发生变化时，DNS服务器无法动态地更新域名和IP地址的映射关系。此时，如果仍然使用域名访问该节点，通过域名解析得到的IP地址是错误的，从而导致访问失败。动态域名系统DDNS（Dynamic Domain Name System）用来动态更新DNS服务器上域名和IP地址之间的映射关系，保证通过域名解析到正确的IP地址。

![通过DDNS服务器实现DDNS更新的典型组网图](https://download.huawei.com/mdl/image/download?uuid=67b393bd56b04c2da4638bf431fdcdcf "通过DDNS服务器实现DDNS更新的典型组网图")  
通过DDNS服务器实现DDNS更新的典型组网图

如[图1](https://info.support.huawei.com/info-finder/encyclopedia/zh/DNS.html#ZH-CN_CONCEPT_0000002099797613_mMcCpPsS_fig01)所示的组网图中，PC需要通过域名访问提供应用层服务的设备DeviceA。DeviceA接入Internet的接口从网络运营商动态获取IP地址，由于每次获取到的IP地址不同，导致域名和IP地址的对应关系会发生变化。而传统的DNS无法动态更新域名和IP地址的对应关系，这就会导致PC访问DeviceA失败。此时，可通过部署DDNS服务器来解决该问题。

1.  DeviceA作为DDNS客户端，当IP地址变化时，向DDNS服务器发送更新域名和IP地址映射关系的DDNS更新请求。
2.  DDNS服务器接收到DDNS客户端的DDNS更新请求后，负责通知DNS服务器动态更新域名和IP地址之间的映射关系。从而保证即使设备的IP地址改变，Internet用户仍然可以通过同样的域名访问设备。

参考资源

1[DNS配置指南（NetEngine AR路由器）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100458332&id=ZH-CN_TASK_0000001563870509)

2[DNS配置指南（CloudEngine S系列交换机）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100318314&id=ZH-CN_TASK_0000001563870509&lang=zh)

3[DNS配置指南（USG6000F防火墙）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100435565&id=ZH-CN_TASK_0000001563870509)

4[观看视频：（多媒体）【网络百科】IPv6基础系列 - 什么是IPv6 DNS？(6:38)](https://support.huawei.com/enterprise/zh/doc/EDOC1100249162)

5[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/DNS.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbODE1MTUwNjkyXX0=
-->