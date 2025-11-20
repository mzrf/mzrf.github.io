# 什么是MU-MIMO？

MU-MIMO（Multi-User Multiple-Input Multiple-Output）即多用户MIMO，允许1个[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")同时和多个终端通信，充分利用空间资源，提升无线吞吐量，是无线通信领域的一种重要的多用户技术。MU-MIMO主要用于蜂窝网络和[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")（[WiFi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")）网络。

目录

-   [MU-MIMO和MIMO的区别是什么？](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html#content1)
-   [MU-MIMO有什么价值？](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html#content2)
-   [MU-MIMO是如何工作的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html#content3)
-   [哪些Wi-Fi设备支持MU-MIMO？](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html#content4)

## MU-MIMO和MIMO的区别是什么？

介绍MU-MIMO之前，不得不先介绍下[MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MIMO.html "MIMO")技术。MIMO技术可简单理解为将空间资源进行分割，经过多根天线进行同步传送。

![MIMO系统](https://download.huawei.com/mdl/image/download?uuid=757a80371b9540fab1248b80700756fa "MIMO系统")  
MIMO系统

MIMO带来的好处是增加单一设备的数据传输速度，同时不占用额外的频谱资源。可以说，无线传输的理论速率从802.11g时代的54Mbps，到802.11n时代的300Mbps，甚至是更高的600Mbps，MIMO技术功不可没。

在MIMO系统中，同一时间[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")仅能和1个终端通信，所以也称为SU-MIMO（Single-User Multiple-Input Multiple-Output），即单用户MIMO。当终端的天线数和AP的天线数相同时，可以充分使用AP的空间资源。但在实际应用中，通常AP和终端的收发天线数是不对等的，AP多是3根或者4根天线，甚至更多，但是终端（比如手机）通常只有1-2根天线，这会造成AP一部分空间资源的浪费。举例来说，1台4×4（4天线，4发4收）的[Wi-Fi 5](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")  AP的理论传输速率可达1.732Gbps，当它与1×1（1天线）手机通信时，最高理论传输速率仅为1/4，即433Mbps，同一时间其余3根天线闲置，则1.3Gbps的容量都会被闲置。

而MU-MIMO技术使AP同一时间和多个终端进行通信，这样就能充分利用AP的总容量。

![MU-MIMO vs MIMO](https://download.huawei.com/mdl/image/download?uuid=dad303b10d2e4d1eac0f171639aa48a2 "MU-MIMO vs MIMO")  
MU-MIMO vs MIMO

不难看出，MU-MIMO和SU-MIMO的关键差异，就在于MU-MIMO在同一时间能和多个终端通信，有效利用了空间资源，成倍提升了吞吐量。

MIMO通常用_M_×_N_来表示_M_个发送天线和_N_个接收天线，而MU-MIMO实现了多用户通信，所以在MIMO基础上增加了MU（多用户）数量的指标项，一般用_M_×_N:U_表示。其中的_M_×_N_仍是指MIMO的天线数，_U_则表示MU数量，即同时通信的终端数量。例如一个MU-MIMO的规格为_8_×_8_:_8_，冒号后的_8_就表示同时通信的终端数量最大为8个。

## MU-MIMO有什么价值？

MU-MIMO主要用于用户分布密集、多用户大流量并发、终端位置相对固定的场景，例如办公场景、会议中心、电子教学等，能为无线网络带来较大的收益。

**提升网络吞吐量和频谱利用率**

MU-MIMO可有效提升无线网络的吞吐量。使用MU-MIMO的无线网络吞吐量通常比SU-MIMO增加2-3倍，[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")的天线数越多，空间资源越多，提升的吞吐量也越多。

**满足视频等应用的大流量需求**

MU-MIMO允许多个终端并发传输数据，让无线网络中数据传输的效率更高，降低了终端在时序上的等待时间，因此可以更好地满足视频、音频和其它大流量、[低时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")应用的需求。

**传统[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")终端也能收益**

由于MU-MIMO带来的整体传输效率的提升，使得无线网络有更多的空闲时间或容量来服务传统的Wi-Fi终端（仅支持SU-MIMO），也就是说，传统Wi-Fi终端的应用体验也能随之提升。

## MU-MIMO是如何工作的？

MU-MIMO要实现和多个终端同时通信，需要结合[波束成形](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.html "波束成形")（[beamforming](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.html "波束成形")）技术实现。首先[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")测量出每根天线到每个终端的信道特征，然后AP根据信道特征，将要发送的数据进行预编码计算，将预编码后信号在每根天线上发出，结果就是所有天线的数据到达每个终端时，仅包含本终端的数据，消除其他终端的数据，就像是形成了指向每个终端的定向波束。

为了便于理解，通过一个2x2的MU-MIMO模型介绍下整体的工作过程，当然实际的计算和处理过程更为复杂。

![MU-MIMO的工作原理](https://download.huawei.com/mdl/image/download?uuid=557810d641954048aea91c144b717d92 "MU-MIMO的工作原理")  
MU-MIMO的工作原理

假设发射端在每根天线发射的数据分别为X1和X2，经过空间传输的衰减和干扰，在接收端的数据变为了Y1和Y2，空间中的4条传输路径h就是数据变化的系数，用于表示无线信道特征。所以只要h已知，就可以计算出接收端收到的数据Y。

![MIMO信号计算](https://download.huawei.com/mdl/image/download?uuid=8ca12a8518614e77afb49460ea4d1135 "MIMO信号计算")  
MIMO信号计算

如果接收端是同一个终端，也就是SU-MIMO，则发送端只需要发送一个收发双方已知的标准数据，接收端就可以根据收到的Y和已知的X计算出h。为了让接收端直接收到要发送的原始数据，则只要将原始数据代入Y，根据已知的h反向计算就能知道应该发送的数据X是什么，这就是预编码的过程。

但对于MU-MIMO而言，接收端包含多个终端，终端只知道自己收到的Y，不知道其他终端收到的Y，也就无法在接收端计算出h，所以只能由发送端进行计算。发送端需要通过信道测量完成h的计算，过程是将数据X发送给各终端，各终端收到后回复Y给发送端，发送端已知X和Y，计算出h。发送端再根据h对发送给多个终端的数据进行预编码，实现一次发送多个终端的数据。

当然无线空间的信道特征是一直变化的，所以在每次发送数据前都需要计算h，只是计算和发送数据的间隔极短，可以忽略信道变化对收发数据的影响。

MU-MIMO根据传输方向可以分为DL MU-MIMO和UL MU-MIMO，DL是指下行链路（Down Link），UL是指上行链路（Up Link）。DL MU-MIMO是指AP同一时间给多个终端发送数据，UL MU-MIMO是指AP同一时间接收多个终端的数据。

## 哪些Wi-Fi设备支持MU-MIMO？

在[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")标准演进中，[802.11ac](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")  Wave2（[Wi-Fi 5](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")）引入了MU-MIMO技术，具体而言是指DL MU-MIMO，最大允许[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")同时向4个终端发送数据。而到了[802.11ax](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")（[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")），又引入了UL MU-MIMO技术，解决了上行多用户传输的瓶颈问题，同时还将允许AP同时通信的最大终端数扩大到了8个，进一步提升了用户密集场景的传输效率。所以只要Wi-Fi设备支持Wi-Fi 5，就支持DL MU-MIMO，而支持Wi-Fi 6的话，则支持双向的MU-MIMO。

需要注意的是，MU-MIMO要生效，需要通信双方的AP和终端都支持MU-MIMO。如果网络中存在不支持MU-MIMO的终端，则AP和该类终端通信时，仍使用SU-MIMO，和支持MU-MIMO的终端通信时，继续使用MU-MIMO。

产品相关介绍请参见：[AirEngine Wi-Fi 6产品](https://e.huawei.com/cn/products/enterprise-networking/wlan/wifi-6/new-products-launch)。

参考资源

1[阅读eBook：Wi-Fi 6](https://support.huawei.com/enterprise/zh/doc/EDOC1100195173)

2[华为WLAN 多用户性能提升技术白皮书](https://e.huawei.com/cn/material/networking/campus-network/wlan/f1f62e463bb640f4bde0d46bfd4fca6e)

3[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ0MzY5MTIxM119
-->