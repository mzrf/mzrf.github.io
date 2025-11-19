# 波束成形天线——其工作原理和测试方法？
![波束成形天线——其工作原理和测试方法？](https://verkotan.com/wp-content/uploads/2020/03/5G-active-hero-tm-1024x740.jpg)

## 什么是波束成形天线？

_波束成形_是新一代智能天线最常用的方法。该方法利用天线阵列将无线电信号“引导”到特定方向，而不是像传统方法那样向扇区内的所有方向发射能量/信号。具体来说，多个小型天线通过适当调整每个天线信号的幅值和相位来控制组合发射信号的方向。该技术会根据需要调整每个组成天线发射信号的相位和幅值，从而产生相长或相消效应，最终将总发射信号集中到一个目标波束中。

波束成形天线正变得越来越普遍，并被广泛应用于雷达等领域，尤其是在电信领域。波束成形技术早在5G出现之前，也就是移动宽带发展的早期阶段就已经存在。波束成形的实现方式日趋复杂，这在一定程度上要归功于现代[大规模MIMO天线](https://idstch.com/technology/electronics/massive-mimo-is-seen-as-a-key-technology-to-delivering-mobile-5g/)。MIMO技术自3G时代就开始应用，它允许使用多个天线来发送和接收无线电信号。大规模MIMO天线拥有数量更多的子天线（约100个），使其能够更高效地传输无线电信号，从而实现极高的数据速率。
![天线波束成形差异](https://verkotan.com/wp-content/uploads/2021/02/Beamforming-1-1.png)

## 5G被动天线和主动天线有什么区别？

_无源天线_完全由无源元件构成，而_有源天线_系统则包含有源组件，用于控制天线性能，以确保在任何条件下都能保持最佳运行状态。虽然无源天线在 5G 网络中发挥着作用，但正是有源天线通过大规模 MIMO 技术实现了波束成形。有源天线能够满足许多不同的用户需求，例如增强信号强度或可配置天线。

5G 为无线通信树立了新的标准，其频率范围超越了以往几代技术。5G 技术包括 FR1（工作频率低于 6 GHz）和 FR2（包括 24 GHz 以上的频段以及 50 GHz 以上的超高频频段）。

![Verkotan 的 OTA 测试舱](https://verkotan.com/wp-content/uploads/2021/02/Beamforming-9-1-1024x768.jpg)


## 波束成形的基本原理

波束成形[天线](https://www.electronics-notes.com/articles/antennas-propagation/smart-adaptive-antennas/beamforming-beamsteering-antenna-basics.php)利用多个天线单元来控制波前的方向。通过改变天线阵列中各个信号的相位，可以形成特定角度的波束。然后，可以将平面波定向到所需方向。

![波束形成波](https://verkotan.com/wp-content/uploads/2021/02/Beamforming-3-1.gif)

当将合成波束指向远场的目标接收天线时，阵列中每个单元到目标的距离略有不同。此外，每个信号的路径长度差为 _d_ * cos( **θ** )，其中 θ 是各个信号的到达角。为了抵消这种差异，使每个信号以相同的相位到达，需要对每个单元应用移相器，从而在远场形成相干波束。这称为相干合成。

由于定向天线中各个信号叠加时会产生相长和相消效应，最终的辐射方向图会呈现多个场强不同的波瓣，且波瓣指向不同的角度。在这种情况下，信号强度会达到一个最大值，这些最大值之间由辐射强度降至零的波瓣隔开。功率最高的主瓣是预期的波束，而其他较小的旁瓣通常是不需要的，因为它们会向不必要的方向辐射不必要的辐射。

## 模拟和数字波束成形
实现天线波束成形的方法有很多种。接下来的几章将简要介绍模拟波束成形、数字波束成形和混合波束成形这三大类方法：

****数字波束成形：**** 在这种方法中，每个天线单元都拥有独立的收发器和数据转换器。这使得生成多组信号并将其应用于各个天线单元成为可能。天线阵列能够​​同时处理多个数据流并形成多个定向波束。凭借形成多个波束的能力，这种天线可以同时向多个接收器传输数据，从而高效地服务于多个用户。数字天线波束成形需要更多的硬件和信号处理资源，但通常来说是一种更具适应性的方法。

****模拟波束成形：**** 采用模拟方法时，整个天线仅使用一套数据转换器，并且只处理一个数据流。这意味着每组天线单元只能形成一个波束。数据流被分成若干信号路径，路径数量与天线单元数量相同，每个信号路径都经过一个移相器，然后发送到各个天线单元。模拟波束成形可以提高天线阵列的增益，从而扩大覆盖范围。模拟波束成形的缺点是整个频段的波束方向相同。

****混合波束成形：****这种方法结合了上述两种方法。天线阵列包含模拟波束成形的子阵列，以及子阵列信号的数字合成。这降低了能耗和设计复杂度，使其更具成本效益。

![模拟波束成形与数字波束成形](https://verkotan.com/wp-content/uploads/2021/02/beamforming-5-2.png)

## 智能天线

[智能天线](https://www.ofcom.org.uk/research-and-data/technology/general/emerging-tech/smart-antennas)能够分析其工作环境并改变天线方向图，从而根据环境变化适当调整自身功能。这使得智能天线能够获得更佳的性能。软件定义无线电、认知无线电、MIMO 等众多新型应用的部署，为智能天线技术的发展提供了支持。

![扇形智能天线阵列图像](https://verkotan.com/wp-content/uploads/2021/02/beamforming-2-2.png)

智能天线包含人工智能，能够进行信号处理，并能检测入射和出射信号的方向。它们还利用波束成形技术来改变发射天线的方向图以及发射信号的方向。由于智能天线需要具备多种功能，目前已开发出两种主要的智能天线技术。两种系统的基本功能相同，都能提供方向性。然而，它们在成本和复杂程度上有所不同，并且适用于不同的应用场景：

****切换波束智能天线：**** 切换波束智能天线旨在将多个天线的信号组合起来，形成几个预设的固定波束方向图。这些波束随后被引导至一个或多个特定方向。SBA（切换波束智能天线）可以根据具体情况选择最合适的方向。这种方法虽然灵活性稍逊，但其设计简单可靠，适用于多种应用场景。

****自适应阵列智能天线：**** 自适应天线阵列可以持续地将波束指向任意方向，并具有更灵活的辐射方向图。自适应阵列需要更高的智能水平，能够更好地感知周围环境。与SBA（表面阵列天线）相比，它们通常更精确、更高效，因为它们能够更好地抑制不必要的波束。与多用户MIMO网络相比，大规模MIMO在基站中使用了大量的天线。它可以被视为多用户MIMO的直接扩展。了解更多关于[多用户MIMO和大规模MIMO的](https://verkotan.com/2018/5g-wireless-and-beamforming-antenna-measurements-at-verkotan/)信息。

## 波束成形天线是如何测试的？

本文主要探讨大型波束成形天线阵列的测试。典型案例是采用波束成形有源天线阵列的4G或5G基站。波束成形天线的OTA性能测试可分为两大类：无源天线测试和有源天线测试。测试完成后，我们的[AntView®工具](https://verkotan.com/services/measurement-analyzing-tool/)能够可视化和整理数据，使天线测量结果的分析和存储更加便捷高效。

我们提供 AntView® 工具的免费演示版。您可以在我们的[AntView® 演示](https://verkotan.com/2021/request-a-demo-access-to-antenna-pattern-analysis-tool-antview/)新闻页面找到如何使用 AntView® 以及如何获取 AntView® 演示版使用权限的说明。

![AntView 工具](https://verkotan.com/wp-content/uploads/2021/02/Beamforming-4-1.png)

AntView®

#### 1. 无源天线测试

[无源天线测试](https://verkotan.com/services/antenna-radiation-pattern-measurements/)采用OTA测试方法，将测试信号直接馈入天线阵列，然后测量输出的射频信号。被测设备（DUT）通常仅包含无源天线阵列，不包含任何有源无线电单元。这使得无源天线测试简便易行，且结果易于比较。无源天线性能测量主要包括测量增益、方向性、效率、旁瓣比等特性。通常测量二维截面图或完整的三维方向图。每个天线端口可以单独测量，然后在后处理中使用端口权重进行波束成形；或者使用波束成形合成器在测量时生成所需的波束。  

![Verkotan OTA 测试](https://verkotan.com/wp-content/uploads/2020/03/P7230571-scaled-e1585336502656-1024x768.jpg)

OTA 测试正在进行中

#### 2. 有源天线测试

[有源天线的测试](https://verkotan.com/services/5g-wireless-testing/)环境与此类似。然而，有源天线的天线端口是嵌入在设备内部的。大部分射频信号生成步骤都在无线电单元内部完成。测试必须在有源模式下进行，即被测设备 (DUT) 处于信号传输模式，无线电单元和天线阵列的工作方式与实际网络中的工作方式相同。由于无线电单元和有源天线阵列的紧密集成，越来越多传统上在传导测试设置中测量的参数必须在辐射条件下进行测试。在 FR1 频段，典型的空中测量参数包括发射功率和基站灵敏度。此外，在 FR2 频段，所有射频参数都必须通过空中测量进行评估。这些参数包括 EVM、ACRL、阻塞、选择性、杂散发射等等。

![5G波束成形示意图](https://verkotan.com/wp-content/uploads/2021/02/Beamformin-article-1.png)

采用平面波转换器的波束成形有源天线测试装置

## 3GPP 测试方法

目前，[3GPP](https://verkotan.com/2020/verkotan-has-extended-the-scope-accredited-test-laboratory-3gpp-ts-37-145-2-2/)（第三代合作伙伴计划）测试标准中描述了多种用于测试波束成形有源天线的OTA测量系统类型。定义波束成形有源天线一致性评估的标准是3GPP TS 38.141-2和3GPP TS 37.145-2。这些标准参考了3GPP TR 37.941，后者给出了测试系统类型、程序和不确定度计算方法的定义。主要的测试系统类型包括室内消声室、紧凑型天线测试场（CATR）和平面波合成器。

#### 1. 室内消声室

室内消声室是指测量距离足够大的房间，使得被测器件 (DUT) 在远场条件下进行测试，远场条件由夫琅禾费距离定义。所需测试室的尺寸可能相当大，具体取决于频率和被测器件的尺寸。

#### 2. 紧凑型天线范围

[紧凑型天线测试场（CATR）](https://www.litepoint.com/wp-content/uploads/2019/07/5G-OTA-article-060419-web.pdf)测试系统采用射频反射器。辐射信号经抛物面反射器反射，从而在比夫琅禾费判据要求的距离更短的距离上形成远场条件。

#### 3. 近场到远场方法

另一种方法是利用近场到远场 (NF-FF) 转换进行天线近场测量，其中远场特性通过软件和必要的转换算法计算得出。这种方法显著缩短了测量远场特性所需的距离。这使得测试实验室能够在不损失测量精度的前提下缩小消声室的尺寸。Verkotan 凭借其宽带宽喇叭天线装置，可为整个 FR1 频段提供主动式[近场到远场天线测试服务](https://verkotan.com/services/5g-wireless-testing/)。我们可以测试各种天线特性，并为客户提供天线方向图测试。

![Verkotan 5G 测试](https://verkotan.com/wp-content/uploads/2020/03/Labrat-1-ta%C2%A6%C3%AAyskoko-011-3-1024x684.jpg)

Verkotan 的 NF-to-FF 实验室

#### 4. 平面波合成器

在采用平面波合成的测试系统中，远场由_平面波转换器_在测试区域产生。平面波转换器是一种相控阵天线，可替代传统测试系统天线。测试信号馈入转换器的各个天线单元，通过控制器调节阵列中每个单元的幅值和相位，从而在测试区域产生平面波场。

Verkotan 使用[R&S PWC200 平面波转换器](https://www.rohde-schwarz.com/fi/product/pwc200-productstartpage_63493-533696.html)进行[平面波合成有源天线测试服务](https://verkotan.com/2020/verkotan-provides-fr1-active-antenna-testing-service-according-to-3gpp-ts38-141-2/)，该服务支持 2.3-3.8GHz 的带宽，涵盖了最重要的 FR1 5G 频段。可测试尺寸最大达一米的 gNB。平面波转换器 (PWC) 专用于 5G 大规模 MIMO 基站测试。  

![pwc200 verkotan](https://verkotan.com/wp-content/uploads/2020/03/TM-5G-e1585575043954-954x1024.jpg)

Verkotan的平面波合成实验室

## 波束成形简述

波束成形已成为提升无线通信数据速率的标准技术。它是大规模MIMO技术的基础，并应用于5G基站和客户端设备。波束成形能够动态调整天线方向图，从而提高对网络环境的适应性。

由于无线电单元与天线集成度的提高，波束成形天线的测试面临着新的挑战。因此，越来越多原本在传导测试环境下进行的测试用例现在需要在无线天线（OTA）环境下进行。大型天线的测试要求测试系统具备远场条件，而这需要专门的测试设备和方法来实现，尤其是在有源天线测试中。

----------

如果您想了解更多关于OTA测试的信息， 还可以阅读我们关于[OTA - 无线性能测试](https://verkotan.com/2020/wireless-performance/)或[手机波](https://verkotan.com/2020/cell-phone-waves-why-testing-cell-phone-waves-is-crucial/)的其他文章。

## 参考

-   [https://www.electronics-notes.com/articles/antennas-propagation/smart-adaptive-antennas/what-is-smart-adaptive-antenna-technology.php](https://www.electronics-notes.com/articles/antennas-propagation/smart-adaptive-antennas/what-is-smart-adaptive-antenna-technology.php)
-   [https://www.electronics-notes.com/articles/antennas-propagation/smart-adaptive-antennas/beamforming-beamsteering-antenna-basics.php](https://www.electronics-notes.com/articles/antennas-propagation/smart-adaptive-antennas/beamforming-beamsteering-antenna-basics.php)
-   [https://www.ofcom.org.uk/research-and-data/technology/general/emerging-tech/smart-antennas](https://www.ofcom.org.uk/research-and-data/technology/general/emerging-tech/smart-antennas)
-   [大规模MIMO天线被视为实现移动5G的关键技术 | 国际防务安全与技术公司 (idstch.com)](https://idstch.com/technology/electronics/massive-mimo-is-seen-as-a-key-technology-to-delivering-mobile-5g/)
-   [https://www.metaswitch.com/knowledge-center/reference/what-is-beamforming-beam-steering-and-beam-switching-with-massive-mimo](https://www.metaswitch.com/knowledge-center/reference/what-is-beamforming-beam-steering-and-beam-switching-with-massive-mimo)
-   [https://www.analog.com/en/analog-dialogue/articles/phased-array-beamforming-ics-simplify-antenna-design.html#](https://www.analog.com/en/analog-dialogue/articles/phased-array-beamforming-ics-simplify-antenna-design.html)
-   [5G-OTA-article-060419-web.pdf (litepoint.com)](https://www.litepoint.com/wp-content/uploads/2019/07/5G-OTA-article-060419-web.pdf)
-   [寻找测试大规模 MIMO 5G 的方法 | 微波与射频 (mwrf.com)](https://www.mwrf.com/technologies/systems/article/21848244/microwaves-rf-finding-ways-to-test-massive-mimo-5g)

----------
转载自: [Verkotan](https://verkotan.com/2021/beamforming-antennas-how-they-work-and-are-tested/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNzUxMzczMzRdfQ==
-->