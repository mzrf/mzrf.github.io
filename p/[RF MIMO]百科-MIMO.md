# 什么是MIMO？

MIMO（Multiple-Input Multiple-Output）是指在无线通信领域使用多天线发送和接收信号的技术。MIMO技术主要应用在[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")（[WiFi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")）领域和移动通信领域，可以有效提高系统容量、覆盖范围和[信噪比](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BF%A1%E5%99%AA%E6%AF%94.html "信噪比")。通常讲的_M_×_N_  MIMO是指发送端有_M_个天线，接收端有_N_个天线。

目录

-   [从SISO到MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MIMO.html#content1)
-   [MIMO有哪些类型？](https://info.support.huawei.com/info-finder/encyclopedia/zh/MIMO.html#content2)
-   [Wi-Fi中的MIMO是如何工作的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/MIMO.html#content3)
-   [什么是M×N MIMO？](https://info.support.huawei.com/info-finder/encyclopedia/zh/MIMO.html#content4)

## 从SISO到MIMO

**SISO（Single-Input Single-Output）**

在介绍MIMO之前，需要先介绍一下什么是SISO。从字面上理解，SISO 就是单发单收，是一种单输入单输出系统，发射天线和接收天线之间的路径是唯一的，传输的是1路信号。在无线系统中，我们把每路信号定义为1个空间流（Spatial Stream）。

![SISO示意图](https://download.huawei.com/mdl/image/download?uuid=7adc8371cc0442c4a031e6e26271537e "SISO示意图")  
SISO示意图

由于发射天线和接收天线之间的路径是唯一的，这样的传输系统是不可靠的，而且传输速率也会受到限制。

**SIMO（Single-Input Multiple-Output）**

为了改变这一局面，在终端处增加1个天线，使得接收端可以同时接收到2路信号，也就是单发多收。这样的传输系统就是单输入多输出，即SIMO。

![SIMO示意图](https://download.huawei.com/mdl/image/download?uuid=0cb6a47266be49bb94e05bbd7d157391 "SIMO示意图")  
SIMO示意图

虽然有2路信号，但是这2路信号是从同一个发射天线发出的，所以发送的数据是相同的，传输的仍然只有1路信号。这样，当某一路信号有部分丢失也没关系，只要终端能从另一路信号中收到完整数据即可。虽然最大容量还是1条路径，但是可靠性却提高了1倍。这种方式叫作接收分集。

**MISO（Multiple-Input Single-Output）**

我们换一个思路，如果把发射天线增加到2个，接收天线还是维持1个，会有什么样的结果呢？

![MISO示意图](https://download.huawei.com/mdl/image/download?uuid=b58c367450a14f7291c86ce2dd87f894 "MISO示意图")  
MISO示意图

因为接收天线只有1个，所以这两路最终还是要合成1路，这就导致发射天线只能发送相同的数据，传输的还是只有1路信号。这样做其实可以达到和SIMO相同的效果，这种传输系统叫作多输入单输出，即MISO。这种方式也叫发射分集。

**MIMO**

如果收发天线同时增加为2个，那么是不是就可以实现独立发送2路信号、速率翻倍了呢？答案是肯定的，因为从前文对SIMO和MISO的分析来看，传输容量取决于收、发双方的天线个数。而这种多收多发的传输系统就是MIMO。

![MIMO示意图](https://download.huawei.com/mdl/image/download?uuid=89beae5fa14f472d9a62a80871210e81 "MIMO示意图")  
MIMO示意图

MIMO 技术允许多个天线同时发送和接收多个信号，并能够区分发往或来自不同空间方位的信号。通过空分复用和空间分集等技术，在不增加占用带宽的情况下，提高系统容量、覆盖范围和[信噪比](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BF%A1%E5%99%AA%E6%AF%94.html "信噪比")。

## MIMO有哪些类型？

MIMO是利用多天线收发信号的技术，最开始用于对单用户的数据传输。但随着多用户传输技术的发展，在MIMO的基础上出现了多种多用户类型的MIMO技术，为了便于区分，将单用户类型的MIMO称为SU-MIMO（Single-user MIMO）。多用户类型的MIMO技术则主要包含以下几种。

**[MU-MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html "MU-MIMO")（Multi-user MIMO）**：允许发射端同时和多个用户传输数据。[Wi-Fi 5](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")标准开始支持4用户的MU-MIMO，[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")标准将用户数增加到了8个。

**CO-MIMO（Cooperative MIMO）**：将多个无线设备组成虚拟的多天线系统，实现相邻的发射设备同时和多个用户传输数据。

**Massive MIMO**：大规模天线技术，极大提升了天线的数量，传统MIMO一般使用2~8天线，而Massive MIMO则可达到64/128/256个天线。可大幅提高系统容量和传输效率，是5G移动通信的关键技术。

从广义上讲，多用户类型的MIMO技术都可以归为MIMO技术，但我们提到MIMO时，通常是指传统的MIMO概念，即SU-MIMO。

## Wi-Fi中的MIMO是如何工作的？

在[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")领域从Wi-Fi 4（802.11n）标准开始引入了MIMO技术。MIMO主要使用了两种关键技术：空间分集和空分复用。不管是分集技术还是复用技术，都是把一路数据变成多路数据的技术，可以归为空时编码技术。

**空间分集**

空间分集技术的思路是制作同一个数据流的不同版本，分别在不同的天线进行编码、调制，然后发送。这个数据流可以是原来要发送的数据流，也可以是原始数据流经过一定的数学变换后形成的新数据流。接收机利用空间均衡器分离接收信号，然后解调、解码，将同一数据流的不同接收信号合并，恢复出原始信号。空间分集技术可以更可靠地传输数据。

Wi-Fi 4标准引入的[波束成形](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.html "波束成形")（[Beamforming](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.html "波束成形")）技术也可以认为是一种分集技术。波束成形需要先检测信道状态，对各天线发送的信号进行预编码，使信号在接收端方向叠加增强。波束成形能够增加信号传输距离，提高接收端收到的信号质量。

![空间分集技术](https://download.huawei.com/mdl/image/download?uuid=85efb4c672ef483eb5e1382195e62959 "空间分集技术")  
空间分集技术

空间分集有效提升了数据传输的可靠性，适用于传输距离长，速率要求不高的场景。

**空分复用**

空分复用技术是指将需要传送的数据分为多个数据流，分别通过不同的天线进行编码、调制，然后进行传输，从而提高系统的传输速率。天线之间相互独立，一个天线相当于一个独立的信道，接收机利用空间均衡器分离接收信号，然后解调、解码，将几个数据流合并，恢复出原始信号。

![空分复用技术](https://download.huawei.com/mdl/image/download?uuid=0695f20f45ae491f9854a64dae718d74 "空分复用技术")  
空分复用技术

空分复用有效提升了数据传输的速率，适用于传输距离短，速率要求高的场景。

## 什么是M×N MIMO？

在[WLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html "WLAN")产品的规格中，通常会看到一个指标项_M_×_N_  MIMO，也有写作_M_T_N_R的，这个指标项有什么含义呢？其实是用来表示MIMO的天线数，_M_表示发送端的天线数，_N_表示接收端的天线数。例如4×3 MIMO表示4根天线发送，3根天线接收。

市面上多数的家用[无线路由器](https://info.support.huawei.com/info-finder/encyclopedia/zh/Wi-Fi%E8%B7%AF%E7%94%B1%E5%99%A8.html "Wi-Fi路由器")都可以看到数根天线，1根天线往往能够支持收和发，所以可以根据天线的数量简单判断，天线的数量就是M和N的值。例如一台有着4根天线的无线路由器，可以认为是4x4 MIMO，当然具体还要以产品规格为准。天线数越多，意味着性能越高，价格也就越贵。

在企业级的[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")产品中，有着更多的天线数，能够为企业提供更加快速和可靠的无线网络。例如华为的企业级[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")  AP产品，旗舰款AirEngine 8760-X1-PRO，2.4G频段支持4x4 MIMO，5G频段支持12x12 MIMO，整机的天线数有16个之多，让速率达到10.75Gbps，为用户带来光纤般的无线体验。

在一个MIMO系统中，如果收发天线数量不相等，那么能够传输的空间流数小于或等于收/发端中更小的天线数。例如，4×4（4T4R）的MIMO系统可以传输4个或者更少的空间流，而3×2（3T2R）的MIMO系统可以传输2个或者1个空间流。

在实际应用中，AP往往具有较多的天线数，从4天线到16天线不等，但是终端（比如手机）通常只有1-2根天线。即使天线技术在不断进步，但受限于终端产品的体积大小，即使再容纳1-2根天线，也远小于AP的天线个数，这就意味着可以传输的空间流数量受限于终端，导致无法充分享受到空间流数增加带来的速率成倍增加，造成AP上天线资源的浪费。幸运的是多用户类型的MIMO技术出现并解决了这一问题，例如[MU-MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html "MU-MIMO")可以让一个AP同时和多个终端传输信号，多个终端的天线总数和AP的天线数对等，让AP的能力得到充分的发挥。

参考资源

1[阅读eBook：Wi-Fi 6](https://support.huawei.com/enterprise/zh/doc/EDOC1100195173)

2[华为WLAN 多用户性能提升技术白皮书](https://e.huawei.com/cn/material/networking/campus-network/wlan/f1f62e463bb640f4bde0d46bfd4fca6e)

3[了解华为AirEngine Wi-Fi 6产品](https://e.huawei.com/cn/products/enterprise-networking/wlan/wifi-6/new-products-launch)

4[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/MIMO.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY2NTI5NzM4Ml19
-->