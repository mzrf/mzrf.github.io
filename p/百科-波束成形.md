# 什么是波束成形？

波束成形技术是将信号以一种能量集中和定向方式发送给无线终端的技术，能全面改善无线终端接收的信号质量，并提升吞吐量。在[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")（[WiFi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")）标准中，从Wi-Fi 4（802.11n）开始引入该技术。

目录

-   [Wi-Fi为什么要用波束成形？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.html#content1)
-   [波束成形是如何工作的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.html#content2)
-   [显式波束成形](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.html#content3)
-   [隐式波束成形](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.html#content4)

## Wi-Fi为什么要用波束成形？

[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")标准一直致力于提升无线的传输速率，尤其是从Wi-Fi 4（802.11n）开始引入了[MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MIMO.html "MIMO")和波束成形技术，让传输速率提升到了数百兆，提升了1个量级。

MIMO技术通过多天线传输，带来传输速率的成倍增长。但在实际应用中STA（无线终端）往往只有1到2个天线，这使得STA发送和接收信号的收益有所差异。STA向[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")发送信号时，AP可以利用自己的多天线系统增强接收增益，获得更好的信号强度；AP向STA发送信号时，如果仅使用对应数量的天线发送信号，则无法利用多天线带来的增益。为了解决这一问题，通过引入波束成形技术，可以增强STA接收到的信号强度，从而使AP和STA可以协商出更高的传输速率。

为了充分利用AP的多天线资源，[Wi-Fi 5](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")（[802.11ac](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")）又引入了[MU-MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html "MU-MIMO")技术，使AP可以同时向多个STA发送信号，有效提升了无线的传输效率。MU-MIMO也需要波束成形技术，波束成形使AP的多天线信号叠加后，让各STA仅收到自己的信号，消除其他STA的信号，避免干扰。[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")（[802.11ax](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")）在Wi-Fi 5的技术上进一步增加了MU-MIMO的多用户数量，这些都离不开波束成形技术的使用。

## 波束成形是如何工作的？

波束成形从字面理解就是塑造波束的形状，那么如何塑造出波束的形状呢？以光束为例，用一个手电筒打出一道光束，光束的形状是固定的。如果在平行方向增加一个手电筒，则会发现两道光束叠加后，光束亮度增加，光束形状发生了改变。如果继续增加手电筒的数量，光束的亮度继续增加，叠加后的光束形状也继续变化。在多个手电筒的情况下，改变手电筒的开关状态或调整发光的强弱，也会影响光束的形状。

对于无线通信，天线就相当于手电筒，无线信号的波束就相当于光束，通过多个天线，控制每个天线发射的信号，就可以改变无线信号的波束形状。

在多天线系统中，如果不同天线传输的信号在到达某一位置时存在两条衰减相等的波束，且两条波束相位相反，就可能会出现空间空洞。波束成形技术可以通过预先补偿发射天线的相位，让两条波束进行叠加以实现信号增强的效果。

![波束成形的原理](https://download.huawei.com/mdl/image/download?uuid=42ba17cb0861481a8bd543a5c305804e "波束成形的原理")  
波束成形的原理

波束成形怎么知道该如何调整发射天线的信号呢？这是通过检测信道状态信息CSI（Channel State Information）来获取并计算出调整参数的。按照CSI获取方式的不同，波束成形可以分为显式波束成形（Explicit beamforming）和隐式波束成形（Implicit beamforming）。

## 显式波束成形

显式波束成形是一种需要STA反馈信道信息的波束成形方式。显式波束成形信道信息的探测和反馈流程如下：

![显式波束成型](https://download.huawei.com/mdl/image/download?uuid=ce4ca84ccf474ba9a92d1f94fb6210bb "显式波束成型")  
显式波束成型

1.  [AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")向STA发送探测数据（Training Symbol）。在802.11n标准中，AP发送探测数据包括空数据包（NDP）和交错前导码两种方式；[802.11ac](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")标准开始则直接使用NDP的方式。
    -   NDP是一种没有数据的空帧，其没有负荷。AP向STA发送NDP探测通告和空数据包，STA收到探测通告和空数据包后进行信道信息反馈。
    -   交错前导码是利用发送的带有负荷的帧实现探测，这个帧会承载一个MAC帧和探测信道。
2.  STA向AP反馈信道信息。
    
    在802.11n标准中，STA的信道信息反馈有三种方式：
    
    -   CSI方式：STA将原始的信道信息直接发送给AP，由AP计算最终的波束成形权重值。
    -   非压缩波束成形权重值：STA收到探测后，由STA计算出波束成形权重值后反馈给AP。这种方式会增加系统开销，因此有了压缩波束成形权重值。
    -   压缩波束成形权重值：同样是由STA计算出波束成形权重值后反馈给AP，并且通过一些方法降低了系统开销。
    
    802.11ac标准开始，STA采用压缩波束成形权重值的方式反馈信道信息。
    
3.  AP根据STA反馈或自己计算的权重信息进行波束成形，多径信号在STA处汇聚，形成增益。

## 隐式波束成形

隐式波束成形是由Beamformer计算发送方向信道信息的波束成形方式，其利用了时分双工（TDD，Time Division Duplexing）系统的互易性（即认为同频段的上下行的信道状态信息是相等的），将Beamformee反馈的上行接收方向信道信息直接应用于下行发送方向，进行波束成形。由于隐式波束成形具体实现的复杂性，从[802.11ac](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")协议开始已经明确不再支持隐式波束成形且业界也基本无厂商实现该方式波束成形，这里我们也不再做更详细的描述。

参考资源

1[阅读eBook：Wi-Fi 6](https://support.huawei.com/enterprise/zh/doc/EDOC1100195173)

2[华为WLAN 多用户性能提升技术白皮书](https://e.huawei.com/cn/material/networking/campus-network/wlan/f1f62e463bb640f4bde0d46bfd4fca6e)

3[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY3MzU2NjEzNF19
-->