# 什么是智能天线？

智能天线是指使用多个天线组成天线阵列，通过智能算法计算出最佳的天线组合，使各天线发射的信号在信号接收端叠加增强，从而增加信号覆盖距离，提高传输速率。智能天线可通过波束成型和天线阵列两种技术实现，而将两种技术相结合，则能够发挥两种技术的优势，从而达到更好的效果。

目录

-   [为什么需要智能天线](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%99%BA%E8%83%BD%E5%A4%A9%E7%BA%BF.html#content1)
-   [智能天线是如何工作的](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%99%BA%E8%83%BD%E5%A4%A9%E7%BA%BF.html#content2)
-   [智能天线的应用](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%99%BA%E8%83%BD%E5%A4%A9%E7%BA%BF.html#content3)

## 为什么需要智能天线

### 普通天线存在哪些问题

[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")（[WiFi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")）标准已演进到了第7代的[Wi-Fi 7](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+7.html "WiFi 7")（[802.11be](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+7.html "WiFi 7")），Wi-Fi 7在理论速率超过23Gbit/s，但在实际使用中，往往无法给用户带来超高的速率。这是因为在无线通信中，用户最终体验到的速率不仅仅由Wi-Fi标准决定，还受无线环境中的各种干扰和障碍物的影响。

为了提升用户最终的体验速率，需要增加[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")的覆盖范围来提高信号质量，并减少信号间的干扰，而天线作为无线通信的核心组件，决定了发射信号的波束，影响着AP的覆盖范围。天线根据其在平面上的方向性，分为全向天线和定向天线。在实际的Wi-Fi网络环境中，定向天线主要用于高密和回传场景，其他多数场景下AP都使用普通全向天线。有3个较为突出的难点需要解决：

-   **边缘覆盖**：普通全向天线的增益有限，对于近距离用户可以提供较好的体验，对于中远距离接近覆盖边缘的用户则无法提供服务或者只能提供较低速率的体验。
-   **跨障碍物覆盖**：实际环境中不可能空无一物，往往存在诸如木板、玻璃、墙体等材质的障碍物。当天线和用户中间存在障碍物遮挡时，无线信号穿过障碍物会有不同程度衰减，导致用户体验变差。
-   **高密场景覆盖**：在用户分布密集的环境中，多用户并发会导致空间内的干扰大大增加，即使[Wi-Fi 5](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")和[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")相继引入了[MU-MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html "MU-MIMO")和[OFDMA](https://info.support.huawei.com/info-finder/encyclopedia/zh/OFDMA.html "OFDMA")等多用户技术，但对接近覆盖边缘的用户体验提升并不明显。

### 智能天线对比普通天线有哪些好处

智能天线可以有效改善边缘覆盖、跨障碍物覆盖、高密场景覆盖中的用户体验。和普通天线对比，智能天线有如下优势：

-   **覆盖距离提升：**相同位置的用户信号强度增强，用户体验速率提升；相同信号强度要求下，可以使用更少的AP，节约客户投资成本。
-   **跨障碍物覆盖体验提升：**可灵活调整天线组合，在障碍物方向上增强信号强度，经过相同的衰减后，用户体验速率提升；对于无法穿透的障碍物，可调整天线组合的方向，利用无线信号的反射、绕射等多径方式绕过障碍物，能够为用户提供服务。
-   **高密场景下降低干扰影响：**可根据用户的位置调整信号波束的方向，降低不同方向用户间的干扰，从而提升用户的体验速率。

## 智能天线是如何工作的

智能天线可通过波束成型和天线阵列两种技术实现，两种技术都是利用多天线的组合来改善发射信号的波束，从而改善无线用户的体验。而将两种技术相结合，则能够同时发挥两种技术的优势，从而达到更好的效果。

### 波束成型技术

波束成型（[Beamforming](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.html "波束成形")）也称为[TxBF](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.html "波束成形")，是将信号以一种能量集中和定向方式发送给客户端的技术，能全面改善客户端接收的信号质量，并提升吞吐量。波束成型从[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")  4（802.11n）标准开始支持，使用多根普通天线即可实现。

在多天线系统中，如果不同天线传输的信号在到达某一位置时存在两条衰减相等的波束，且两条波束相位相反，就可能会出现信号能量零点。波束成型技术可以通过预先补偿天线发射信号的相位，让两条波束进行相干叠加 ，提升用户的接收信号强度，以改善用户体验。

![波束成型提升用户接收信号强度](https://download.huawei.com/mdl/image/download?uuid=ce42ef88c9364d0a99b73b96a30fa5f6 "波束成型提升用户接收信号强度")  
波束成型提升用户接收信号强度

### 天线阵列技术

天线阵列是一种波束切换技术，由多个小天线组成天线阵列。每个小天线由数个天线振子组成，天线振子可以独立开关，从而让小天线既可做全向天线，也可以做定向天线。小天线的组合方式与小天线本身的增益、极化方式、方向图等都有关系，所以小天线和其天线振子的数量决定了最终形成的波束的数量。例如2.4G频段共有4个天线，每个天线有4个振子，则共有16个振子，每个振子的状态有开和关两种，则共有216种天线组合。

![天线阵列和振子](https://download.huawei.com/mdl/image/download?uuid=ead5fcf53dad49cba9a015755ea9bc0c "天线阵列和振子")  
天线阵列和振子

天线阵列通过智能算法能够选择不同的天线组合进行信号的发射和接收，形成不同的信号辐射方向，为处于不同位置的用户选出最佳的天线组合发射和接收信号，形成波束，从而提升用户的接收信号强度，以改善用户体验。

![天线阵列通过智能算法切换波束](https://download.huawei.com/mdl/image/download?uuid=f384d2d7028a41f790892ab4fa412317 "天线阵列通过智能算法切换波束")  
天线阵列通过智能算法切换波束

### 波束成型和天线阵列组合

天线阵列可以实现多种天线组合，远多于普通天线的单一组合。华为的智能天线算法先根据终端位置选择出最佳的天线组合，再进一步利用波束成型技术对波束优化。这种组合比单独使用天线阵列有更好的波束，比单独使用波束成型有更好的方向性，能够进一步增强用户的接收信号强度，抑制干扰，提升用户速率体验。

![波束成型和天线阵列组合效果](https://download.huawei.com/mdl/image/download?uuid=4ed37ca88b254392987dd2dbbd112720 "波束成型和天线阵列组合效果")  
波束成型和天线阵列组合效果

华为[Wi-Fi 6](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html "WiFi 6")、[Wi-Fi 7](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+7.html "WiFi 7")  [AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")均支持智能天线。更多产品相关介绍请参见：[AirEngine Wi-Fi产品](https://e.huawei.com/cn/products/enterprise-networking/wlan/wifi-6/new-products-launch)。

### 动态变焦

随着技术的演进以及无线网络环境的不断变化，华为智能天线开始从聚焦水平面调控转向垂直面的调控，从增强边缘覆盖演进到降低干扰，以灵活适应不同业务的需要。这种新的智能天线技术被称为动态变焦智能天线技术，华为在部分新产品中支持该技术。

动态变焦智能天线支持切换全向和高密两种覆盖模式，不同模式下的波束宽度和覆盖半径有所差异。在人群集中的高密接入场景中，终端在一个比较小的范围内大量存在，将天线切换到高密模式，信号覆盖范围收缩，天线能量在垂直方向集中，从而增大了此范围内的信号强度，并降低其他区域的能量泄露和干扰。对于人群分散需要广覆盖的场景，将天线切换到全向模式，扩大覆盖范围能够保证更大范围内用户的使用体验。

除了上述根据用户分布情况选择不同模式外，全向和高密模式也可以根据网络中AP的部署间距动态自适应切换。如[图1-6](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%99%BA%E8%83%BD%E5%A4%A9%E7%BA%BF.html#fig940472211356)所示，在AP部署密度较低、间距较大时，天线自动切换为全向模式保证覆盖范围；在AP密集部署、间距较小时，自动切换为高密模式降低AP间的自组网干扰。

![动态变焦智能天线工作模式](https://download.huawei.com/mdl/image/download?uuid=c9174a5a6ce14ac3a0c5cf5fd5ce994d "动态变焦智能天线工作模式")  
动态变焦智能天线工作模式

## 智能天线的应用

### 中远距离覆盖增强场景

在开放的办公区内，无障碍物遮挡，当用户持终端远离[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")，距离AP较远时，智能天线算法会根据终端的位置，选择最合适的定向波束发送数据，取代全向波束。利用定向波束的高增益特性提升对中远距离用户的覆盖能力，实现边缘用户的覆盖强化。

![中远距离覆盖增强场景](https://download.huawei.com/mdl/image/download?uuid=7aa02cdbfa014aebaef9cc700e1b971f "中远距离覆盖增强场景")  
中远距离覆盖增强场景

### 复杂无线环境跨障碍物场景

办公区内存在玻璃隔断、半隔断等障碍物时，例如隔出的会议室，半遮挡的茶水间，智能天线也能提升AP的覆盖效果。对于需要穿透墙体的场景，由于定向波束的高增益，从而具有明显的穿透优势；对于环境中存在无法穿越的障碍物遮挡，智能天线可以选择其他定向波束进行反射、绕射等多径方式绕过障碍物，避免信号产生明显的衰减。

![复杂无线环境跨障碍物场景](https://download.huawei.com/mdl/image/download?uuid=0748edeee35244a8a020df5ae44da34f "复杂无线环境跨障碍物场景")  
复杂无线环境跨障碍物场景

### 多用户并发的高密场景

在用户分布较为密集的办公区，环境干扰小时，可开启多用户的并发传输（[MU-MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html "MU-MIMO")  ）来提升数据传输效率。而智能天线的定向波束选择，通过将同方向的用户聚合在一起采用相同定向波束传输，一方面提升终端接收信号的强度，另一方面减小不同方向终端数据之间的相互干扰。

![多用户并发的高密场景](https://download.huawei.com/mdl/image/download?uuid=27b71e951129443dab11cf5a17fbc159 "多用户并发的高密场景")  
多用户并发的高密场景

参考资源

1[阅读eBook：Wi-Fi智能天线](https://support.huawei.com/enterprise/zh/doc/EDOC1100212082)

2[阅读eBook：Wi-Fi 7](https://support.huawei.com/enterprise/zh/doc/EDOC1100325165)

3[华为WLAN智能天线技术白皮书](https://e.huawei.com/cn/material/networking/wlan/a33b1684cf284bdcb990f3f38dff2672)

4[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E6%99%BA%E8%83%BD%E5%A4%A9%E7%BA%BF.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MjI1MjE0MTZdfQ==
-->