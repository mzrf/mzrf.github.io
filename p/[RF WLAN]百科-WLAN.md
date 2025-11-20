# 什么是WLAN？

无线局域网WLAN（Wireless Local Area Network）是一种无线计算机网络，使用无线信道代替有线传输介质连接两个或多个设备形成一个[局域网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B1%80%E5%9F%9F%E7%BD%91.html "局域网")LAN（Local Area Network），典型部署场景如家庭、学校、校园或企业办公楼等。WLAN是一个网络系统，而我们常见的[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")是这个网络系统中的一种技术。所以，WLAN和Wi-Fi之间是包含关系，WLAN包含了Wi-Fi。

目录

-   [WLAN的优势](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html#content1)
-   [WLAN和Wi-Fi有什么不同？](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html#content2)
-   [WLAN安全吗？](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html#content3)
-   [WLAN的漫游](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html#content4)
-   [WLAN的基本元素](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html#content5)
-   [WLAN的网络类型](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html#content6)
-   [WLAN是怎么工作的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html#content7)

## WLAN的优势

WLAN技术最早出现在美国，主要应用于最后一段网线的无线延伸，最主要的运用就是在家庭中使用，由于美国居住环境里铺放线路的困难（独立别墅、小院），加上经济发达，便携机、PDA等设备的普及率很高，人们对无线上网需求很强烈。从而导致WLAN技术普及加快。

和有线接入技术相比，WLAN的优势如下：

-   网络使用自由：凡是自由空间均可连接网络，不受限于线缆和端口位置。在办公大楼、机场候机厅、度假村、商务酒店、体育场馆、咖啡店等场所尤为适用。
-   网络部署灵活：对于地铁、公路交通监控等难于布线的场所，采用WLAN进行无线网络覆盖，免去或减少了繁杂的网络布线，实施简单，成本低，扩展性好。

## WLAN和Wi-Fi有什么不同？

[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")指的是Wi-Fi联盟的商标，也是一种基于IEEE 802.11标准的无线网络通信技术，目的是改善基于IEEE 802.11标准的无线网络产品之间的互通性。

WLAN的全称是Wireless Local Area Network，中文含义是无线局域网，WLAN的定义有广义和狭义两种：广义上讲WLAN是以各种无线电波（如激光、红外线等）的无线信道来代替有线[局域网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B1%80%E5%9F%9F%E7%BD%91.html "局域网")中的部分或全部传输介质所构成的网络；WLAN的狭义定义是基于IEEE 802.11系列标准，利用高频无线射频（如2.4GHz、5GHz或6GHz频段的无线电磁波）作为传输介质的无线局域网。我们日常生活中的WLAN，就是指的WLAN的狭义定义。在WLAN的演进和发展过程中，其实现技术标准有很多，如蓝牙、Wi-Fi、HyperLAN2等。而Wi-Fi技术由于其实现相对简单、通信可靠、灵活性高和实现成本相对较低等特点，成为了WLAN的主流技术标准，Wi-Fi技术也逐渐成为了WLAN技术标准的代名词。

简单来说就是，WLAN是一个网络系统，而Wi-Fi是这个网络系统中的一种技术。所以，WLAN和Wi-Fi之间是包含关系，WLAN包含了Wi-Fi。

## WLAN安全吗？

WLAN技术具有安装便捷、使用灵活、经济节约、易于扩展等优点。但是WLAN技术是以无线射频信号作为业务数据的传输介质，这种开放的信道使攻击者很容易对无线信道中传输的业务数据进行窃听和篡改。

WLAN常见安全威胁如下：

-   [Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")无认证：攻击者可随意连接无线网络，进而对整个网络进行攻击。
-   无线数据无加密：攻击者可以通过空口抓包对在无线信道中传输的业务数据进行窃听和篡改。
-   边界威胁：非法[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")与合法AP放出相同[SSID](https://info.support.huawei.com/info-finder/encyclopedia/zh/SSID.html "SSID")，导致用户连接非法AP，数据被攻击者截获。

针对以上这些安全威胁，设计了对应的安全防护措施，以保护客户网络能防御攻击。

-   防止未经授权使用网络服务的措施是链路认证和用户接入认证，通过部署企业级用户认证方案，对用户身份进行集中的认证和管理。

-   提高数据安全的措施是数据加密，通过部署更高加密强度的[WPA3](https://info.support.huawei.com/info-finder/encyclopedia/zh/WPA3.html "WPA3")保护空口传输的用户数据无法被破解。WPA3的密钥长度达到256 bit，是目前强度最高的加密算法。
-   针对非法AP的措施是无线攻击检测和反制，通过部署无线入侵检测系统（Wireless Intrusion Detection System，WIDS）/无线[入侵防御系统](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%85%A5%E4%BE%B5%E9%98%B2%E5%BE%A1.html "入侵防御")（Wireless Intrusion Prevention System，WIPS），实时发现空口威胁和钓鱼AP，并进行反制，保护客户网络不被非法入侵。

## WLAN的漫游

在WLAN网络中，无线终端用户具有移动通信能力。但由于单个[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")设备的信号覆盖范围都是有限的，终端用户在移动过程中，往往会出现从一个AP服务区跨越到另一个AP服务区的情况。为了避免移动用户在不同的AP之间切换时，网络通讯中断，引入了无线[漫游](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi%E6%BC%AB%E6%B8%B8.html "WiFi漫游")的概念。

无线漫游就是指工作站STA（Station）在移动到两个AP覆盖范围的临界区域时，STA与新的AP进行关联并与原有AP断开关联，且在此过程中保持不间断的网络连接。简单来说，就如同手机的移动通话功能，手机从一个基站的覆盖范围移动到另一个基站的覆盖范围时，能提供不间断、无缝的通话能力。

常见的WLAN漫游技术有传统漫游、快速漫游、智能漫游、无损漫游等几种。

## WLAN的基本元素

-   工作站STA（Station）：支持802.11标准的终端设备。例如带无线网卡的电脑、支持WLAN的手机等。

-   接入点[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")（[Access Point](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")）：为STA提供基于802.11标准的无线接入服务，起到有线网络和无线网络的桥接作用。
    
    ![STA和AP](https://download.huawei.com/mdl/image/download?uuid=9d0b3884028b4496934e8ac9fbbe4e9c "STA和AP")  
    STA和AP
    
-   虚拟接入点VAP（Virtual Access Point）：是AP设备上虚拟出来的业务功能实体。用户可以在一个AP上创建不同的VAP来为不同的用户群体提供无线接入服务。
    
    ![VAP的示意图](https://download.huawei.com/mdl/image/download?uuid=49ba6210b1704cd3a5a282c0d91bf7cd "VAP的示意图")  
    VAP的示意图
    
-   基本服务集BSS（Basic Service Set）：一个AP所覆盖的范围。在一个BSS的服务区域内，STA可以相互通信。
-   扩展服务集ESS（Extend Service Set）：由多个使用相同[SSID](https://info.support.huawei.com/info-finder/encyclopedia/zh/SSID.html "SSID")的BSS组成。
    
    ![BSS和ESS的关系](https://download.huawei.com/mdl/image/download?uuid=5b99565b69874ca681f5370cba32b451 "BSS和ESS的关系")  
    BSS和ESS的关系
    
-   分布式系统（Distribution System）：分布式系统是指AP之间通过无线链路连接两个或者多个独立的[局域网](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%B1%80%E5%9F%9F%E7%BD%91.html "局域网")（包括有线局域网和无线局域网），组建一个互通的网络实现数据传输。目前无线分布式系统主要基于WDS或MESH协议。

## WLAN的网络类型

在企业场景下，通常有以下几种WLAN的网络类型。

-   **AC+FIT  [AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")集中式部署**
    
    “AC+FIT AP”的模式目前广泛应用于大中型园区的[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")网络部署，如商场、超市、酒店、企业办公等。AC的主要功能是通过CAPWAP隧道对所有FIT AP进行管理和控制。AC统一给FIT AP批量下发配置，因此不需要对AP逐个进行配置，大大降低了WLAN的管控和维护成本。同时，因为用户的接入认证可以由AC统一管理，所以用户可以在AP间实现无线[漫游](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi%E6%BC%AB%E6%B8%B8.html "WiFi漫游")。
    
    对于小范围Wi-Fi覆盖的场景，本身所需AP数量较少，如果额外部署一台AC的话，会导致整体无线网络成本较高。这种场景下，如果没有用户无线漫游的需求，建议部署FAT AP；如果希望同时满足用户无线漫游的需求，建议部署云AP。
    
-   **FAT AP独立部署**
    
    FAT AP，又称为胖AP，独立完成Wi-Fi覆盖，不需要另外部署管控设备。但是，由于FAT AP独自控制用户的接入，用户无法在FAT AP之间实现无线漫游，只有在FAT AP覆盖范围内才能使用Wi-Fi网络。
    
    因此，FAT AP通常用于家庭或SOHO环境的小范围Wi-Fi覆盖，在企业场景已经逐步被“AC+FIT AP”和“云管理平台+云AP”的模式所取代。
    
-   **[Leader AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Leader+AP.html "Leader AP")+FIT AP集中式部署**
    
    Leader AP是FAT AP的一个扩展功能，是指FAT AP能够像AC一样，可以和多个FIT AP一起组建WLAN，由FAT AP统一管理和配置FIT AP，为用户提供一个可漫游的无线网络。“Leader AP+FIT AP”的组网架构继承了“AC+FIT AP”的组网架构，FAT AP本身可以看做是AC+FIT AP两个模块的组合，支持Leader AP功能前，仅支持管理自身的FIT AP模块；支持Leader AP功能后，管理自身FIT AP模块的同时，还能够扩展管理更多的FIT AP。
    
-   **云化部署**
    
    云AP自身功能和FAT AP类似，所以可以应用于家庭WLAN或SOHO环境的小型组网；同时，“云管理平台+云AP”的组网结构和“AC+FIT AP”的组网结构类似，云AP由云管理平台统一管理和控制，所以又可以应用于大中型组网。
    
    云AP支持[即插即用](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E5%8D%B3%E6%8F%92%E5%8D%B3%E7%94%A8.html "即插即用")，部署简单，并且不受部署空间的限制，能灵活的扩展，目前比较多的应用于分支较多的场景。
    

## WLAN是怎么工作的？

在WLAN中，信息在发射端需要先经过信源编码转换为便于电路计算和处理的数字信号，再经过信道编码和调制， 转换为无线电波发射出去。接收端接收到无线电波后，经过解调、解码，最后转成信息。信息可以是图像、文字、声音等。其中发送设备和接收设备使用接口和信道连接。

![WLAN的工作机制](https://download.huawei.com/mdl/image/download?uuid=e7a6d287280e48ef83470d436791b4ef "WLAN的工作机制")  
WLAN的工作机制

-   信源编码：信源编码是将最原始的信息，经过对应的编码方式，转换为数字信号的过程。信源编码可以减少原始信息中的冗余信息，即在保证不失真的情况下，最大限度压缩信息。不同类型的信息需要采用不同的编码方式处理，例如，H.264就是视频的一种编码方式。
-   信道编码：信道编码是一种对信息纠错、检错的技术，可以提升信道传输的可靠性。信息在无线传输过程中容易受到噪声的干扰，导致接收信息出错，引入信道编码能够在接收设备上最大程度地恢复信息，降低误码率。WLAN使用的信道编码方式包含二进制卷积编码（Binary Convolutional Encoding，BCC）和低密度奇偶校验码（Low Density Parity Check，LDPC）。
-   调制：数字信号在电路中表现为高低电平的瞬时变化，只有将数字信号叠加到高频振荡电路产生的高频信号上，才能通过天线转换成无线电波发射出去，叠加动作就是调制的过程。高频信号本身没有任何信息，只是用来“运载”信息，所以称为载波。调制的过程实际包含符号映射和载波调制。WLAN中常见的符号映射技术[QAM](https://info.support.huawei.com/info-finder/encyclopedia/zh/QAM.html "QAM")，载波调制技术是OFDM。

-   空口：对于有线通信很容易理解，设备上的接口是可见的，连接可见的线缆，而对于WLAN，接口是不可见的，连接着不可见的空间，为了便于理解和描述，将无线通信使用的接口称为空中接口，简称空口。
-   信道：信道是传输信息的通道。在WLAN中，802.11协议也定义出允许使用的无线信道频段和具体频率范围。

参考资源

1[阅读eBook：Wi-Fi 6](https://support.huawei.com/enterprise/zh/doc/EDOC1100195173)

2[了解华为WLAN产品](https://e.huawei.com/cn/products/enterprise-networking/wlan)

3[华为智简园区WLAN无线网桥技术白皮书](https://e.huawei.com/cn/material/networking/wlan/9943d119420c491495f0d698ddbbb121)

4[华为WLAN安全技术白皮书](https://e.huawei.com/cn/material/networking/wlan/7dc1db88d42b4325a8a62ad75adb0a8a)

5[华为WLAN漫游技术白皮书](https://e.huawei.com/cn/material/networking/campus-network/wlan/0648ddf4afb24dceb773edca9716ec8a)

6[华为云管理园区解决方案智能调优和漫游技术白皮书2.0](https://e.huawei.com/cn/material/networking/campus-network/wlan/866756d4097f41d4b6c646f91036ed9c)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NDExOTU3OTddfQ==
-->