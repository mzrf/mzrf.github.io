# 什么是DHCP？

动态主机配置协议DHCP（Dynamic Host Configuration Protocol）是一种网络管理协议，用于集中对用户[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")进行动态管理和配置。  
DHCP于1993年10月成为标准协议，其前身是BOOTP协议。DHCP协议由RFC 2131定义，采用客户端/服务器通信模式，由客户端（DHCP Client）向服务器（DHCP Server）提出配置申请，DHCP Server为网络上的每个设备动态分配IP地址、子网掩码、默认[网关](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E8%B7%AF%E7%94%B1%E5%99%A8.html "路由器")地址，域名服务器（[DNS](https://info.support.huawei.com/info-finder/encyclopedia/zh/DNS.html "DNS")）地址和其他相关配置参数，以便可以与其他[IP](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")网络通信。

目录

-   [为什么要使用DHCP？](https://info.support.huawei.com/info-finder/encyclopedia/zh/DHCP.html#content1)
-   [DHCP是怎么工作的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/DHCP.html#content2)
-   [DHCP使用场景](https://info.support.huawei.com/info-finder/encyclopedia/zh/DHCP.html#content3)

## 为什么要使用DHCP？

在[IP](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")网络中，每个连接Internet的设备都需要分配唯一的[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")。DHCP使网络管理员能从中心结点监控和分配IP地址。当某台计算机移到网络中的其它位置时，能自动收到新的IP地址。DHCP实现的自动化分配IP地址不仅降低了配置和部署设备的时间，同时也降低了发生配置错误的可能性。另外DHCP服务器可以管理多个网段的配置信息，当某个网段的配置发生变化时，管理员只需要更新DHCP服务器上的相关配置即可，实现了集中化管理。

总体来看，DHCP带来了如下优势：

-   准确的IP配置：IP地址配置参数必须准确，并且在处理“ 192.168.XXX.XXX”之类的输入时，很容易出错。另外印刷错误通常很难解决，使用DHCP服务器可以最大程度地降低这种风险。
-   减少IP地址冲突：每个连接的设备都必须有一个IP地址。但是，每个地址只能使用一次，重复的地址将导致无法连接一个或两个设备的冲突。当手动分配地址时，尤其是在存在大量仅定期连接的端点（例如移动设备）时，可能会发生这种情况。DHCP的使用可确保每个地址仅使用一次。
-   IP地址管理的自动化：如果没有DHCP，网络管理员将需要手动分配和撤销地址。跟踪哪个设备具有什么地址可能是徒劳的，因为几乎无法理解设备何时需要访问网络以及何时需要离开网络。DHCP允许将其自动化和集中化，因此网络专业人员可以从一个位置管理所有位置。
-   高效的变更管理：DHCP的使用时更改地址，范围或端点变得非常简单。例如，组织可能希望将其IP寻址方案从一个范围更改为另一个范围。DHCP服务器配置有新信息，该信息将传播到新端点。同样，如果升级并更换了网络设备，则不需要网络配置。

## DHCP是怎么工作的？

DHCP协议采用UDP作为传输协议，DHCP客户端使用的源端口号为68，目的端口号为67发送请求消息到DHCP服务器，DHCP服务器使用的源端口号为67，目的端口号为68回应应答消息给DHCP客户端。

只有跟DHCP客户端在同一个网段的DHCP服务器才能收到DHCP客户端广播的DHCP DISCOVER报文。当DHCP客户端与DHCP服务器不在同一个网段时，必须部署DHCP中继来转发DHCP客户端和DHCP服务器之间的DHCP报文。在DHCP客户端看来，DHCP中继就像DHCP服务器；在DHCP服务器看来，DHCP中继就像DHCP客户端。

**无中继场景时DHCP客户端首次接入网络的工作原理**

如下图所示，在没有部署DHCP中继的场景下，首次接入网络DHCP客户端与DHCP服务器的报文交互过程，该过程称为DHCP报文四步交互。

![无中继场景时DHCP客户端首次接入网络的报文交互示意图](https://download.huawei.com/mdl/image/download?uuid=0b437a2030c44296b3a93bd698a80f8c "无中继场景时DHCP客户端首次接入网络的报文交互示意图")  
无中继场景时DHCP客户端首次接入网络的报文交互示意图

第一步：发现阶段

首次接入网络的DHCP客户端不知道DHCP服务器的[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")，为了学习到DHCP服务器的IP地址，DHCP客户端以广播方式发送DHCP DISCOVER报文（目的IP地址为255.255.255.255）给同一网段内的所有设备（包括DHCP服务器或中继）。DHCP DISCOVER报文中携带了客户端的MAC地址（[chaddr字段](https://support.huawei.com/hedex/pages/EDOC1100087046AZJ0324D/10/EDOC1100087046AZJ0324D/10/resources/dc/dc_cfg_dhcp_6005.html#ZH-CN_CONCEPT_0176371535__c1)）、需要请求的参数列表选项（[Option55](https://support.huawei.com/hedex/pages/EDOC1100087046AZJ0324D/10/EDOC1100087046AZJ0324D/10/resources/dc/dc_cfg_dhcp_6005.html#ZH-CN_CONCEPT_0176371535__op55)）、广播标志位（[flags字段](https://support.huawei.com/hedex/pages/EDOC1100087046AZJ0324D/10/EDOC1100087046AZJ0324D/10/resources/dc/dc_cfg_dhcp_6005.html#ZH-CN_CONCEPT_0176371535__f1)）等信息。

第二步：提供阶段

与DHCP客户端位于同一网段的DHCP服务器都会接收到DHCP DISCOVER报文，DHCP服务器选择跟接收DHCP DISCOVER报文接口的IP地址处于同一网段的地址池，并且从中选择一个可用的IP地址，然后通过DHCP OFFER报文发送给DHCP客户端。

通常，DHCP服务器的地址池中会指定IP地址的[租期](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100087046&id=ZH-CN_CONCEPT_0176371534&lang=zh)，如果DHCP客户端发送的DHCP DISCOVER报文中携带了期望租期，服务器会将客户端请求的期望租期与其指定的租期进行比较，选择其中时间较短的租期分配给客户端。

DHCP服务器在地址池中为客户端分配IP地址的顺序如下：

1.  DHCP服务器上已配置的与客户端MAC地址静态绑定的IP地址。
2.  客户端发送的DHCP DISCOVER报文中[Option50](https://support.huawei.com/hedex/pages/EDOC1100087046AZJ0324D/10/EDOC1100087046AZJ0324D/10/resources/dc/dc_cfg_dhcp_6005.html#ZH-CN_CONCEPT_0176371535__op50)（请求IP地址选项）指定的地址。
3.  地址池内查找“Expired”状态的IP地址，即曾经分配给客户端的超过租期的IP地址。
4.  在地址池内随机查找一个“Idle”状态的IP地址。
5.  如果未找到可供分配的IP地址，则地址池依次自动回收超过租期的（“Expired”状态）和处于冲突状态（“Conflict”状态）的IP地址。回收后如果找到可用的IP地址，则进行分配；否则，DHCP客户端等待应答超时后，重新发送DHCP DISCOVER报文来申请IP地址。

设备支持在地址池中排除某些不能通过DHCP机制进行分配的IP地址。例如，客户端所在网段已经手工配置了地址为192.168.1.100/24的DNS服务器，DHCP服务器上配置的网段为192.168.1.0/24的地址池中需要将192.168.1.100的IP地址排除，不能通过DHCP分配此地址，否则，会造成地址冲突。

为了防止分配出去的IP地址跟网络中其他客户端的IP地址冲突，DHCP服务器在发送DHCP OFFER报文前通过发送源地址为DHCP服务器IP地址、目的地址为预分配出去IP地址的[ICMP](https://info.support.huawei.com/info-finder/encyclopedia/zh/ICMP.html "ICMP")  ECHO REQUEST报文对分配的IP地址进行地址冲突探测。如果在指定的时间内没有收到应答报文，表示网络中没有客户端使用这个IP地址，可以分配给客户端；如果指定时间内收到应答报文，表示网络中已经存在使用此IP地址的客户端，则把此地址列为冲突地址，然后等待重新接收到DHCP DISCOVER报文后按照前面介绍的选择IP地址的优先顺序重新选择可用的IP地址。

此阶段DHCP服务器分配给客户端的IP地址不一定是最终确定使用的IP地址，因为DHCP OFFER报文发送给客户端等待16秒后如果没有收到客户端的响应，此地址就可以继续分配给其他客户端。通过下面的选择阶段和确认阶段后才能最终确定客户端可以使用的IP地址。

第三步：选择阶段

如果有多个DHCP服务器向DHCP客户端回应DHCP OFFER报文，则DHCP客户端一般只接收第一个收到的DHCP OFFER报文，然后以广播方式发送DHCP REQUEST报文，该报文中包含客户端想选择的DHCP服务器标识符（即[Option54](https://support.huawei.com/hedex/pages/EDOC1100087046AZJ0324D/10/EDOC1100087046AZJ0324D/10/resources/dc/dc_cfg_dhcp_6005.html#ZH-CN_CONCEPT_0176371535__op54)）和客户端IP地址（即[Option50](https://support.huawei.com/hedex/pages/EDOC1100087046AZJ0324D/10/EDOC1100087046AZJ0324D/10/resources/dc/dc_cfg_dhcp_6005.html#ZH-CN_CONCEPT_0176371535__op50)，填充了接收的DHCP OFFER报文中yiaddr字段的IP地址）。

DHCP客户端广播发送DHCP REQUEST报文通知所有的DHCP服务器，它将选择某个DHCP服务器提供的IP地址，其他DHCP服务器可以重新将曾经分配给客户端的IP地址分配给其他客户端。

第四步：确认阶段

当DHCP服务器收到DHCP客户端发送的DHCP REQUEST报文后，DHCP服务器回应DHCP ACK报文，表示DHCP REQUEST报文中请求的IP地址（[Option50](https://support.huawei.com/hedex/pages/EDOC1100087046AZJ0324D/10/EDOC1100087046AZJ0324D/10/resources/dc/dc_cfg_dhcp_6005.html#ZH-CN_CONCEPT_0176371535__op50)填充的）分配给客户端使用。

DHCP客户端收到DHCP ACK报文，会广播发送[免费ARP](https://info.support.huawei.com/info-finder/encyclopedia/zh/ARP.html "ARP")报文，探测本网段是否有其他终端使用服务器分配的IP地址，如果在指定时间内没有收到回应，表示客户端可以使用此地址。如果收到了回应，说明有其他终端使用了此地址，客户端会向服务器发送DHCP DECLINE报文，并重新向服务器请求IP地址，同时，服务器会将此地址列为冲突地址。当服务器没有空闲地址可分配时，再选择冲突地址进行分配，尽量减少分配出去的地址冲突。

当DHCP服务器收到DHCP客户端发送的DHCP REQUEST报文后，如果DHCP服务器由于某些原因（例如协商出错或者由于发送REQUEST过慢导致服务器已经把此地址分配给其他客户端）无法分配DHCP REQUEST报文中[Option50](https://support.huawei.com/hedex/pages/EDOC1100087046AZJ0324D/10/EDOC1100087046AZJ0324D/10/resources/dc/dc_cfg_dhcp_6005.html#ZH-CN_CONCEPT_0176371535__op50)填充的IP地址，则发送DHCP NAK报文作为应答，通知DHCP客户端无法分配此IP地址。DHCP客户端需要重新发送DHCP DISCOVER报文来申请新的IP地址。

**有中继场景时DHCP客户端首次接入网络的工作原理**

有DHCP中继的场景中，首次接入网络的DHCP客户端和DHCP服务器的工作原理与**无中继场景时DHCP客户端首次接入网络的工作原理**相同。主要差异是DHCP中继在DHCP服务器和DHCP客户端之间转发DHCP报文，以保证DHCP服务器和DHCP客户端可以正常交互。下面仅针对DHCP中继的工作原理进行介绍。

如下图所示，在部署DHCP中继的场景下，首次接入网络DHCP客户端与DHCP服务器的报文交互过程。

![有中继场景时DHCP客户端首次接入网络的报文交互示意图](https://download.huawei.com/mdl/image/download?uuid=75c8e572300249d094ce4c11b14cec07 "有中继场景时DHCP客户端首次接入网络的报文交互示意图")  
有中继场景时DHCP客户端首次接入网络的报文交互示意图

第一步：发现阶段

DHCP中继接收到DHCP客户端广播发送的DHCP DISCOVER报文后，进行如下处理：

1.  检查DHCP报文中的hops字段，如果大于16，则丢弃DHCP报文；否则，将hops字段加1（表明经过一次DHCP中继），并继续下面的操作。
2.  检查DHCP报文中的giaddr字段。如果是0，将giaddr字段设置为接收DHCP DISCOVER报文的接口IP地址。如果不是0，则不修改该字段，继续下面的操作。
3.  将DHCP报文的目的IP地址改为DHCP服务器或下一跳中继的IP地址，源地址改为中继连接客户端的接口地址，通过[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")转发将DHCP报文单播发送到DHCP服务器或下一跳中继。

如果DHCP客户端与DHCP服务器之间存在多个DHCP中继，后面的中继接收到DHCP DISCOVER报文的处理流程同前面所述。

第二步：提供阶段

DHCP服务器接收到DHCP DISCOVER报文后，选择与报文中giaddr字段为同一网段的地址池，并为客户端分配IP地址等参数，然后向giaddr字段标识的DHCP中继单播发送DHCP OFFER报文。

DHCP中继收到DHCP OFFER报文后，会进行如下处理：

1.  检查报文中的giaddr字段，如果不是接口的地址，则丢弃该报文；否则，继续下面的操作。
2.  DHCP中继检查报文的广播标志位。如果广播标志位为1，则将DHCP OFFER报文广播发送给DHCP客户端；否则将DHCP OFFER报文单播发送给DHCP客户端。

第三步：选择阶段

中继接收到来自客户端的DHCP REQUEST报文的处理过程同无中继场景下的选择阶段。

第四步：确认阶段

中继接收到来自服务器的DHCP ACK报文的处理过程同无中继场景下的确认阶段。

**DHCP客户端重用曾经使用过的地址的工作原理**

DHCP客户端非首次接入网络时，可以重用曾经使用过的地址。如下图所示，DHCP客户端与DHCP服务器交互DHCP报文，以重新获取之前使用的IP地址等网络参数，该过程称为两步交互。

![DHCP客户端重用曾经使用过的IP地址的报文交互过程](https://download.huawei.com/mdl/image/download?uuid=cbbe05da53be4c61a03d582f8e6f7471 "DHCP客户端重用曾经使用过的IP地址的报文交互过程")  
DHCP客户端重用曾经使用过的IP地址的报文交互过程

第一步：选择阶段

客户端广播发送包含前一次分配的IP地址的DHCP REQUEST报文，报文中的Option50（请求的IP地址选项）字段填入曾经使用过的IP地址。

第二步：确认阶段

DHCP服务器收到DHCP REQUEST报文后，根据DHCP REQUEST报文中携带的MAC地址来查找有没有相应的租约记录，如果有则返回DHCP ACK报文，通知DHCP客户端可以继续使用这个IP地址。否则，保持沉默，等待客户端重新发送DHCP DISCOVER报文请求新的IP地址。

**DHCP客户端更新租期的工作原理**

DHCP服务器采用动态分配机制给客户端分配IP地址时，分配出去的IP地址有租期限制。DHCP客户端向服务器申请地址时可以携带期望租期，服务器在分配租期时把客户端期望租期和地址池中租期配置比较，分配其中一个较短的租期给客户端。租期到期或者客户端下线释放地址后，服务器会收回该IP地址，收回的IP地址可以继续分配给其他客户端使用。这种机制可以提高IP地址的利用率，避免客户端下线后IP地址继续被占用。如果DHCP客户端希望继续使用该地址，需要更新IP地址的租期（如延长IP地址租期）。

DHCP客户端更新租期的过程如下图所示。

![DHCP客户端更新租期示意图](https://download.huawei.com/mdl/image/download?uuid=3ce2b460c2fa4636b1a8bc641b021a77 "DHCP客户端更新租期示意图")  
DHCP客户端更新租期示意图

1.  当租期达到50%（T1）时，DHCP客户端会自动以单播的方式向DHCP服务器发送DHCP REQUEST报文，请求更新IP地址租期。如果收到DHCP服务器回应的DHCP ACK报文，则租期更新成功（即租期从0开始计算）；如果收到DHCP NAK报文，则重新发送DHCP DISCOVER报文请求新的IP地址。
2.  当租期达到87.5%（T2）时，如果仍未收到DHCP服务器的应答，DHCP客户端会自动以广播的方式向DHCP服务器发送DHCP REQUEST报文，请求更新IP地址租期。如果收到DHCP服务器回应的DHCP ACK报文，则租期更新成功（即租期从0开始计算）；如果收到DHCP NAK报文，则重新发送DHCP DISCOVER报文请求新的IP地址。
3.  如果租期时间到时都没有收到服务器的回应，客户端停止使用此IP地址，重新发送DHCP DISCOVER报文请求新的IP地址。

客户端在租期时间到之前，如果用户不想使用分配的IP地址（例如客户端网络位置需要变更），会触发DHCP客户端向DHCP服务器发送DHCP RELEASE报文，通知DHCP服务器释放IP地址的租期。DHCP服务器会保留这个DHCP客户端的配置信息，将IP地址列为曾经分配过的IP地址中，以便后续重新分配给该客户端或其他客户端。客户端可以通过发送DHCP INFORM报文向服务器请求更新配置信息。

如下图所示，部署DHCP中继时，更新租期的过程与上述过程相似。

![客户端通过DHCP中继更新租期示意图](https://download.huawei.com/mdl/image/download?uuid=1a75cbe38bd54506b6b188ba795c7dc9 "客户端通过DHCP中继更新租期示意图")  
客户端通过DHCP中继更新租期示意图

## DHCP使用场景

DHCP提供了两种地址分配机制，网络管理员可以根据网络需求为不同的主机选择不同的分配策略。

-   动态分配机制：通过DHCP为主机分配一个有使用期限的[IP地址](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")。
    
    DHCP使用了租期的概念，或称为设备IP地址的有效期。租用时间是不定的，主要取决于用户在某地连接Internet需要多久，这种分配机制适用于主机需要临时接入网络或者空闲地址数小于网络主机总数且主机不需要永久连接网络的场景。
    
-   静态分配机制：网络管理员通过DHCP为指定的主机分配固定的IP地址。
    
    相比手工静态配置IP地址，通过DHCP方式静态分配机制避免人工配置发生错误，方便管理员统一维护管理。
    

参考资源

1[DHCP配置（NetEngine AR路由器）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100087046&id=ZH-CN_CONCEPT_0176371515&lang=zh)

2[DHCP配置（CloudEngine数据中心交换机）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100195094&id=ZH-CN_TASK_0275773045&lang=zh)

3[DHCP配置（CloudEngine S系列交换机）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100364141&id=ZH-CN_CONCEPT_0176371515)

4[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/DHCP.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMTE3MjUwMTRdfQ==
-->